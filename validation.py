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
            option = int(input('Choose an option: '))
            if option in [ 1 , 2 , 3 , 9 ]:
                return option
        except ValueError:
            print("Please enter a number")
            continue
