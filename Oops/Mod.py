class my:
    def __init__(self):
        self.m1()
    def m1(self):
        print("M1")
        self.m2()

    def m2(self):
        print("M2")




class m(my):

    def m3(self):
        print("M3")
        self.m4()
    def m4(self):
        print("M4")




obj=m()
obj.m3()