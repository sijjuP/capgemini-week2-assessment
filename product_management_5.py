class Book:
    def __init__(self,name,price,stock):
        self.name=name
        self.price=price
        self.stock=stock

    def check_availability(self,quantity):
        return True if(self.stock>quantity) else False
        
name=input("\nEnter product name:\n")
price=float(input("\nEnter product price in INR:\n"))
stock=int(input("\nEnter product stock:\n"))

book_obj=Book(name,price,stock)

input=int(input("\nEnter quantity required:\t"))
if(book_obj.check_availability(input)):
    print("Stock avalilabele")
else:
    print("Stock not avalilabele")