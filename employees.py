import storage

from storage import load_employees
from storage import save_employees

from validation import get_valid_name
from validation import get_valid_age
from validation import get_valid_option

def add_employee():
    name = get_valid_name()
    age = get_valid_age()
    employee = {
        "Name": name,
        "Age": age
    }
    storage.employees.append(employee)
    save_employees()
def show_employees():
    while True:
        if not storage.employees:
            print('')
            print("=======================================")
            print("=== !!!!!! No employees found!!!!!! ===")
            print("=======================================")
            print('')           
            print("2. Exit")
        else:
            print("============== EMPLOYEES ==============")
            for index, employee in enumerate(storage.employees, start=1):
                print(f"{index}. Name: {employee['Name']} | Age: {employee['Age']}")
            print("=======================================")
            print("1. Delete employee")
            print("2. Exit")
            print("3. Edit employee")
            print("=======================================")
        action = get_valid_option()
        if action== 1 :delete_employee()
        elif action== 2 :break
        elif action== 3 :edit_employee()
def delete_employee():
    while True:
        choice_delete = input("Choose employee for delete:")
        try:
            choice_delete =int(choice_delete)
        except ValueError:
            print("Please enter a number")
        if 1 <= choice_delete <= len(storage.employees):
            aproved = input(
                f"Are u sure you want to delete {storage.employees[choice_delete - 1]['Name']}? y/n: "
            )
            if aproved.lower()=='y':
                storage.employees.pop(choice_delete -1 )
                break
            else:
                print("Deletion canceled.")
                break
        else : 
            print("=======================================")
            print('=== !!!!!! Employee not found!!!!!! ===')
            print("=======================================")
            break
    save_employees()
def search_employee():
    while True :
        search_by_name = get_valid_name()
        for employee in storage.employees :
            if search_by_name in employee["Name"]:
                print("===== Search Result =====")
                print(f" Name: {employee['Name']} | Age: {employee['Age']}")
                print("==========================")
        if not any(search_by_name in employee["Name"] for employee in storage.employees):
            print("===== Search Result =====")
            print("=== !!!!!! No employees found!!!!!! ===")
            print("============================Try again==")
        print("1. Search again")
        print("2. Exit")
        print("==========================")
        print("Choose an option:")
        option = get_valid_option()
        if option== 1:
            search_employee()
        elif option== 2:
            break        
def edit_employee():
    print("Choose employee for edit:")
    choice_edit = get_valid_option()
    if 1 <= choice_edit <= len(storage.employees):
        employee = storage.employees[choice_edit - 1]
        while True:
            new_name = input("Enter employee name: ")
            if not new_name:
                print("We dont edit name")
                break
            if new_name[0].isupper() and new_name.isalpha():
                employee['Name'] = new_name
                break
            else:
                print("First letter must be uppercase and name must contain only letters.")
        while True:
            new_age = input("Enter employee age: ")
            if not new_age:
                print("We dont edit age")
                break
            try:
                new_age = int(new_age)
                if 17 <= new_age <= 100:
                    employee['Age'] = new_age
                    break
                else:
                    print("Age must be between 17 and 100.")
            except ValueError:
                print("Please enter a valid number for age.")
            save_employees()
    else:
        print('Employee not found')
    save_employees()
