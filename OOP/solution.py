# q1: class created with attr
class Car:

    def __init__(self, brand, model):
        self.brand=brand
        self.model=model

# q2: method to display full name in class
    def fullName(self):
        return f"{self.brand} {self.model}"

# q3: inherited class from Car class
class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size=battery_size

# q1: class instance created
car_q1=Car("Mahindra", "Nano")
print("Car's brand is:", car_q1.brand)
print("Car's model is:", car_q1.model)

# q2: method to display full name in class
car_q2=Car("Tata", "Thar")
print("Your car is", car_q2.fullName())

# q3: inherited class from Car class
car_q3=ElectricCar("Tesla", "Swift", "9v")
print (f"EV brand is {car_q3.brand} and model is {car_q3.model} with {car_q3.battery_size} battery")