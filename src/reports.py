from __future__ import annotations
from datetime import date
import json
from typing import Iterable

from src.models.Employee import Employee


def employees_json(employees: Iterable[Employee]) -> str:
    """Return a JSON string for all employees sorted by yearly salary (desc) then last name (asc)."""
    sorted_employees = sorted(employees, key=lambda emp: (-emp.yearly_salary, emp.last_name))
    return json.dumps([emp.to_dict() for emp in sorted_employees], indent=2)


def quarterly_upcoming_enrollees(employees: Iterable[Employee], as_of: date | None = None) -> str:
    """Return a JSON string of employees who will qualify for enrolment by the end of the next quarter.

    An employee qualifies if they are not enrolled and will have been employed for at least 3 years
    by the last day of the next quarter relative to `as_of` (or today when None).
    Results are sorted by employment date (descending).
    """
    as_of = as_of or date.today()
    month = as_of.month
    year = as_of.year

    # Determine next quarter end date
    if 1 <= month <= 3:
        next_quarter_end = date(year, 6, 30)
    elif 4 <= month <= 6:
        next_quarter_end = date(year, 9, 30)
    elif 7 <= month <= 9:
        next_quarter_end = date(year, 12, 31)
    else:
        next_quarter_end = date(year + 1, 3, 31)

    upcoming = [
        emp for emp in employees
        if (not emp.is_enrolled()) and emp.is_qualified(next_quarter_end)
    ]

    sorted_upcoming = sorted(upcoming, key=lambda emp: emp.employment_date, reverse=True)
    return json.dumps([emp.to_dict() for emp in sorted_upcoming], indent=2)
