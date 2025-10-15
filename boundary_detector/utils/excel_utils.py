"""Excel utility functions"""

from typing import Any


def column_index_to_letter(col_index: int) -> str:
    """
    Convert 0-indexed column number to Excel letter notation.
    
    Args:
        col_index: Column index (0-indexed, e.g., 0 = 'A', 25 = 'Z', 26 = 'AA')
    
    Returns:
        Excel column letter (e.g., 'A', 'Z', 'AA', 'AB')
    
    Examples:
        >>> column_index_to_letter(0)
        'A'
        >>> column_index_to_letter(25)
        'Z'
        >>> column_index_to_letter(26)
        'AA'
        >>> column_index_to_letter(701)
        'ZZ'
    """
    result = ""
    col_num = col_index + 1  # Convert to 1-indexed
    
    while col_num > 0:
        col_num -= 1  # Adjust for 0-indexed in modulo
        remainder = col_num % 26
        result = chr(65 + remainder) + result
        col_num //= 26
    
    return result


def is_cell_empty(value: Any) -> bool:
    """
    Check if a cell value is considered empty.
    
    Optimized for speed - only checks for None or empty string.
    Any non-None value (including whitespace-only strings) is considered non-empty.
    
    Args:
        value: Cell value from calamine or openpyxl
    
    Returns:
        True if cell is empty, False otherwise
    
    Examples:
        >>> is_cell_empty(None)
        True
        >>> is_cell_empty("")
        True
        >>> is_cell_empty("  ")
        False  # Whitespace strings are considered non-empty for performance
        >>> is_cell_empty("Hello")
        False
        >>> is_cell_empty(0)
        False
        >>> is_cell_empty(0.0)
        False
    """
    # Only None and empty string are considered empty
    # This is fast and avoids expensive .strip() operations
    return value is None or value == ""