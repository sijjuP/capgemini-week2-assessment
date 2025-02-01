from abc import ABC,abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(IShape):
    def calculate_area(self,l,w):
        return l*w

class Circle(IShape):
    def calculate_area(self,r):
        return 3.14*r**2

# Example usage
l=int(input("Enter length of rectangle:\t"))
w=int(input("Enter width of rectangle:\t"))
rect=Rectangle()
print(f"Area of the rectangle:{rect.calculate_area(l,w)}")

r=float(input("\nEnter radius of circle:\t"))
cir=Circle()
print(f"Area of the circle: {cir.calculate_area(r)}")