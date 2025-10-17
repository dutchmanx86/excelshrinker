"""Time range series detector for Excel spreadsheets"""

from typing import List, Optional, Tuple, Dict, Any
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from .time_period_parser import TimePeriodParser


class TimeSeriesInfo:
    """Information about a detected time series"""

    def __init__(
        self,
        start_col: int,
        end_col: int,
        row: int,
        series_type: str,
        increment: str,
        start_date: Optional[str] = None,
        pattern: Optional[str] = None
    ):
        self.start_col = start_col
        self.end_col = end_col
        self.row = row
        self.series_type = series_type  # 'annual', 'quarterly', 'monthly', 'repeating_annual', 'repeating_quarterly'
        self.increment = increment  # '1 year', '1 quarter', '1 month', etc.
        self.start_date = start_date
        self.pattern = pattern  # Description of the pattern

    def __repr__(self):
        return (f"TimeSeriesInfo(row={self.row}, cols={self.start_col}-{self.end_col}, "
                f"type={self.series_type}, increment={self.increment})")


class TimeRangeDetector:
    """
    Detects time series patterns in Excel rows.

    Supports:
    - Annual series (years incrementing by 1)
    - Quarterly series (quarters incrementing by 1)
    - Monthly series (months incrementing by 1)
    - Repeating annual (same year repeated N times before incrementing)
    - Repeating quarterly (same quarter repeated N times before incrementing)
    """

    def __init__(self):
        self.time_parser = TimePeriodParser()

    def detect_row_series(
        self,
        row_values: List[Any],
        row_number: int,
        start_col: int = 0,
        format_codes: Optional[List[Optional[str]]] = None
    ) -> List[TimeSeriesInfo]:
        """
        Detect all time series patterns in a row.

        Args:
            row_values: List of cell values in the row
            row_number: Row number (0-indexed)
            start_col: Starting column index (0-indexed)
            format_codes: Optional list of Excel number format codes for each cell

        Returns:
            List of TimeSeriesInfo objects (may be empty if no patterns detected)
        """
        if not row_values or len(row_values) < 2:
            return []

        detected_series = []
        i = 0

        while i < len(row_values):
            # Skip empty cells
            while i < len(row_values) and (row_values[i] is None or not str(row_values[i]).strip()):
                i += 1

            if i >= len(row_values):
                break

            # Extract contiguous non-empty values with their format codes
            segment_start = i
            non_empty_values = []
            segment_formats = []

            while i < len(row_values):
                val = row_values[i]
                if val is not None and str(val).strip():
                    non_empty_values.append((i, val))
                    # Get format code if available
                    if format_codes and i < len(format_codes):
                        segment_formats.append(format_codes[i])
                    else:
                        segment_formats.append(None)
                    i += 1
                else:
                    # Found a gap
                    break

            if len(non_empty_values) < 2:
                continue

            actual_start_col = start_col + non_empty_values[0][0]
            actual_end_col = start_col + non_empty_values[-1][0]

            # Try different pattern detectors in order of specificity
            # Sequential with format comes first as it's most specific
            detectors = [
                lambda vals, row, sc, ec: self._detect_sequential_with_format(
                    vals, row, sc, ec, segment_formats
                ),
                self._detect_monthly_series,
                self._detect_repeating_quarterly_series,
                self._detect_quarterly_series,
                self._detect_repeating_annual_series,
                self._detect_annual_series,
            ]

            for detector in detectors:
                result = detector(non_empty_values, row_number, actual_start_col, actual_end_col)
                if result:
                    detected_series.append(result)
                    break

        return detected_series

    def _detect_sequential_with_format(
        self,
        values: List[Tuple[int, Any]],
        row: int,
        start_col: int,
        end_col: int,
        format_codes: List[Optional[str]]
    ) -> Optional[TimeSeriesInfo]:
        """
        Detect sequential integer patterns with year/quarter-like format codes.
        E.g., 0, 1, 2, 3... with format ["Year" 0] -> Annual series

        Args:
            values: List of (index, value) tuples
            row: Row number
            start_col: Starting column
            end_col: Ending column
            format_codes: List of format codes for each value

        Returns:
            TimeSeriesInfo if pattern detected, None otherwise
        """
        if len(values) < 2 or not format_codes:
            return None

        # Extract numeric values
        numbers = []
        for idx, val in values:
            if isinstance(val, (int, float)):
                numbers.append(int(val))
            else:
                return None

        # Check if it's a sequential pattern starting from 0 or 1
        if len(numbers) < 2:
            return None

        start_num = numbers[0]
        if start_num not in (0, 1):
            return None

        # Verify it's sequential
        for i, num in enumerate(numbers):
            if num != start_num + i:
                return None

        # Check format codes for year/quarter/period indicators
        # Look at the first format code as representative
        first_format = format_codes[0] if format_codes else None
        if not first_format or first_format == 'General':
            return None

        # Normalize format code to lowercase for matching
        format_lower = first_format.lower()

        # Detect pattern type from format code
        if 'year' in format_lower or '"year"' in format_lower:
            series_type = 'annual'
            increment = '1 year'
            pattern = f"Sequential annual series (Year {start_num} to Year {numbers[-1]})"
            # Use relative year notation instead of actual dates
            start_date = f"Year {start_num}"

        elif 'quarter' in format_lower or '"q"' in format_lower or 'q0' in format_lower:
            series_type = 'quarterly'
            increment = '1 quarter'
            pattern = f"Sequential quarterly series (Q{start_num} to Q{numbers[-1]})"
            # Use relative quarter notation
            start_date = f"Q{start_num if start_num > 0 else 1}"

        elif 'period' in format_lower or 'month' in format_lower:
            series_type = 'monthly'
            increment = '1 month'
            pattern = f"Sequential period series ({start_num} to {numbers[-1]})"
            # Use relative period notation
            start_date = f"Period {start_num}"

        else:
            # Has a custom format but not recognized as time series
            return None

        return TimeSeriesInfo(
            start_col=start_col,
            end_col=end_col,
            row=row,
            series_type=series_type,
            increment=increment,
            start_date=start_date,
            pattern=pattern
        )

    def _detect_annual_series(
        self,
        values: List[Tuple[int, Any]],
        row: int,
        start_col: int,
        end_col: int
    ) -> Optional[TimeSeriesInfo]:
        """Detect annual series with 1-year increments"""
        if len(values) < 2:
            return None

        dates = []
        for idx, val in values:
            parsed_date = self._parse_to_date(val)
            if not parsed_date:
                return None
            dates.append(parsed_date)

        # Check if all dates increment by exactly 1 year
        for i in range(1, len(dates)):
            expected = dates[i-1] + relativedelta(years=1)
            # Allow some flexibility for year-end dates
            if not self._dates_close(dates[i], expected, days_tolerance=5):
                return None

        return TimeSeriesInfo(
            start_col=start_col,
            end_col=end_col,
            row=row,
            series_type='annual',
            increment='1 year',
            start_date=dates[0].isoformat(),
            pattern=f"Annual series from {dates[0].year} to {dates[-1].year}"
        )

    def _detect_quarterly_series(
        self,
        values: List[Tuple[int, Any]],
        row: int,
        start_col: int,
        end_col: int
    ) -> Optional[TimeSeriesInfo]:
        """Detect quarterly series with 1-quarter increments"""
        if len(values) < 2:
            return None

        # Parse as quarters
        quarters = []
        for idx, val in values:
            quarter_info = self._parse_quarter(val)
            if not quarter_info:
                return None
            quarters.append(quarter_info)

        # Check if quarters increment by 1
        for i in range(1, len(quarters)):
            prev_q, prev_y = quarters[i-1]
            curr_q, curr_y = quarters[i]

            if prev_q == 4:
                expected_q, expected_y = 1, prev_y + 1
            else:
                expected_q, expected_y = prev_q + 1, prev_y

            if curr_q != expected_q or curr_y != expected_y:
                return None

        start_q, start_y = quarters[0]
        end_q, end_y = quarters[-1]

        return TimeSeriesInfo(
            start_col=start_col,
            end_col=end_col,
            row=row,
            series_type='quarterly',
            increment='1 quarter',
            start_date=f"{start_y}-Q{start_q}",
            pattern=f"Quarterly series from Q{start_q} {start_y} to Q{end_q} {end_y}"
        )

    def _detect_monthly_series(
        self,
        values: List[Tuple[int, Any]],
        row: int,
        start_col: int,
        end_col: int
    ) -> Optional[TimeSeriesInfo]:
        """Detect monthly series with 1-month increments"""
        if len(values) < 3:  # Need at least 3 for monthly
            return None

        dates = []
        for idx, val in values:
            parsed_date = self._parse_to_date(val)
            if not parsed_date:
                return None
            dates.append(parsed_date)

        # Check if all dates increment by approximately 1 month
        # Month increments vary (28-31 days), so we check year/month separately
        for i in range(1, len(dates)):
            prev = dates[i-1]
            curr = dates[i]

            # Calculate expected next month
            expected = prev + relativedelta(months=1)

            # Check if year and month match (day can vary due to month-end)
            if curr.year != expected.year or curr.month != expected.month:
                return None

        return TimeSeriesInfo(
            start_col=start_col,
            end_col=end_col,
            row=row,
            series_type='monthly',
            increment='1 month',
            start_date=dates[0].isoformat(),
            pattern=f"Monthly series from {dates[0].strftime('%Y-%m')} to {dates[-1].strftime('%Y-%m')}"
        )

    def _detect_repeating_annual_series(
        self,
        values: List[Tuple[int, Any]],
        row: int,
        start_col: int,
        end_col: int
    ) -> Optional[TimeSeriesInfo]:
        """
        Detect annual values that repeat N times before incrementing.
        E.g., 2015, 2015, 2015, ..., 2016, 2016, 2016, ...
        """
        if len(values) < 4:
            return None

        # Try to parse as years (integers or dates)
        years = []
        for idx, val in values:
            year = self._extract_year(val)
            if year is None:
                return None
            years.append(year)

        # Find the repeat pattern
        first_year = years[0]
        repeat_count = 1

        for y in years[1:]:
            if y == first_year:
                repeat_count += 1
            else:
                break

        if repeat_count < 2:
            return None

        # Verify the pattern continues
        expected_year = first_year
        for i in range(0, len(years), repeat_count):
            chunk = years[i:i+repeat_count]
            if not chunk:
                break

            # All values in chunk should be the same year
            if not all(y == expected_year for y in chunk):
                # Allow partial chunk at the end
                if i + repeat_count < len(years):
                    return None

            expected_year += 1

        # Determine if repeat count suggests monthly (12) or other pattern
        if repeat_count == 12:
            increment_desc = f"{repeat_count} months (annual)"
        elif repeat_count == 3:
            increment_desc = f"{repeat_count} months (quarterly)"
        else:
            increment_desc = f"{repeat_count} periods"

        return TimeSeriesInfo(
            start_col=start_col,
            end_col=end_col,
            row=row,
            series_type='repeating_annual',
            increment=increment_desc,
            start_date=f"{first_year}-01-01",
            pattern=f"Annual values repeating {repeat_count} times from {first_year} to {years[-1]}"
        )

    def _detect_repeating_quarterly_series(
        self,
        values: List[Tuple[int, Any]],
        row: int,
        start_col: int,
        end_col: int
    ) -> Optional[TimeSeriesInfo]:
        """
        Detect quarterly values that repeat N times before incrementing.
        E.g., 1Q16, 1Q16, 1Q16, 2Q16, 2Q16, 2Q16, ...
        """
        if len(values) < 4:
            return None

        # Try to parse all as quarters
        quarters = []
        for idx, val in values:
            quarter_info = self._parse_quarter(val)
            if not quarter_info:
                return None
            quarters.append(quarter_info)

        # Find the repeat pattern
        first_quarter = quarters[0]
        repeat_count = 1

        for q in quarters[1:]:
            if q == first_quarter:
                repeat_count += 1
            else:
                break

        if repeat_count < 2:
            return None

        # Verify the pattern continues
        expected_q, expected_y = first_quarter
        for i in range(0, len(quarters), repeat_count):
            chunk = quarters[i:i+repeat_count]
            if not chunk:
                break

            # All values in chunk should be the same quarter
            if not all(q == (expected_q, expected_y) for q in chunk):
                # Allow partial chunk at the end
                if i + repeat_count < len(quarters):
                    return None

            # Increment to next quarter
            if expected_q == 4:
                expected_q = 1
                expected_y += 1
            else:
                expected_q += 1

        start_q, start_y = quarters[0]
        end_q, end_y = quarters[-1]

        return TimeSeriesInfo(
            start_col=start_col,
            end_col=end_col,
            row=row,
            series_type='repeating_quarterly',
            increment=f"{repeat_count} months (quarterly)",
            start_date=f"{start_y}-Q{start_q}",
            pattern=f"Quarterly values repeating {repeat_count} times from Q{start_q} {start_y} to Q{end_q} {end_y}"
        )

    def _parse_to_date(self, value: Any) -> Optional[date]:
        """Parse a value to a date object"""
        if isinstance(value, datetime):
            return value.date()
        elif isinstance(value, date):
            return value
        elif isinstance(value, (int, float)):
            # Try as year
            try:
                year = int(value)
                if 1900 <= year <= 2100:
                    return date(year, 1, 1)
            except:
                pass
        elif isinstance(value, str):
            # Try time period parser
            parsed = self.time_parser.parse_to_date(value)
            if parsed:
                return date.fromisoformat(parsed)

            # Try as year string
            try:
                year = int(value.strip())
                if 1900 <= year <= 2100:
                    return date(year, 1, 1)
            except:
                pass

        return None

    def _extract_year(self, value: Any) -> Optional[int]:
        """Extract year from a value"""
        if isinstance(value, (int, float)):
            year = int(value)
            if 1900 <= year <= 2100:
                return year
        elif isinstance(value, (datetime, date)):
            return value.year
        elif isinstance(value, str):
            # Try direct conversion
            try:
                year = int(value.strip())
                if 1900 <= year <= 2100:
                    return year
            except:
                pass

            # Try parsing as time period
            period_info = self.time_parser.get_period_info(value)
            if period_info:
                return period_info['year']

        return None

    def _parse_quarter(self, value: Any) -> Optional[Tuple[int, int]]:
        """Parse a value to (quarter, year) tuple"""
        if isinstance(value, str):
            period_info = self.time_parser.get_period_info(value)
            if period_info and period_info['period_type'] == 'quarter':
                return (period_info['quarter'], period_info['year'])

        return None

    def _dates_close(self, date1: date, date2: date, days_tolerance: int = 5) -> bool:
        """Check if two dates are within tolerance"""
        delta = abs((date1 - date2).days)
        return delta <= days_tolerance
