from Student import Student
from Employee import Employee
class Choice(Student,Employee):
    def choice(self):
        ch=input(("Enter Which File do you want to Open (Student/Employee):"))
        if ch.lower()=="student":
            self.StudntDetails()
        elif ch.lower()=="employee":
            self.EmployeeDetails()
        else:
            print("No Such Files")

obj=Choice()
obj.choice()