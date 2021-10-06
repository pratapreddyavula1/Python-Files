class Student:
    def __init__(self):
        self.__id=124
        self.__name="Pratap"

    def display(self):
        print(self.__id)
        print(self.__name)

c=Student()
print(c._Student__id) #Name Mangling
