#ILoveAdeline
import storage
from storage import load_employees
from storage import save_employees
load_employees()
from employees import add_employee
from employees import show_employees
from employees import search_employee
from employees import delete_employee
from employees import edit_employee

from validation import get_valid_option


def print_header(title):
    print("=======================================")
    print(f"               {title}                ")
    print("=======================================")
while True:
    print("===== Employee Management System =====")
    print("1. Add employee")
    print("2. Show employees")
    print("3. Search employees")
    print("9. Exit")
    print("======================================")
    choice = get_valid_option()
    if choice== 1:add_employee()  
    elif choice== 2:
        if not storage.employees:
                print_header("No employees found")
        else:show_employees()
    elif choice== 3: search_employee()
    elif choice== 9:break
    else:
        print("Invalid option")
        continue