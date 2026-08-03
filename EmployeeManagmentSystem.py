#ILoveAdeline

import json
def load_employees():
    global employees

    with open("Employees.json", "r") as archive:
        employees = json.load(archive)      
load_employees()
def save_employees():
    with open("Employees.json", "w") as archive:
        json.dump(employees , archive , indent=4)
def add_employee():
    name = get_valid_name()
    age = get_valid_age()
    employee = {
        "Name": name,
        "Age": age
    }
    employees.append(employee)
    save_employees()
def show_employees():
    while True:
        if not employees:
            print('')
            print("=======================================")
            print("=== !!!!!! No employees found!!!!!! ===")
            print("=======================================")
            print('')           
            print("2. Exit")
        else:
            print("============== EMPLOYEES ==============")
            for index, employee in enumerate(employees, start=1):
                print(f"{index}. Name: {employee['Name']} | Age: {employee['Age']}")
            print("=======================================")
            print("1. Delete employee")
            print("2. Exit")
            print("3. Edit employee")
            print("=======================================")
            print("Choose an option:")
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
        if 1 <= choice_delete <= len(employees):
            aproved = input(
                f"Are u sure you want to delete {employees[choice_delete - 1]['Name']}? y/n: "
            )
            if aproved.lower()=='y':
                employees.pop(choice_delete -1 )
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
        for employee in employees :
            if search_by_name in employee["Name"]:
                print("===== Search Result =====")
                print(f" Name: {employee['Name']} | Age: {employee['Age']}")
                print("==========================")
        if not any(search_by_name in employee["Name"] for employee in employees):
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
def get_valid_name():
    while True:
        name = input("Enter employee name: ")
        if not name:
            print("Name can't be empty")
            continue
        if name[0].isupper() and name.isalpha():
            return name
        print("First letter must be uppercase and name must contain only letters.")
def get_valid_age():
    while True:
        age = input("Enter employee age: ")
        try:
            age = int(age)
            if 17 <= age <= 100:
                return age
            print("Age must be between 17 and 100.")
        except ValueError:
            print("Please enter a valid number for age.")
def get_valid_option():
    while True:
        try:
            option = int(input())
            if option in [ 1 , 2 , 3 , 9 ]:
                return option
        except ValueError:
            print("Please enter a number")
            continue
def edit_employee():
    print("Choose employee for edit:")
    choice_edit = get_valid_option()
    if 1 <= choice_edit <= len(employees):
        employee = employees[choice_edit - 1]
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
while True:
    print("===== Employee Management System =====")
    print("1. Add employee")
    print("2. Show employees")
    print("3. Search employees")
    print("9. Exit")
    print("======================================")
    print("Choose an option:")
    choice = get_valid_option()
    if choice== 1:add_employee()  
    elif choice== 2:
        if not employees:
                print('')
                print("=======================================")
                print("=== !!!!!! No employees found!!!!!! ===")
                print("============================Try again==")
                print('')
        else:show_employees()
    elif choice== 3: search_employee()
    elif choice== 9:break
    else:
        print("Invalid option")
        continue
