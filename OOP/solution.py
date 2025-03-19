# q1: class created with attr
class Car:
    def __init__(self, brand, model, priModel):
        self.brand=brand
        self.model=model
# q4: private attr for model
        self.__priModel=priModel

# q2: method to display full name in class
    def fullName(self):
        return f"{self.brand} {self.model} {self.__priModel}"

# q4: private getter method
    def get_priModel(self):
        return f"{self.__priModel}"

# q3: inherited class from Car class
class ElectricCar(Car):
    def __init__(self, brand, model, priModel, battery_size):
        super().__init__(brand, model, priModel)
        self.battery_size=battery_size

# q1: class instance created
car_q1=Car("Mahindra", "Nano", "Private Nano")
print("Car's brand is:", car_q1.brand)
print("Car's model is:", car_q1.model)
print("Car's private model is:", car_q1.get_priModel())

# q2: method to display full name in class
car_q2=Car("Tata", "Thar", "Private Thar")
print("Your car is:", car_q2.fullName())

# q3: inherited class from Car class
# q4: private attr passed and called
car_q3=ElectricCar("Tesla", "Swift", "Private Swift", "9v")
print (f"EV brand: {car_q3.brand}, Model: {car_q3.model}, Private Model: {car_q3.get_priModel()}, Battery size: {car_q3.battery_size}")
