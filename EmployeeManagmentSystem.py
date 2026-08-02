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
    while True:
        name = input("Name of employee: ")
        if not name:
            print("Name can't be empty")
            continue
        if name[0].isupper():
            if name.isalpha():
                break
            print("Please enter letters")
            
        else:
            print("First letter must be uppercase")
    while True:
        age = input("Type age:")
        try:
            age = int(age)
            if age > 100 or age < 17:
                print('Type real age!')
            else:
                break
        except ValueError:
            print("Please enter a number")
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
            print("===== EMPLOYEES =====")
            for index, employee in enumerate(employees, start=1):
                print(f"{index}. Name: {employee['Name']} | Age: {employee['Age']}")
            print("=====================")
            print("1. Delete employee")
            print("2. Exit")
        action = input('Ur option:')
        if action== "1":
            delete_employee()
        elif action== "2":
            break
        else: 
            print("Invalid option")
            continue
def delete_employee():
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
    else : 
        print('Employee not found') 
    save_employees()
def search_employee():
    search_by_name = input("Type name : ")
    for employee in employees :
        if search_by_name.lower() in employee["Name"].lower() :
            print(f" Name: {employee['Name']} | Age: {employee['Age']}")
while True:
    print("===== Employee Management System =====")
    print("1. Add employee")
    print("2. Show employees")
    print("3. Search employees")
    print("9. Exit")
    choice = input("Ur option:")
    if choice== "1":
        add_employee()  
    elif choice== "2":
        if not employees:
                print('')
                print("=======================================")
                print("=== !!!!!! No employees found!!!!!! ===")
                print("============================Try again==")
                print('')
        else:
            show_employees()
    elif choice== "3": 
        search_employee()
    elif choice== "9":
        break
    else: 
        print("Invalid option")
        continue
