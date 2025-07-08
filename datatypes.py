
from funcs.my_module import cube_number, greet
from funcs.my_classes import Car
from funcs.person import Person



my_first_number = 42
print(my_first_number)

my_first_string = "Hello World!"
print(my_first_string)

print(f"my first number was {my_first_number} and my first string was {my_first_string}")

my_list_var = [1,76,9,3,17,0,3]
print(my_list_var[0])

car_one = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Silver",
    "mileage": 35000,
    "vin": "1HGCM82633A004352",
    "owner": "John Doe",
    "registered": True,
    "previous_owners": ["Alice Smith", "Bob Johnson"],
    "service_records": [
        {"date": "2023-01-10", "service": "Oil Change"},
        {"date": "2023-06-15", "service": "Brake Inspection"},
        {"date": "2024-02-20", "service": "Tire Replacement"}
    ],
    "accident_history": None
}

car_two = {
    "make": "Honda",
    "model": "Accord",
    "year": 2018,
    "color": "Black",
    "mileage": 58000,
    "vin": "2HGFB2F59FH000123",
    "owner": "Jane Smith",
    "registered": True,
    "previous_owners": ["Tom Blake"],
    "service_records": [
        {"date": "2022-09-12", "service": "Battery Replacement"},
        {"date": "2023-03-30", "service": "Engine Tune-Up"}
    ],
    "accident_history": [
        {
            "date": "2021-07-04",
            "description": "Rear-ended at traffic light",
            "damage": "Rear bumper and trunk damage",
            "repaired": True
        }
    ]
}

car_station =[car_one, car_two]

#print(car_station[1]["make"])

#for car in car_station:
print(car_station[1]["make"])
print(car_station[1]["accident_history"][0]["damage"])

n = 100
if n < 50:
    print("n is less than 50")
elif n == 50:
    print("n is equal 50")
else:
    print("n is greater than 50")


if any(car["make"] == "Tesla" for car in car_station):
    print("Tesla found")
else:
    print("no Tesla in the list")


print(cube_number(3))
print(greet("John"))


my_car = Car("Tesla", "Model S", 2022, 79999.99, ["Autopilot", "Electric", "All-Wheel Drive"],"Red")
print(my_car.condition)

person_one = Person("John", "Walker", 25, 5.7, "Black", "Employed")
person_two = Person("Kalisa", "Fabrice", 42, 6.0, "White", "Unemployed")

person_one.describe_yourself()

print(f"{person_one.firstname} is happy: {person_one.check_happiness()}") 
print(f"{person_two.firstname} is happy: {person_two.check_happiness()}") 