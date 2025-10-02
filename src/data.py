# Create the in-memory data store
from datetime import date
from src.models.Employee import Employee
from src.models.PensionPlan import PensionPlan


employees = [
    Employee(
        employee_id=1,
        first_name="Daniel",
        last_name="Agar",
        yearly_salary=105945.50,
        employment_date=date(2023, 1, 17),
        pension_plan=PensionPlan(
            plan_reference_number="EX1089",
            enrollment_date=date(2023, 1, 17),
            monthly_contribution=100.00
        )
    ),
    Employee(
        employee_id=2,
        first_name="Bernard",
        last_name="Shaw",
        yearly_salary=197750.00,
        employment_date=date(2022, 9, 3),
        pension_plan=PensionPlan(
            plan_reference_number="SM2307",
            enrollment_date=date(2025, 9, 3),
            monthly_contribution=1555.50
        )
    ),
    Employee(
        employee_id=3,
        first_name="Carly",
        last_name="Agar",
        yearly_salary=842000.75,
        employment_date=date(2014, 5, 16),
        pension_plan=PensionPlan(
            plan_reference_number="SM2307",
            enrollment_date=date(2017, 5, 17),
            monthly_contribution=1555.50
        )
    ),
    Employee(
        employee_id=4,
        first_name="Wesley",
        last_name="Schneider",
        yearly_salary=74500.00,
        employment_date=date(2023, 7, 21),
        pension_plan=None
    ),
    Employee(
        employee_id=5,
        first_name="Anna",
        last_name="Wiltord",
        yearly_salary=85750.00,
        employment_date=date(2023, 3, 15),
        pension_plan=None
    ),
    Employee(
        employee_id=6,
        first_name="Yosef",
        last_name="Tesfalem",
        yearly_salary=100000.00,
        employment_date=date(2024, 10, 31),
        pension_plan=None
    )
]


def load_sample_data():
    """Return a list of Employee objects (in-memory dataset)."""
    return employees