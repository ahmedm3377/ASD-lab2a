import json
from datetime import date, timedelta
from typing import Optional

class PensionPlan:
    def __init__(self, plan_reference_number: str, enrollment_date: date, monthly_contribution: float):
        self.plan_reference_number = plan_reference_number
        self.enrollment_date = enrollment_date
        self.monthly_contribution = monthly_contribution

    def to_dict(self):
        return {
            "planReferenceNumber": self.plan_reference_number,
            "enrollmentDate": self.enrollment_date.isoformat() if self.enrollment_date else None,
            "monthlyContribution": self.monthly_contribution
        }

