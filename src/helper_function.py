from datetime import date
from src.models.Employee import Employee
from src.models.PensionPlan import PensionPlan
from src.data import employees
import json



def print_all_employees_report():
    """
    Prints a list of all employees in JSON format, sorted by yearly salary (descending)
    and then by last name (ascending).
    """
    sorted_employees = sorted(employees, key=lambda emp: (-emp.yearly_salary, emp.last_name))
    
    employee_dicts = [emp.to_dict() for emp in sorted_employees]

    print(json.dumps(employee_dicts, indent=2))

def print_quarterly_enrollees_report():
    """
    Prints the Quarterly Upcoming Enrollees report in JSON format.
    
    An employee qualifies if they are not enrolled in a pension plan and
    will have been employed for at least 3 years by the last day of the next quarter.
    The list is sorted by employment date in descending order.
    """
    current_date = date.today()
    
    # Calculate the next quarter's start and end dates
    current_month = current_date.month
    if 1 <= current_month <= 3:
        next_quarter_start = date(current_date.year, 4, 1)
        next_quarter_end = date(current_date.year, 6, 30)
    elif 4 <= current_month <= 6:
        next_quarter_start = date(current_date.year, 7, 1)
        next_quarter_end = date(current_date.year, 9, 30)
    elif 7 <= current_month <= 9:
        next_quarter_start = date(current_date.year, 10, 1)
        next_quarter_end = date(current_date.year, 12, 31)
    else:  # 10 <= current_month <= 12
        next_quarter_start = date(current_date.year + 1, 1, 1)
        next_quarter_end = date(current_date.year + 1, 3, 31)

    upcoming_enrollees = []
    for emp in employees:
        # Check if they are not yet enrolled and will qualify by the end of the next quarter
        if not emp.is_enrolled() and (next_quarter_end - emp.employment_date).days / 365.25 >= 3:
            upcoming_enrollees.append(emp)

    # Sort the list by employment date in descending order
    sorted_enrollees = sorted(upcoming_enrollees, key=lambda emp: emp.employment_date, reverse=True)
    
    enrollee_dicts = [emp.to_dict() for emp in sorted_enrollees]
    
    print(json.dumps(enrollee_dicts, indent=2))