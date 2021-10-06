from Human import human
class Employee(human):
    def EmployeeDetails(self):
        self.input()
        self.ename=input("Enter Employee Name:")
        self.eid=int(input("Enter Employee Id:"))
        self.desg=input("Enter Employee Designation:")
        self.sal=int(input("Enter Employee Salary:"))
        self.exp=int(input("Enter Employee Experience:"))
        self.Hike()
    def Hike(self):
        a=self.desg
        b=self.sal
        c=self.exp
        if c>10:
            if a.lower()=="pm":
                hike=0.1
                HikeSalary=b+(b*hike)
            elif a.lower()=="tm":
                hike=0.2
                HikeSalary=b+(b*hike)
            elif a.lower() == "manager":
                hike = 0.3
                HikeSalary = b + (b * hike)

            elif a.lower()=="dev":
                hike=0.5
                HikeSalary=b+(b*hike)

            else:
                hike=0.04
                HikeSalary=b+(b*hike)
        if c>=5 and c<10:
            if a.lower()=="pm":
                hike=0.01
                HikeSalary=b+(b*hike)
            elif a.lower()=="tm":
                hike=0.02
                HikeSalary=b+(b*hike)
            elif a.lower() == "manager":
                hike = 0.03
                HikeSalary = b + (b * hike)

            elif a.lower()=="dev":
                hike=0.05
                HikeSalary=b+(b*hike)

            else:
                hike=0.04
                HikeSalary=b+(b*hike)
        else:
            print("Not Eligible For the Hike...Sorry")
        self.hike=str(hike*100)+"%"
        self.TotalHike=HikeSalary
        self.display1()

    def display1(self):
        print("******************")
        print("Employee Name:",self.ename)
        print()
        print("Enter Employee ID:",self.eid)
        print()
        print("Employee Designation:",self.desg)
        print()
        print("Employee Experience:", self.exp)
        print()
        print("Employee Salary:",self.sal)
        print()
        print("Employee Hike:",self.hike)
        print()
        print("Employee  Total Hiked Salary:",self.TotalHike)



