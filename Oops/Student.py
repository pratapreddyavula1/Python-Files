from Human import human
class Student(human):
    def  StudntDetails(self):
        self.input()
        self.sname=input("Enter Student name:")
        self.sid=int(input("Enter  Student Id:"))
        self.cls=input("Enter Student Class:")
        self.maths=int(input("Enter Maths Marks:"))
        self.social = int(input("Enter  Social Marks:"))
        self.hindi = int(input("Enter Hindi Marks:"))
        self.english=int(input("Enter English Marks:"))
        self.Total()
    def Total(self):
        self.total=self.maths+self.social+self.hindi+self.english
        self.avgs=self.total/4
        self.Grade="A+" if self.avgs>=90 else"A" if (self.avgs<90 and self.avgs>=75) else "B" if (self.avgs<75 and self.avgs>=45) else"c" if self.avgs>=35 else"F"
        self.display()
    def display(self):
        print("**********************************")
        print("Student Name:",self.sname)
        print()
        print("Student Id:",self.sid)
        print()
        print("Student Class:",self.cls)
        print()
        print("Student Total:",self.total)
        print()
        print("Student Average:",self.avgs)
        print()
        print("Student Grade:",self.Grade)






