from abc import ABC,abstractmethod

class ICalculator(ABC):
    @abstractmethod
    def add(self,a,b):
        pass

    @abstractmethod
    def subtract(self,a,b):
        pass

    @abstractmethod
    def multiply(self,a,b):
        pass

    @abstractmethod
    def divide(self,a,b):
        pass

class BasicCalculator(ICalculator):
    def add(self,a,b):
        return a+b

    def subtract(self,a,b):
        return a-b

    def multiply(self,a,b):
        return a*b

    def divide(self,a,b):
        if b==0:
            return "Division by zero is not allowed"
        return a/b

calc=BasicCalculator()
a=int(input("Enter first number:\t"))
b=int(input("Enter second number:\t"))

print(f"Addition: {calc.add(a, b)}")
print(f"Subtraction: {calc.subtract(a, b)}")
print(f"Multiplication: {calc.multiply(a, b)}")
print(f"Division: {calc.divide(a, b)}")