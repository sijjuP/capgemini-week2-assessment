class Vehicle:
    def __init__(self):
        self.mode="road transport"
        print("\nVehicle object created\n")
    def vehicle_disp(self):
        print("\nmethod in Vehicle\n")


class Car(Vehicle):
    def __init__(self):
        print("\nCar object created\n")
    def car_disp(self):
        self.vehicle_disp()
        print("\nmethod in Car\n")

class Bike(Vehicle):
    def __init__(self):
        print("\nBike object created\n")
    def bike_disp(self):
        self.vehicle_disp()
        print("\nmethod in Bike\n")

class ElectricCar(Car):
    def __init__(self):
        print("\nElectric car object created")
    def electricar_disp(self):
        self.vehicle_disp()
        self.car_disp()
        print("\nmethod in ElectricCar\n")

electric_car=ElectricCar()
electric_car.electricar_disp()

car_obj=Car()
car_obj.vehicle_disp()