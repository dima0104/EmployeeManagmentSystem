import json
def load_employees():
    global employees

    with open("Employees.json", "r") as archive:
        employees = json.load(archive)      
def save_employees():
    with open("Employees.json", "w") as archive:
        json.dump(employees , archive , indent=4)
