class Car:

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def display_car_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

    
    def drive(self, miles):
        self.odometer_reading += miles
        print(f"You drove {miles} miles. Total miles: {self.odometer_reading}")