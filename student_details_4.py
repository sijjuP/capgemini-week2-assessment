class Student:
    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def get_student_details(self):
        return {"name":self.name,"roll no":self.roll_no}

name=input("\nEnter Student name:\n")
roll_no=input("\nEnter Student roll_no:\n")

student_obj=Student(name,roll_no)
print(student_obj.get_student_details())