
"""Inverted index compression for JSON data with repeated strings"""

import json
import re
from typing import Dict, Any, List, Tuple, Union
from collections import Counter, defaultdict


class InvertedIndexCompressor:
    """
    Compress JSON using a true inverted index approach.

    Maps values to their locations:
    - Repeated values are stored once with a list of all their locations
    - Those entries are removed from the main data
    - Significantly reduces size when values are repeated

    Example:
        Original: 100 cells with value "Corporate"
        Compressed: "Corporate": {"type": "string", "ranges": ["A1", "A5", ...]}
                   (those 100 cells removed from main data)
    """

    def __init__(self, min_length: int = 3, min_occurrences: int = 2):
        """
        Initialize compressor.

        Args:
            min_length: Minimum string length to compress
            min_occurrences: Minimum number of times a value must appear to be compressed
        """
        self.min_length = min_length
        self.min_occurrences = min_occurrences
    
    def compress(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Compress format result data using inverted index.

        Groups entries by:
        1. String value (for strings that appear multiple times)
        2. Format signature (for numbers with same format+style)

        Args:
            data: Format result data with 'format_ranges' list

        Returns:
            Compressed result with structure:
            {
                "format_index": {
                    "fmt_1": {"number_format": "#,##0", "type": "number", "ranges": [...]},
                    ...
                },
                "string_index": {
                    "value1": {"type": "string", "ranges": ["A1", "A5", ...]},
                    ...
                },
                "date_series_definitions": {...},
                "compression_stats": {...}
            }
        """
        # Extract format_ranges
        format_ranges = data.get('format_ranges', [])

        # Build string inverted index (existing logic)
        string_index = defaultdict(lambda: {'type': None, 'ranges': []})
        value_counts = Counter()

        # Count string occurrences
        for entry in format_ranges:
            value = entry.get('value')
            if value is not None and isinstance(value, str) and len(value) >= self.min_length:
                value_counts[value] += 1

        # Build string index for qualifying values
        qualifying_strings = {
            value for value, count in value_counts.items()
            if count >= self.min_occurrences
        }

        for entry in format_ranges:
            value = entry.get('value')
            if value in qualifying_strings:
                range_str = entry.get('range')
                value_type = entry.get('type')
                string_index[value]['type'] = value_type
                string_index[value]['ranges'].append(range_str)

        # Convert to regular dict
        string_index = {k: dict(v) for k, v in string_index.items()}
        string_index = self._optimize_ranges(string_index)

        # Build format index (NEW: group numbers by format signature)
        # Format signature = (number_format, bold, italic, underline, font_color, bg_color)
        format_index = defaultdict(lambda: {
            'number_format': None, 'type': None, 'ranges': [],
            'bold': None, 'italic': None, 'underline': None, 'font_color': None, 'bg_color': None
        })
        format_counts = Counter()

        # Count format signature occurrences for numbers
        for entry in format_ranges:
            entry_type = entry.get('type')
            # Only group numbers (not strings or dates)
            if entry_type not in ('string', 'date'):
                # Create format signature: number_format + styling
                format_code = entry.get('format_code')
                bold = entry.get('bold')
                italic = entry.get('italic')
                underline = entry.get('underline')
                font_color = entry.get('font_color')
                bg_color = entry.get('bg_color')

                if format_code:
                    signature = (format_code, bold, italic, underline, font_color, bg_color)
                    format_counts[signature] += 1

        # Build format index for formats that appear multiple times
        qualifying_signatures = {
            sig for sig, count in format_counts.items()
            if count >= self.min_occurrences
        }

        # Group ranges by format signature
        for entry in format_ranges:
            entry_type = entry.get('type')
            if entry_type not in ('string', 'date'):
                format_code = entry.get('format_code')
                bold = entry.get('bold')
                italic = entry.get('italic')
                underline = entry.get('underline')
                font_color = entry.get('font_color')
                bg_color = entry.get('bg_color')

                signature = (format_code, bold, italic, underline, font_color, bg_color)
                if signature in qualifying_signatures:
                    range_str = entry.get('range')
                    format_index[signature]['number_format'] = format_code
                    format_index[signature]['type'] = entry_type
                    # Only add styling if truthy
                    if bold:
                        format_index[signature]['bold'] = True
                    if italic:
                        format_index[signature]['italic'] = True
                    if underline:
                        format_index[signature]['underline'] = True
                    if font_color:
                        format_index[signature]['font_color'] = font_color
                    if bg_color:
                        format_index[signature]['bg_color'] = bg_color
                    format_index[signature]['ranges'].append(range_str)

        # Convert to regular dict with cleaner keys
        format_index_clean = {}
        for idx, (signature, info) in enumerate(format_index.items(), 1):
            # Remove None styling attributes from the output
            clean_info = {k: v for k, v in info.items() if v is not None and v != []}
            format_index_clean[f"fmt_{idx}"] = clean_info

        # NOTE: Do NOT optimize format_index ranges - they're already ranges from format detector
        # The _optimize_ranges function is designed for single cells only

        # Extract date series (keep existing structure)
        date_series_definitions = data.get('date_series_definitions', {})

        # Build list of entries to exclude (in inverted indices)
        excluded_ranges = set()
        for info in string_index.values():
            for range_str in info['ranges']:
                excluded_ranges.add(range_str)
        for info in format_index_clean.values():
            for range_str in info['ranges']:
                excluded_ranges.add(range_str)

        # Compress ranges: exclude entries that are now in indices
        compressed_ranges = []
        for entry in format_ranges:
            range_str = entry.get('range')
            value = entry.get('value')
            entry_type = entry.get('type')

            # Skip if in string index
            if value in qualifying_strings:
                continue

            # Skip if in format index (check if signature matches)
            if entry_type not in ('string', 'date'):
                format_code = entry.get('format_code')
                bold = entry.get('bold')
                italic = entry.get('italic')
                underline = entry.get('underline')
                font_color = entry.get('font_color')
                bg_color = entry.get('bg_color')

                signature = (format_code, bold, italic, underline, font_color, bg_color)
                if signature in qualifying_signatures:
                    continue

            # Keep everything else
            compressed_ranges.append(entry)

        # Calculate compression stats
        original_size = len(json.dumps(data, separators=(',', ':')))
        string_index_size = len(json.dumps(string_index, separators=(',', ':')))
        format_index_size = len(json.dumps(format_index_clean, separators=(',', ':')))
        date_series_size = len(json.dumps(date_series_definitions, separators=(',', ':')))
        compressed_ranges_size = len(json.dumps(compressed_ranges, separators=(',', ':')))

        compressed_size = string_index_size + format_index_size + date_series_size + compressed_ranges_size

        entries_moved = len(format_ranges) - len(compressed_ranges)

        return {
            "format_index": format_index_clean,
            "string_index": string_index,
            "date_series_definitions": date_series_definitions,
            "remaining_ranges": compressed_ranges,
            "compression_stats": {
                "format_signatures": len(format_index_clean),
                "unique_strings": len(string_index),
                "entries_moved_to_index": entries_moved,
                "entries_remaining": len(compressed_ranges),
                "min_occurrences_threshold": self.min_occurrences,
                "original_size_bytes": original_size,
                "compressed_size_bytes": compressed_size,
                "string_index_size_bytes": string_index_size,
                "format_index_size_bytes": format_index_size,
                "date_series_size_bytes": date_series_size,
                "compressed_ranges_size_bytes": compressed_ranges_size,
                "compression_ratio": round(compressed_size / original_size, 3) if original_size > 0 else 1.0,
                "space_saved_bytes": original_size - compressed_size,
                "space_saved_percent": round((1 - compressed_size / original_size) * 100, 1) if original_size > 0 else 0
            }
        }

    def _optimize_ranges(self, inverted_index: Dict[str, Dict]) -> Dict[str, Dict]:
        """
        Optimize inverted index by converting consecutive cell references to range notation.

        E.g., ["A1", "A2", "A3", "B5"] -> ["A1:A3", "B5"]
        """
        for value, info in inverted_index.items():
            ranges = info.get('ranges', [])
            if len(ranges) > 1:
                optimized = self._compress_cell_references(ranges)
                info['ranges'] = optimized

        return inverted_index

    def _compress_cell_references(self, cell_refs: List[str]) -> List[str]:
        """
        Compress a list of cell references by detecting consecutive sequences.

        Args:
            cell_refs: List of cell references like ["S2", "T2", "U2", ...]

        Returns:
            List with consecutive references compressed to ranges like ["S2:U2", ...]
        """
        if not cell_refs:
            return []

        # Parse all cell references
        parsed = []
        for ref in cell_refs:
            col, row = self._parse_cell_reference(ref)
            if col is not None:
                parsed.append((ref, col, row))

        if not parsed:
            return cell_refs

        # Sort by row first, then column
        parsed.sort(key=lambda x: (x[2], x[1]))  # (row, col)

        # Group consecutive cells
        compressed = []
        group_start = parsed[0]
        group_end = parsed[0]

        for i in range(1, len(parsed)):
            current = parsed[i]
            current_ref, current_col, current_row = current
            end_ref, end_col, end_row = group_end

            # Check if current cell is consecutive
            is_consecutive = False

            # Same row, consecutive columns
            if current_row == end_row and current_col == end_col + 1:
                is_consecutive = True
            # Same column, consecutive rows
            elif current_col == end_col and current_row == end_row + 1:
                is_consecutive = True

            if is_consecutive:
                # Extend the group
                group_end = current
            else:
                # Save the current group and start a new one
                compressed.append(self._format_range(group_start, group_end))
                group_start = current
                group_end = current

        # Add the last group
        compressed.append(self._format_range(group_start, group_end))

        return compressed

    def _parse_cell_reference(self, cell_ref: str) -> Tuple[int, int]:
        """
        Parse cell reference into column index and row number.

        Args:
            cell_ref: Cell reference like "A1", "AB10"

        Returns:
            Tuple of (column_index, row_number) or (None, None) if parsing fails
        """
        match = re.match(r'^([A-Z]+)(\d+)$', cell_ref)
        if not match:
            return (None, None)

        col_letters = match.group(1)
        row_num = int(match.group(2))

        # Convert column letters to index (A=0, B=1, ..., Z=25, AA=26, etc.)
        col_idx = 0
        for char in col_letters:
            col_idx = col_idx * 26 + (ord(char) - ord('A') + 1)
        col_idx -= 1  # Convert to 0-indexed

        return (col_idx, row_num)

    def _format_range(self, start_cell: Tuple, end_cell: Tuple) -> str:
        """
        Format a range from start and end cell tuples.

        Args:
            start_cell: (ref, col_idx, row_num) tuple
            end_cell: (ref, col_idx, row_num) tuple

        Returns:
            Range string like "A1" or "A1:A3"
        """
        start_ref = start_cell[0]
        end_ref = end_cell[0]

        if start_ref == end_ref:
            return start_ref
        else:
            return f"{start_ref}:{end_ref}"

    def decompress(self, compressed: Dict[str, Any]) -> Dict[str, Any]:
        """
        Decompress data that was compressed with compress().

        Args:
            compressed: Compressed data with 'inverted_index' and 'data' keys

        Returns:
            Original decompressed data

        Raises:
            ValueError: If compressed data is malformed or missing required keys
        """
        # Validate input structure
        if not isinstance(compressed, dict):
            raise ValueError("Compressed data must be a dictionary")

        if 'inverted_index' not in compressed:
            raise ValueError("Missing 'inverted_index' key in compressed data")

        if 'data' not in compressed:
            raise ValueError("Missing 'data' key in compressed data")

        inverted_index = compressed.get('inverted_index', {})
        compressed_data = compressed.get('data', {})

        # Reconstruct format_ranges
        format_ranges = list(compressed_data.get('format_ranges', []))

        # Add back entries from inverted index
        for value, info in inverted_index.items():
            value_type = info['type']
            ranges = info['ranges']
            # Expand ranges back to individual cells
            for range_str in ranges:
                # Check if it's a range (contains ':')
                if ':' in range_str:
                    # Expand range to individual cells
                    expanded = self._expand_range(range_str)
                    for cell_ref in expanded:
                        format_ranges.append({
                            'range': cell_ref,
                            'type': value_type,
                            'value': value
                        })
                else:
                    # Single cell
                    format_ranges.append({
                        'range': range_str,
                        'type': value_type,
                        'value': value
                    })

        # Rebuild the original data structure
        result = dict(compressed_data)
        result['format_ranges'] = format_ranges

        return result

    def _expand_range(self, range_str: str) -> List[str]:
        """
        Expand a range string to individual cell references.

        Args:
            range_str: Range like "A1:A3" or "S2:U2"

        Returns:
            List of cell references like ["A1", "A2", "A3"]
        """
        if ':' not in range_str:
            return [range_str]

        start_ref, end_ref = range_str.split(':')
        start_col, start_row = self._parse_cell_reference(start_ref)
        end_col, end_row = self._parse_cell_reference(end_ref)

        if start_col is None or end_col is None:
            return [range_str]  # Return as-is if can't parse

        cells = []

        # Same row, different columns (horizontal range)
        if start_row == end_row:
            for col_idx in range(start_col, end_col + 1):
                col_letter = self._column_index_to_letter(col_idx)
                cells.append(f"{col_letter}{start_row}")
        # Same column, different rows (vertical range)
        elif start_col == end_col:
            col_letter = self._column_index_to_letter(start_col)
            for row_num in range(start_row, end_row + 1):
                cells.append(f"{col_letter}{row_num}")
        else:
            # 2D range - expand all cells
            for row_num in range(start_row, end_row + 1):
                for col_idx in range(start_col, end_col + 1):
                    col_letter = self._column_index_to_letter(col_idx)
                    cells.append(f"{col_letter}{row_num}")

        return cells

    def _column_index_to_letter(self, col_idx: int) -> str:
        """
        Convert column index to Excel column letters.

        Args:
            col_idx: 0-indexed column (0=A, 1=B, ..., 25=Z, 26=AA)

        Returns:
            Column letters like "A", "Z", "AA"
        """
        col_idx += 1  # Convert to 1-indexed
        letters = ""
        while col_idx > 0:
            col_idx, remainder = divmod(col_idx - 1, 26)
            letters = chr(65 + remainder) + letters
        return letters


def compress_format_result_json(
    json_data: Union[str, Dict],
    min_length: int = 3,
    min_occurrences: int = 2
) -> Dict[str, Any]:
    """
    Compress format detection JSON using inverted index (value -> locations mapping).

    Maps repeated values to their locations, removing them from the main data.
    Only compresses strings that appear at least min_occurrences times.

    Args:
        json_data: JSON string or dict to compress
        min_length: Minimum string length to compress
        min_occurrences: Minimum times a value must appear to be compressed

    Returns:
        Compressed result with inverted_index and data

    Example:
        >>> json_str = result.to_json()
        >>> compressed = compress_format_result_json(json_str, min_occurrences=2)
        >>> print(f"Saved {compressed['compression_stats']['space_saved_percent']}%")
    """
    # Parse JSON if string
    if isinstance(json_data, str):
        data = json.loads(json_data)
    else:
        data = json_data

    # Compress
    compressor = InvertedIndexCompressor(min_length=min_length, min_occurrences=min_occurrences)
    return compressor.compress(data)


def decompress_format_result_json(compressed: Dict[str, Any]) -> Dict[str, Any]:
    """
    Decompress format detection JSON.

    Args:
        compressed: Compressed data from compress_format_result_json()

    Returns:
        Original decompressed data
    """
    compressor = InvertedIndexCompressor()
    return compressor.decompress(compressed)


def save_compressed_json(compressed: Dict[str, Any], filepath: str):
    """
    Save compressed JSON to file.
    
    Args:
        compressed: Compressed data
        filepath: Path to save to
    """
    with open(filepath, 'w') as f:
        json.dump(compressed, f, indent=2)


def load_compressed_json(filepath: str) -> Dict[str, Any]:
    """
    Load and decompress JSON from file.
    
    Args:
        filepath: Path to load from
    
    Returns:
        Decompressed data
    """
    with open(filepath, 'r') as f:
        compressed = json.load(f)
    
    return decompress_format_result_json(compressed)