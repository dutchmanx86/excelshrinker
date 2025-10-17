"""Data models for format detection results"""

from dataclasses import dataclass, field
from typing import Optional, Dict, Any


@dataclass
class FormatRange:
    """
    Represents a range of cells with the same number format.
    
    Attributes:
        range: Excel range notation (e.g., "A1:C1" for ranges, "B1" for single cells)
        type: Format type - 'number', 'currency', 'percentage', 'string', 'date', 'time', 'other'
        value: Optional cell value (used for string types)
        parsed_date: Optional parsed date (for time period strings like "1Q24")
        original_value: Optional original string value before parsing
        format_code: Optional Excel format code string (for debugging)
        format_id: Optional Excel format ID number
        bold: Optional bold styling
        italic: Optional italic styling
        underline: Optional underline styling
        font_color: Optional font/text color
        bg_color: Optional background color
    """

    range: str
    type: str
    value: Optional[str] = None
    parsed_date: Optional[str] = None
    original_value: Optional[str] = None
    format_code: Optional[str] = None
    format_id: Optional[int] = None
    bold: Optional[bool] = None
    italic: Optional[bool] = None
    underline: Optional[bool] = None
    font_color: Optional[str] = None
    bg_color: Optional[str] = None
    date_series_info: Optional[Dict[str, Any]] = None
    
    def __post_init__(self):
        """Validate the format range"""
        valid_types = {'number', 'currency', 'percentage', 'string', 'date', 'time', 'other'}
        if self.type not in valid_types:
            raise ValueError(f"Invalid type '{self.type}'. Must be one of: {valid_types}")
    
    def to_dict(self, include_debug: bool = False) -> Dict[str, Any]:
        """
        Convert to dictionary for JSON serialization.
        
        Args:
            include_debug: If True, include format_code and format_id for debugging
        
        Returns:
            Dictionary representation of the format range
        """
        result = {
            'range': self.range,
            'type': self.type
        }
        
        # Add optional fields only if they have values
        if self.value is not None:
            result['value'] = self.value

        if self.parsed_date is not None:
            result['parsed_date'] = self.parsed_date

        if self.original_value is not None:
            result['original_value'] = self.original_value

        # Add styling attributes as keys only (not key-value pairs) when truthy
        if self.bold:
            result['bold'] = True

        if self.italic:
            result['italic'] = True

        if self.underline:
            result['underline'] = True

        if self.font_color:
            result['font_color'] = self.font_color

        if self.bg_color:
            result['bg_color'] = self.bg_color

        # Always include format_code for numbers (needed for inverted index compression)
        if self.format_code is not None and self.type not in ('string', 'date'):
            result['format_code'] = self.format_code

        if self.date_series_info is not None:
            result['date_series'] = self.date_series_info

        # Debug information (optional)
        if include_debug:
            if self.format_id is not None:
                result['format_id'] = self.format_id

        return result
    
    @property
    def is_single_cell(self) -> bool:
        """Check if this is a single cell (not a range)"""
        return ':' not in self.range
    
    @property
    def start_cell(self) -> str:
        """Get the starting cell of the range"""
        if ':' in self.range:
            return self.range.split(':')[0]
        return self.range
    
    @property
    def end_cell(self) -> str:
        """Get the ending cell of the range"""
        if ':' in self.range:
            return self.range.split(':')[1]
        return self.range
    
    def __repr__(self) -> str:
        """String representation for debugging"""
        parts = [f"FormatRange(range='{self.range}'", f"type='{self.type}'"]
        
        if self.value:
            parts.append(f"value='{self.value}'")
        if self.parsed_date:
            parts.append(f"parsed_date='{self.parsed_date}'")
        if self.bold:
            parts.append("bold")
        if self.italic:
            parts.append("italic")
        if self.underline:
            parts.append("underline")
        if self.font_color:
            parts.append(f"font_color='{self.font_color}'")
        if self.bg_color:
            parts.append(f"bg_color='{self.bg_color}'")

        return ', '.join(parts) + ')'