import json
def load_employees():
    global employees

    with open("employees.json", "r") as file:
        employees = json.load(file)      
load_employees()
def save_employees():
    with open("Employees.json", "w") as file:
        json.dump(employees , file)
def add_employee():
    while True:
        name = input("Name of employer: ")
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
        elif action== "2":break
def delete_employee():
    delite = int(input("Choose employee for delete:"))
    if 1 <= delite <= len(employees):
        aproved = input(
            f"Are u sure you want to delete {employees[delite - 1]['Name']}? y/n: "
        )
        if aproved.lower()=='y':
            employees.pop(delite -1 )
    else : 
        print('Employee not found') 
    save_employees()
while True:
    print("===== Employee Management System =====")
    print("1. Add employee")
    print("2. Show employees")
    print("9. Exit")
    choice = input("Ur option:")
    if choice== "1":add_employee()  
    if choice== "2":
        if not employees:
                print('')
                print("=======================================")
                print("=== !!!!!! No employees found!!!!!! ===")
                print("============================Try again==")
                print('')
        else:
            show_employees()
    if choice== "9":break
    