import json
from datetime import date, timedelta
from typing import Optional
from src.models.PensionPlan import PensionPlan

class Employee:
    def __init__(self, employee_id: int, first_name: str, last_name: str, yearly_salary: float, employment_date: date, pension_plan: Optional[PensionPlan] = None):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.yearly_salary = yearly_salary
        self.employment_date = employment_date
        self.pension_plan = pension_plan

    def is_qualified(self, current_date: date) -> bool:
        """
        Checks if an employee has been employed for at least 3 years.
        """
        years_employed = (current_date - self.employment_date).days / 365.25
        return years_employed >= 3

    def is_enrolled(self) -> bool:
        """
        Checks if an employee is already enrolled in a pension plan.
        """
        return self.pension_plan is not None

    def to_dict(self):
        return {
            "employeeId": self.employee_id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "yearlySalary": self.yearly_salary,
            "employmentDate": self.employment_date.isoformat(),
            "pensionPlan": self.pension_plan.to_dict() if self.pension_plan else None
        }