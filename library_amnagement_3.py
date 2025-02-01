class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def display_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nisbn: {self.isbn}")        

title=input("\nEnter Book title:\n")
author=input("\nEnter Book author:\n")
isbn=input("\nEnter Book isbn:\n")

book_obj=Book(title,author,isbn)
book_obj.display_details()