class Car:
    def move(self):
        print("Car moves on the road\n")

class Airplane:
    def move(self):
        print("Airplane flies\n")

class FlyingCar(Car,Airplane):
    def move(self):
        print("Can fly and drive\n")
        
fly_car=FlyingCar()
fly_car.move()