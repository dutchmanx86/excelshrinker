"""
Generate Workbook Index
Creates a compact index summary from MASTER_WORKBOOK_ANALYSIS.md for faster querying.
This index can be used to quickly identify relevant sheets before sending full content to LLM.
"""
import argparse
import re
from pathlib import Path
from typing import Dict


def build_sheet_index(markdown_content: str) -> Dict[str, list]:
    """
    Build a lightweight index of all sheets in the markdown file.

    For each sheet, extracts section-level information:
    - Section name
    - Section Type
    - Description & Purpose
    - Key Components
    - Notes & Customizations

    Args:
        markdown_content: Full content of MASTER_WORKBOOK_ANALYSIS.md

    Returns:
        Dictionary mapping sheet names to list of section summaries
    """
    index = {}

    # Split by sheet headers (lines starting with # SHEET X:)
    sheet_sections = re.split(r'\n# SHEET \d+: ', markdown_content)

    for section in sheet_sections[1:]:  # Skip first split (before any sheets)
        lines = section.split('\n')
        sheet_name = lines[0].strip()  # First line after split is sheet name

        # Parse sections within this sheet
        sections = []
        current_section = None

        for line in lines[1:]:
            # Section header (### SectionName)
            if line.startswith('### '):
                # Save previous section if exists
                if current_section and current_section.get('name'):
                    sections.append(current_section)

                # Start new section
                current_section = {
                    'name': line.replace('### ', '').strip(),
                    'type': None,
                    'description': None,
                    'components': None,
                    'notes': None
                }

            # Extract specific fields within section
            elif current_section:
                if line.startswith('- **Section Type**:'):
                    current_section['type'] = line.replace('- **Section Type**:', '').strip()
                elif line.startswith('- **Description & Purpose**:'):
                    current_section['description'] = line.replace('- **Description & Purpose**:', '').strip()
                elif line.startswith('- **Key Components**:'):
                    current_section['components'] = line.replace('- **Key Components**:', '').strip()
                elif line.startswith('- **Notes & Customizations**:'):
                    current_section['notes'] = line.replace('- **Notes & Customizations**:', '').strip()
                elif line.startswith('    - **Frequency**:'):
                    # Extract time series frequency (e.g., "Annual, Monthly")
                    if 'time_range' not in current_section:
                        current_section['time_range'] = {}
                    current_section['time_range']['frequency'] = line.replace('    - **Frequency**:', '').strip()
                elif line.strip().startswith('- Annual:') or line.strip().startswith('- Monthly:') or line.strip().startswith('- Quarterly:'):
                    # Extract simplified date range without anchor points
                    # e.g., "Monthly: 2015-01-31 to 2027-12-31" -> "Monthly: 2015-2027"
                    if 'time_range' not in current_section:
                        current_section['time_range'] = {}

                    parts = line.strip().split(':', 1)
                    if len(parts) == 2:
                        freq_type = parts[0].replace('-', '').strip()  # "Annual", "Monthly", etc.
                        range_text = parts[1].strip()

                        # Extract just the year range, ignoring anchor points
                        # Look for pattern like "2015-01-31 to 2027-12-31" or "likely 2011-2023"
                        year_match = re.search(r'(\d{4}).*?(?:to|-).*?(\d{4})', range_text)
                        if year_match:
                            start_year, end_year = year_match.groups()
                            current_section['time_range'][freq_type.lower()] = f"{start_year}-{end_year}"
                        elif 'likely' in range_text:
                            # Handle "likely 2011-2023" format
                            year_match = re.search(r'(\d{4})-(\d{4})', range_text)
                            if year_match:
                                start_year, end_year = year_match.groups()
                                current_section['time_range'][freq_type.lower()] = f"{start_year}-{end_year}"

        # Don't forget the last section
        if current_section and current_section.get('name'):
            sections.append(current_section)

        index[sheet_name] = sections

    return index


def generate_index_markdown(index: Dict[str, list]) -> str:
    """
    Generate a compact markdown index from the sheet index.

    Args:
        index: Sheet index from build_sheet_index()

    Returns:
        Markdown formatted index
    """
    output = "# Workbook Index\n\n"
    output += "This is a compact index of all sheets in the workbook for quick reference.\n"
    output += "Use this to identify relevant sheets before querying the full MASTER_WORKBOOK_ANALYSIS.md\n\n"
    output += f"**Total Sheets**: {len(index)}\n\n"
    output += "---\n\n"

    for sheet_name, sections in index.items():
        output += f"## {sheet_name}\n\n"

        # Output each section
        for section in sections:
            output += f"### {section['name']}\n"

            if section['type']:
                output += f"- **Section Type**: {section['type']}\n"
            if section['description']:
                output += f"- **Description & Purpose**: {section['description']}\n"
            if section['components']:
                output += f"- **Key Components**: {section['components']}\n"
            if section.get('time_range'):
                # Format time range concisely
                time_info = []
                tr = section['time_range']
                if 'annual' in tr:
                    time_info.append(f"Annual: {tr['annual']}")
                if 'monthly' in tr:
                    time_info.append(f"Monthly: {tr['monthly']}")
                if 'quarterly' in tr:
                    time_info.append(f"Quarterly: {tr['quarterly']}")
                if time_info:
                    output += f"- **Time Range**: {', '.join(time_info)}\n"
            if section['notes']:
                output += f"- **Notes & Customizations**: {section['notes']}\n"

            output += "\n"

        output += "---\n\n"

    return output


def main():
    """
    Main function to generate workbook index.
    """
    parser = argparse.ArgumentParser(
        description="Generate a compact index from MASTER_WORKBOOK_ANALYSIS.md"
    )
    parser.add_argument(
        "dataset",
        help="Name of the dataset folder (e.g., 'alphasense')"
    )

    args = parser.parse_args()

    # Find the master markdown file
    base_dir = Path(__file__).parent
    dataset_dir = base_dir / "datasets" / args.dataset
    markdown_file = dataset_dir / "processing_outputs" / "MASTER_WORKBOOK_ANALYSIS.md"

    if not markdown_file.exists():
        print(f"ERROR: File not found: {markdown_file}")
        return

    print(f"Reading: {markdown_file}")
    with open(markdown_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    print(f"File size: {len(markdown_content):,} bytes")
    print("Building index...")

    # Build the index
    index = build_sheet_index(markdown_content)
    print(f"Found {len(index)} sheets")

    # Generate index markdown
    index_markdown = generate_index_markdown(index)

    # Save to file
    output_file = dataset_dir / "processing_outputs" / "WORKBOOK_INDEX.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(index_markdown)

    print(f"\nIndex saved to: {output_file}")
    print(f"Index size: {len(index_markdown):,} bytes")
    print(f"Compression ratio: {len(index_markdown) / len(markdown_content):.1%}")


if __name__ == "__main__":
    main()
