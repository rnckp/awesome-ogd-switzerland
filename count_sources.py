"""
Script to count data sources in the README.md file and output a report with total and grouped counts.
"""

import re
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.markdown import Markdown

README_PATH = Path("readme.md")

console = Console()

# Sections that contain data sources to count
DATA_SOURCE_SECTIONS = [
    "Data Sources",
    "Geo Data",
    "Linked Open Data",
    "APIs",
    "Organizations, Initiatives, Events and Projects",
    "Newsletters",
    "Podcasts",
    "Miscellaneous",
    "Media",
    "Social Media",
    "International",
]


def parse_all_data_sources(readme_text):
    """Parse all data sources from multiple sections in the README."""
    # Find all ## level sections
    all_sections = list(re.finditer(r"^## (.+)$", readme_text, re.MULTILINE))

    section_counts = {}
    detailed_counts = {}

    for idx, section_match in enumerate(all_sections):
        section_name = section_match.group(1).strip()

        # Skip sections that don't contain data sources
        if section_name not in DATA_SOURCE_SECTIONS:
            continue

        # Get section content
        start = section_match.end()
        end = (
            all_sections[idx + 1].start()
            if idx + 1 < len(all_sections)
            else len(readme_text)
        )
        section_content = readme_text[start:end]

        # Parse this section
        section_total = 0
        subsection_counts = {}

        # Find all level 3 and level 4 headings in this section
        headings = list(
            re.finditer(r"^(###|####) (.+)$", section_content, re.MULTILINE)
        )

        current_level3 = None

        for h_idx, heading in enumerate(headings):
            level = heading.group(1)
            heading_name = heading.group(2).strip()
            h_start = heading.end()
            h_end = (
                headings[h_idx + 1].start()
                if h_idx + 1 < len(headings)
                else len(section_content)
            )
            heading_content = section_content[h_start:h_end]

            # Count markdown links (data sources)
            links = re.findall(r"^- \[.+?\]\(.+?\)", heading_content, re.MULTILINE)
            count = len(links)

            if level == "###":
                current_level3 = heading_name
                if count > 0:
                    full_key = f"{section_name} > {heading_name}"
                    subsection_counts[full_key] = (
                        subsection_counts.get(full_key, 0) + count
                    )
                    section_total += count
            elif level == "####":
                full_key = (
                    f"{section_name} > {current_level3} > {heading_name}"
                    if current_level3
                    else f"{section_name} > {heading_name}"
                )
                if count > 0:
                    subsection_counts[full_key] = count
                    section_total += count

        # Also count direct links under the section (not under any subsection)
        # Find content before first heading
        if headings:
            direct_content = section_content[: headings[0].start()]
        else:
            direct_content = section_content

        direct_links = re.findall(r"^- \[.+?\]\(.+?\)", direct_content, re.MULTILINE)
        if direct_links:
            section_total += len(direct_links)
            subsection_counts[section_name] = len(direct_links)

        if section_total > 0:
            section_counts[section_name] = section_total
            detailed_counts.update(subsection_counts)

    return section_counts, detailed_counts


def main():
    if not README_PATH.exists():
        console.log(f"[red]File not found: {README_PATH}")
        return

    readme_text = README_PATH.read_text(encoding="utf-8")
    section_counts, detailed_counts = parse_all_data_sources(readme_text)

    total = sum(section_counts.values())

    # Print report
    console.rule("[bold green]Complete Data Sources Report")
    console.print(
        f"\n[bold cyan]Total data sources across all sections:[/bold cyan] [bold magenta]{total}[/bold magenta]\n"
    )

    # Summary table by main section
    summary_table = Table(
        title="Summary by Main Section", show_header=True, header_style="bold magenta"
    )
    summary_table.add_column("Section", style="cyan", no_wrap=False)
    summary_table.add_column("Count", style="magenta", justify="right")

    for section, count in section_counts.items():
        summary_table.add_row(section, str(count))

    console.print(summary_table)
    console.print()

    # Detailed table
    if detailed_counts:
        detail_table = Table(
            title="Detailed Breakdown", show_header=True, header_style="bold green"
        )
        detail_table.add_column("Category Path", style="green", no_wrap=False)
        detail_table.add_column("Count", style="yellow", justify="right")

        for path, count in detailed_counts.items():
            detail_table.add_row(path, str(count))

        console.print(detail_table)
        console.print()

    # Markdown summary
    console.rule("[bold blue]Markdown Summary")
    md = "# Complete Data Sources Count Report\n\n"
    md += f"**Total data sources:** {total}\n\n"
    md += "## Summary by Main Section\n\n"
    md += "| Section | Count |\n"
    md += "|---------|-------|\n"
    for section, count in section_counts.items():
        md += f"| {section} | {count} |\n"

    if detailed_counts:
        md += "\n## Detailed Breakdown\n\n"
        md += "| Category Path | Count |\n"
        md += "|---------------|-------|\n"
        for path, count in detailed_counts.items():
            md += f"| {path} | {count} |\n"

    console.print(Markdown(md))

    # Save to file
    output_file = Path("count_sources.md")
    output_file.write_text(md, encoding="utf-8")
    console.print(f"\n[bold green]✓[/] Report saved to [cyan]{output_file}[/cyan]")


if __name__ == "__main__":
    main()
