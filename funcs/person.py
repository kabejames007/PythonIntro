class Person:
    def __init__(self, firstname: str, lastname: str, age: int, height: float, race: str, employment_statuses: str)-> None:
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.height = height
        self.race = race
        self.employment_statuses = employment_statuses
        self.is_happy = True

    def describe_yourself(self):
        print(f"Hello, my name is {self.firstname} {self.lastname}. I am {self.age} years old and {self.height} tall. I am {self.race} and I am currently {self.employment_statuses}.")


    def check_happiness(self):
        """"
         Updates happiness based on emplyment status.
        """
        if self.employment_statuses == "unemployed":
            self.is_happy = False
        

