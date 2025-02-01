class Person:
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
    def display_person(self):
        print(f"\nName: {self.name}\nId: {self.id}\nAge: {self.age}")

class Employee(Person):
    def __init__(self,department,salary,name,id,age):
        super().__init__(name,id,age)
        self.department=department
        self.salary=salary
    def display_employee(self):
        self.display_person()
        print(f"\ndepartment: {self.department}\nsalary: {self.salary}\n")
    

class Manager(Employee):
    def __init__(self,department,salary,name,id,age):
        super().__init__(department,salary,name,id,age)
    def approve_leave(self):
        print("\nLeave approved\n")
        



manager_obj=Manager("Development",30000,"manager1","001","56")
manager_obj.display_employee()
manager_obj.display_person()
manager_obj.approve_leave()