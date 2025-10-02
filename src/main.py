"""Interactive CLI wrapper that calls the project report functions.

This file is intentionally robust about imports so it works when run as
``python -m src.main`` or ``python src/main.py`` from the project root.
"""
from __future__ import annotations
from datetime import date
import sys
from pathlib import Path

# Ensure project root is on sys.path so `import src...` works when running
# this file directly (python src/main.py). Project root is the parent of src/.
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

try:
    # prefer package imports: python -m src.main or when project root is on sys.path
    from src.data import load_sample_data
    from src.reports import employees_json, quarterly_upcoming_enrollees
except Exception:
    # As a last resort try local imports (when running with src as working dir)
    try:
        from data import load_sample_data
        from reports import employees_json, quarterly_upcoming_enrollees
    except Exception:
        print('Failed to import project modules using package imports. Run from project root using: python -m src.main')
        raise


def print_all_employees_report() -> None:
    employees = load_sample_data()
    print(employees_json(employees))


def print_quarterly_enrollees_report(as_of: date | None = None) -> None:
    employees = load_sample_data()
    as_of = as_of or date.today()
    print(quarterly_upcoming_enrollees(employees, as_of=as_of))


def main() -> None:
    print("Welcome to the Employee Pension Plans CLI App!")
    while True:
        print("\nChoose an option:")
        print("1. Print all Employees report")
        print("2. Print Quarterly Upcoming Enrollees report")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\n--- All Employees Report ---")
            print_all_employees_report()
            print("----------------------------\n")
        elif choice == '2':
            print("\n--- Quarterly Upcoming Enrollees Report ---")
            print_quarterly_enrollees_report()
            print("-------------------------------------------\n")
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()