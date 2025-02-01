class Employee:
    def __init__(self,name,id,department):
        self.name=name
        self.id=id
        self.department=department

name=input("\nEnter Employee name:\n")
id=input("\nEnter Employee id:\n")
department=input("\nEnter Employee department:\n")

employee_obj=Employee(name,id,department)
print(f"\nEmployee object details:\nname: {employee_obj.name}\nid: {employee_obj.id}\ndepartment: {employee_obj.department}")
