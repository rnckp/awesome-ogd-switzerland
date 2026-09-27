"""Regression checks for resource counting and link-check outcomes (no network)."""

import tempfile
import unittest
from pathlib import Path
from unittest.mock import MagicMock, patch

from awesome_ogd_switzerland import count_sources as counter
from awesome_ogd_switzerland import link_checker as checker


class HelperTests(unittest.TestCase):
    def test_counter_cli_accepts_input_and_output_paths(self):
        with tempfile.TemporaryDirectory() as temp:
            readme = Path(temp) / "directory.md"
            output = Path(temp) / "counts.md"
            readme.write_text("## Resources\n- [Data](https://example.org)\n")
            self.assertEqual(counter.main([str(readme), "--output", str(output)]), 0)
            self.assertIn("**Total resource entries:** 1", output.read_text())

    def test_checker_cli_writes_report_and_preserves_exit_status(self):
        with tempfile.TemporaryDirectory() as temp:
            readme = Path(temp) / "directory.md"
            output = Path(temp) / "links.md"
            readme.write_text("## Resources\n- [Data](https://example.org)\n")
            for outcome, code, status in [
                ("reachable", 200, 0),
                ("needs review", 403, 0),
                ("likely broken", 404, 1),
            ]:
                with (
                    self.subTest(outcome=outcome),
                    patch.object(
                        checker,
                        "check_all_links",
                        return_value=[("https://example.org", outcome, code, "")],
                    ) as check,
                ):
                    self.assertEqual(
                        checker.main([str(readme), "-o", str(output)]), status
                    )
                    check.assert_called_once_with(["https://example.org"])
                    self.assertIn("**Total URLs checked:** 1", output.read_text())

    def test_cli_missing_input_returns_failure(self):
        with tempfile.TemporaryDirectory() as temp:
            missing = str(Path(temp) / "missing.md")
            self.assertEqual(counter.main([missing]), 1)
            self.assertEqual(checker.main([missing]), 1)

    def test_counts_labels_secondary_links_and_arbitrary_headings(self):
        text = """# Directory
## Table of Contents
- [Renamed section](#renamed-section)
## Renamed section
- OKFN [[Website](https://example.org)] [[Source](https://example.org/repo)]
### Group
- [Dataset](https://example.org/data) with [API](https://example.org/api)
  - [Nested helper](https://example.org/nested)
##### Detail
- [Another](https://example.org/other)
## Another section
- [Resource](https://example.net)
"""
        summary, detail = counter.parse_resource_entries(text)
        self.assertEqual(summary, {"Renamed section": 3, "Another section": 1})
        self.assertEqual(detail["Renamed section > Group > Detail"], 1)
        self.assertEqual(detail["Another section"], 1)

    def test_counter_ignores_fenced_examples(self):
        text = """## Resources
```markdown
## Fake section
- [Fake](https://example.org/fake)
```
- [Real](https://example.org/real)
"""
        self.assertEqual(counter.parse_resource_entries(text)[0], {"Resources": 1})

    def test_url_extraction_handles_html_markdown_and_fragments(self):
        text = """[Link](https://example.org/a_(b)#part)
[Same](https://example.org/a_(b)#other)
<a href="https://example.org/tool"><img src="https://example.org/badge?a=1&amp;b=2"></a>
<https://example.org/auto>
Plain https://example.org/plain.
[Local](#heading) [Mail](mailto:test@example.org)
[Title](https://example.org/title "Title")
[ref]: https://example.org/reference
"""
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "README.md"
            path.write_text(text)
            self.assertEqual(
                checker.extract_urls_from_markdown(path),
                [
                    "https://example.org/a_(b)",
                    "https://example.org/tool",
                    "https://example.org/badge?a=1&b=2",
                    "https://example.org/auto",
                    "https://example.org/plain",
                    "https://example.org/title",
                    "https://example.org/reference",
                ],
            )

    @staticmethod
    def response(code):
        response = MagicMock()
        response.__enter__.return_value.status_code = code
        return response

    def test_head_failure_get_success_and_streaming(self):
        with (
            patch.object(checker.requests, "head", return_value=self.response(405)),
            patch.object(
                checker.requests, "get", return_value=self.response(200)
            ) as get,
        ):
            self.assertEqual(
                checker.check_url("https://example.org")[1:3], ("reachable", 200)
            )
            self.assertTrue(get.call_args.kwargs["stream"])

    def test_timeout_falls_back_to_get(self):
        with (
            patch.object(
                checker.requests,
                "head",
                side_effect=checker.requests.exceptions.Timeout,
            ),
            patch.object(checker.requests, "get", return_value=self.response(200)),
        ):
            self.assertEqual(checker.check_url("https://example.org")[1], "reachable")

    def test_http_errors_are_not_all_dead_links(self):
        for code, outcome in [
            (403, "needs review"),
            (429, "needs review"),
            (503, "needs review"),
            (404, "likely broken"),
            (410, "likely broken"),
        ]:
            with (
                self.subTest(code=code),
                patch.object(
                    checker.requests, "head", return_value=self.response(code)
                ),
                patch.object(checker.requests, "get", return_value=self.response(code)),
            ):
                self.assertEqual(checker.check_url("https://example.org")[1], outcome)

    def test_connection_failure_needs_review(self):
        with (
            patch.object(
                checker.requests,
                "head",
                side_effect=checker.requests.exceptions.ConnectionError,
            ),
            patch.object(
                checker.requests,
                "get",
                side_effect=checker.requests.exceptions.ConnectionError,
            ),
        ):
            self.assertEqual(
                checker.check_url("https://example.org")[1:3], ("needs review", 0)
            )

    def test_empty_and_mixed_reports(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "report.md"
            checker.generate_report([], path)
            self.assertIn("**Reachable rate:** 0.0%", path.read_text())
            checker.generate_report(
                [
                    ("https://example.org/ok", "reachable", 200, ""),
                    ("https://example.org/missing", "likely broken", 404, "Missing"),
                    ("https://example.org/blocked", "needs review", 403, "Blocked"),
                ],
                path,
            )
            report = path.read_text()
            self.assertIn("**Likely broken (404/410):** 1", report)
            self.assertIn("**Needs review:** 1", report)


if __name__ == "__main__":
    unittest.main()
