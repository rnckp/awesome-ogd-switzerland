"""Check README HTTP links, separating likely broken URLs from inconclusive checks."""

import argparse
import re
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from html import unescape
from pathlib import Path
from urllib.parse import urldefrag, urlsplit

import requests
from rich.console import Console
from rich.progress import track

console = Console()
REQUEST_TIMEOUT = 30
MAX_WORKERS = 10
USER_AGENT = "Mozilla/5.0 (compatible; Link-Checker/1.0)"


def extract_urls_from_markdown(file_path: Path) -> list[str]:
    """Extract HTTP(S) destinations from Markdown, HTML and plain text.

    Quotes and angle brackets delimit HTML attributes, so adjacent markup is
    never included. Balanced URL parentheses are retained; Markdown closing
    parentheses and surrounding prose punctuation are discarded. Fragments
    are removed because HTTP requests cannot validate client-side routes.
    """
    content = file_path.read_text(encoding="utf-8")
    urls = []
    seen = set()
    for match in re.finditer(r"""https?://[^\s<>"'\[\]`]+""", content):
        url = unescape(match[0])
        # Stop at the first unmatched closing parenthesis (Markdown syntax).
        depth = 0
        for index, char in enumerate(url):
            if char == "(":
                depth += 1
            elif char == ")":
                if depth == 0:
                    url = url[:index]
                    break
                depth -= 1
        url = urldefrag(url.rstrip(".,;:!?"))[0]
        if urlsplit(url).netloc and url not in seen:
            seen.add(url)
            urls.append(url)
    return urls


def classify_status(status_code: int) -> str:
    if 200 <= status_code < 400:
        return "reachable"
    if status_code in (404, 410):
        return "likely broken"
    return "needs review"


def check_url(url: str) -> tuple[str, str, int, str]:
    """Return URL, outcome, HTTP code and explanation.

    Retry failed HEAD checks with a streamed GET: some servers reject HEAD.
    Do not download response bodies (links can point at large datasets).
    """
    headers = {"User-Agent": USER_AGENT}
    for method in (requests.head, requests.get):
        try:
            with method(
                url,
                timeout=REQUEST_TIMEOUT,
                allow_redirects=True,
                headers=headers,
                stream=True,
            ) as response:
                code = response.status_code
                outcome = classify_status(code)
            if outcome == "reachable":
                return url, outcome, code, ""
            result = (
                url,
                outcome,
                code,
                {
                    401: "Authentication required; not evidence of a dead link",
                    403: "Access denied or bot protection; check in a browser",
                    404: "HTTP 404; verify the destination before removing",
                    410: "HTTP 410; resource reported gone",
                    429: "Rate limited; retry later",
                }.get(code, "Server or HTTP error; retry or check manually"),
            )
        except requests.exceptions.Timeout:
            result = (url, "needs review", 0, "Timeout; retry later")
        except requests.exceptions.TooManyRedirects:
            result = (url, "needs review", 0, "Redirect loop; check in a browser")
        except requests.exceptions.RequestException as error:
            result = (
                url,
                "needs review",
                0,
                f"Connection/request error: {type(error).__name__}",
            )
    return result


def check_all_links(urls):
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # map preserves input order for stable report diffs.
        return list(
            track(
                executor.map(check_url, urls),
                total=len(urls),
                description="Checking links",
                console=console,
            )
        )


def generate_report(results, output_path=Path("link-check-report.md")):
    total = len(results)
    reachable = sum(outcome == "reachable" for _, outcome, _, _ in results)
    broken = sum(outcome == "likely broken" for _, outcome, _, _ in results)
    review = total - reachable - broken
    rate = reachable / total * 100 if total else 0
    lines = [
        "# Link Check Report",
        "",
        f"**Checked at:** {datetime.now(timezone.utc).isoformat(timespec='seconds')}",
        f"**Total URLs checked:** {total}  ",
        f"**Reachable:** {reachable}  ",
        f"**Likely broken (404/410):** {broken}  ",
        f"**Needs review:** {review}  ",
        f"**Reachable rate:** {rate:.1f}%",
        "",
        "HTTP reachability does not verify page content, licensing, downloads or "
        "JavaScript routes. Fragments and internal anchors are not checked. "
        "Access blocks, rate limits, server errors and connection failures are "
        "inconclusive, not proof of dead links. Even 404/410 results should be "
        "confirmed before removing a resource.",
        "",
    ]
    for category in ("likely broken", "needs review"):
        rows = [r for r in results if r[1] == category]
        lines += [f"## {category.capitalize()}", ""]
        if not rows:
            lines += ["None.", ""]
            continue
        lines += ["| URL | HTTP status | Detail |", "| --- | :---: | --- |"]
        for url, _, code, detail in rows:
            safe_url = url.replace("|", "%7C")
            safe_detail = detail.replace("|", r"\|").replace("\n", " ")
            lines.append(
                f"| [{safe_url}](<{safe_url}>) | {code or '-'} | {safe_detail} |"
            )
        lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")
    console.print(
        f"Checked {total}: {reachable} reachable, {broken} likely broken, {review} need review."
    )
    console.print(f"Report saved to {output_path}")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("readme", type=Path, nargs="?", default=Path("README.md"))
    parser.add_argument(
        "-o", "--output", type=Path, default=Path("link-check-report.md")
    )
    args = parser.parse_args(argv)
    if not args.readme.is_file():
        console.print(f"File not found: {args.readme}")
        return 1
    results = check_all_links(extract_urls_from_markdown(args.readme))
    generate_report(results, args.output)
    # An inconclusive automated check alone should not fail CI.
    return 1 if any(r[1] == "likely broken" for r in results) else 0


if __name__ == "__main__":
    raise SystemExit(main())
