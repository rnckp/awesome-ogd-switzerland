"""Count resource bullets by Markdown heading, without a fixed section list."""

import argparse
import re
from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.markdown import Markdown

console = Console()


def parse_resource_entries(readme_text):
    """Count each top-level bullet with an external link once.

    Secondary links do not add entries. Navigation links, prose, indented
    sub-bullets and fenced examples are excluded. Counts describe entries,
    not unique datasets or publishers; deliberate cross-references count again.
    """
    sections, details = Counter(), Counter()
    headings = {}
    fence = None
    for line in readme_text.splitlines():
        marker = re.match(r"^\s{0,3}(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        heading = re.match(r"^(#{1,6})\s+(.+?)(?:\s+#+)?\s*$", line)
        if heading:
            level = len(heading[1])
            headings = {k: v for k, v in headings.items() if k < level}
            headings[level] = heading[2]
            continue
        if 2 not in headings or not re.match(r"^[-*+]\s+", line):
            continue
        # A label may precede the link, as in "OKFN [[Website](https://...)]".
        if not re.search(r"\]\(<?https?://", line):
            continue
        sections[headings[2]] += 1
        path = " > ".join(headings[k] for k in sorted(headings) if k >= 2)
        details[path] += 1
    return dict(sections), dict(details)


# Preserve the import name used by older callers.
parse_all_data_sources = parse_resource_entries


def generate_report(readme_text):
    sections, details = parse_resource_entries(readme_text)
    lines = [
        "# Resource Entry Count Report",
        "",
        f"**Total resource entries:** {sum(sections.values())}",
        "",
        "Counts include data sources, interfaces, tools and related resources. "
        "Each resource bullet counts once, regardless of secondary links. "
        "Cross-references in separate sections count as separate entries; "
        "these are not counts of unique datasets or publishers.",
        "",
    ]
    for title, counts, label in [
        ("Summary by Main Section", sections, "Section"),
        ("Detailed Breakdown", details, "Category Path"),
    ]:
        lines += [f"## {title}", "", f"| {label} | Count |", "| --- | ---: |"]
        lines += [
            f"| {name.replace('|', r'\|')} | {count} |"
            for name, count in counts.items()
        ]
        lines.append("")
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", type=Path, nargs="?", default=Path("README.md"))
    parser.add_argument("-o", "--output", type=Path, default=Path("count_sources.md"))
    args = parser.parse_args(argv)
    if not args.readme.is_file():
        console.print(f"File not found: {args.readme}")
        return 1
    report = generate_report(args.readme.read_text(encoding="utf-8"))
    args.output.write_text(report, encoding="utf-8")
    console.print(Markdown(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
