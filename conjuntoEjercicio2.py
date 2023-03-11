
""" from datetime import datetime

birthdays = {}

while True:
    birthday = input("\nIngrese un cumpleaños en formato mm/dd/yyyy , o precione enter para salir: ")
    if not birthday:
        break
    name = input("Enter the name for this birthday: ")
    day, month, year = map(int, birthday.split("/"))
    birthdays[(day, month, year)] = name

while True:
    date = input("Ingrese un cumpleaños en formato mm/dd/yyyy , o precione enter para salir: ")
    if not date:
        break
    try:
        month, day, year = map(int, date.split("/"))
        dt = datetime(year, month, day)
        for bday, name in birthdays.items():
            if dt.month == bday[1] and dt.day == bday[0]:
                age = dt.year - bday[2]
                print(f"{name} would be {age} years old on {date}")
                break
        else:
            print("No hay cumpleaños encontrados para esta fecha")
    except ValueError:
        print("Formato de fecha invalida, por favor intentalo de nuevo\n") """

from datetime import datetime

# Function to calculate age based on birthday and a given date
def calculate_age(birthday, date):
    birthdate = datetime.strptime(birthday, '%m/%d/%Y')
    enddate = datetime.strptime(date, '%m/%d/%Y')
    age = enddate.year - birthdate.year - ((enddate.month, enddate.day) < (birthdate.month, birthdate.day))
    return age

# Create an empty dictionary to store birthdays
birthdays = {}

# Ask user for birthdays until they type 'quit'
while True:
    birthday = input("Enter a birthday in mm/dd/yyyy format (or type 'quit' to exit): ")
    if birthday == 'quit':
        break
    name = input("Enter the name for this birthday: ")
    birthdays[birthday] = name

# Ask user for a date to check ages
check_date = input("Enter a date in mm/dd/yyyy format to check ages: ")

# Loop through the dictionary and print the names and ages for each birthday
for birthday in birthdays:
    name = birthdays[birthday]
    age = calculate_age(birthday, check_date)
    print(f"{name} would be {age} years old on {check_date}.")
