"""Custom exceptions for boundary detection"""


class BoundaryDetectorError(Exception):
    """Base exception for boundary detector"""
    pass


class FileLoadError(BoundaryDetectorError):
    """Error loading Excel file"""
    
    def __init__(self, file_path: str, message: str = None):
        self.file_path = file_path
        default_message = f"Failed to load Excel file: {file_path}"
        super().__init__(message or default_message)


class SheetNotFoundError(BoundaryDetectorError):
    """Specified sheet not found in workbook"""
    
    def __init__(self, sheet_name: str, available_sheets: list = None):
        self.sheet_name = sheet_name
        self.available_sheets = available_sheets
        
        message = f"Sheet '{sheet_name}' not found"
        if available_sheets:
            message += f". Available sheets: {', '.join(available_sheets)}"
        
        super().__init__(message)


class DetectionError(BoundaryDetectorError):
    """Error during boundary detection process"""
    pass