"""Link checker for awesome-ogd-switzerland README.

This script extracts all URLs from readme.md and checks their availability.
"""

import re
import time
from pathlib import Path
from typing import List, Tuple
from urllib.parse import urlparse

import requests
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.table import Table
from rich.panel import Panel
from rich import box

console = Console()

# Timeout for requests
REQUEST_TIMEOUT = 10
# User agent to avoid blocking
USER_AGENT = "Mozilla/5.0 (compatible; Link-Checker/1.0)"


def extract_urls_from_markdown(file_path: Path) -> List[str]:
    """Extract all URLs from a markdown file."""
    console.log(f"Reading file: {file_path}")
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match markdown links [text](url) and plain URLs
    markdown_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
    urls = [url for _, url in markdown_links]
    
    # Also find plain URLs (http:// or https://)
    plain_urls = re.findall(r'https?://[^\s\)]+', content)
    urls.extend(plain_urls)
    
    # Remove duplicates and anchors
    unique_urls = []
    seen = set()
    for url in urls:
        # Remove anchor fragments
        clean_url = url.split('#')[0]
        # Skip if it's just an anchor or already seen
        if clean_url and clean_url not in seen:
            seen.add(clean_url)
            unique_urls.append(clean_url)
    
    console.log(f"Found {len(unique_urls)} unique URLs")
    return unique_urls


def check_url(url: str) -> Tuple[str, bool, int, str]:
    """Check if a URL is accessible.
    
    Returns:
        Tuple of (url, is_available, status_code, error_message)
    """
    headers = {'User-Agent': USER_AGENT}
    
    try:
        response = requests.head(
            url,
            timeout=REQUEST_TIMEOUT,
            allow_redirects=True,
            headers=headers
        )
        
        # If HEAD fails, try GET
        if response.status_code >= 400:
            response = requests.get(
                url,
                timeout=REQUEST_TIMEOUT,
                allow_redirects=True,
                headers=headers
            )
        
        is_available = response.status_code < 400
        return (url, is_available, response.status_code, "")
        
    except requests.exceptions.Timeout:
        return (url, False, 0, "Timeout")
    except requests.exceptions.ConnectionError:
        return (url, False, 0, "Connection Error")
    except requests.exceptions.TooManyRedirects:
        return (url, False, 0, "Too Many Redirects")
    except requests.exceptions.RequestException as e:
        return (url, False, 0, str(e)[:50])
    except Exception as e:
        return (url, False, 0, f"Unknown Error: {str(e)[:50]}")


def check_all_links(urls: List[str]) -> List[Tuple[str, bool, int, str]]:
    """Check all URLs with a progress bar."""
    results = []
    
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("({task.completed}/{task.total})"),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        task = progress.add_task("[cyan]Checking links...", total=len(urls))
        
        for url in urls:
            result = check_url(url)
            results.append(result)
            
            # Update progress with status
            status = "✓" if result[1] else "✗"
            progress.update(task, advance=1, description=f"[cyan]Checking links... {status} {url[:50]}")
            
            # Small delay to avoid overwhelming servers
            time.sleep(0.1)
    
    return results


def generate_report(results: List[Tuple[str, bool, int, str]]) -> None:
    """Generate and display the report."""
    total = len(results)
    available = sum(1 for _, is_avail, _, _ in results if is_avail)
    unavailable = total - available
    
    # Summary statistics
    console.print()
    console.print(Panel.fit(
        f"[bold green]Available:[/bold green] {available}\n"
        f"[bold red]Unavailable:[/bold red] {unavailable}\n"
        f"[bold blue]Total:[/bold blue] {total}\n"
        f"[bold yellow]Success Rate:[/bold yellow] {(available/total*100):.1f}%",
        title="[bold cyan]Link Check Summary[/bold cyan]",
        border_style="cyan"
    ))
    
    # Table of unavailable links
    if unavailable > 0:
        console.print()
        table = Table(
            title="[bold red]Unavailable Links[/bold red]",
            box=box.ROUNDED,
            show_lines=True
        )
        table.add_column("URL", style="cyan", no_wrap=False)
        table.add_column("Status Code", style="yellow", justify="center")
        table.add_column("Error", style="red")
        
        for url, is_avail, status_code, error in results:
            if not is_avail:
                status_str = str(status_code) if status_code > 0 else "-"
                error_str = error if error else "HTTP Error"
                table.add_row(url, status_str, error_str)
        
        console.print(table)
    else:
        console.print()
        console.print("[bold green]✓ All links are accessible![/bold green]")
    
    # Save plain text report
    report_file = Path("link-check-report.txt")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write("Link Check Report\n")
        f.write("=" * 80 + "\n\n")
        f.write(f"Total URLs checked: {total}\n")
        f.write(f"Available: {available}\n")
        f.write(f"Unavailable: {unavailable}\n")
        f.write(f"Success Rate: {(available/total*100):.1f}%\n\n")
        
        if unavailable > 0:
            f.write("Unavailable Links:\n")
            f.write("-" * 80 + "\n")
            for url, is_avail, status_code, error in results:
                if not is_avail:
                    f.write(f"\nURL: {url}\n")
                    f.write(f"Status Code: {status_code if status_code > 0 else 'N/A'}\n")
                    f.write(f"Error: {error if error else 'HTTP Error'}\n")

    # Save markdown report
    md_report_file = Path("link-check-report.md")
    with open(md_report_file, 'w', encoding='utf-8') as f:
        f.write(f"# Link Check Report\n\n")
        f.write(f"**Total URLs checked:** {total}  \n")
        f.write(f"**Available:** {available}  \n")
        f.write(f"**Unavailable:** {unavailable}  \n")
        f.write(f"**Success Rate:** {(available/total*100):.1f}%\n\n")

        if unavailable > 0:
            f.write("## Unavailable Links\n\n")
            f.write("| URL | Status Code | Error |\n")
            f.write("| --- | :---: | --- |\n")
            for url, is_avail, status_code, error in results:
                if not is_avail:
                    status_str = str(status_code) if status_code > 0 else "-"
                    error_str = error if error else "HTTP Error"
                    # Markdown clickable link
                    md_url = f"[{url}]({url})"
                    f.write(f"| {md_url} | {status_str} | {error_str} |\n")
        else:
            f.write("All links are accessible!\n")

    console.print(f"\n[dim]Report saved to: {report_file} and {md_report_file}[/dim]")


def main():
    """Main entry point for the link checker."""
    console.print(Panel.fit(
        "[bold cyan]Link Checker for awesome-ogd-switzerland[/bold cyan]\n"
        "Checking all URLs in readme.md",
        border_style="cyan"
    ))
    
    # Find readme file
    readme_path = Path("readme.md")
    if not readme_path.exists():
        console.print("[bold red]Error: readme.md not found![/bold red]")
        return 1
    
    try:
        # Extract URLs
        urls = extract_urls_from_markdown(readme_path)
        
        if not urls:
            console.print("[yellow]No URLs found in readme.md[/yellow]")
            return 0
        
        # Check all links
        console.print()
        results = check_all_links(urls)
        
        # Generate report
        generate_report(results)
        
        # Return exit code based on results
        unavailable = sum(1 for _, is_avail, _, _ in results if not is_avail)
        return 1 if unavailable > 0 else 0
        
    except Exception as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
        return 1


if __name__ == "__main__":
    exit(main())

