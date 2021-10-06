class A :
    def a1(self):
        print("A - A1")
    def a2(self):
        print("A2")

class B(A):
    print("dsf")
    def b1(self):
        print("B1")

    def b2(self):
        print("B2")

    def a1(self):
        print("B - A1")

class C(B) :
    def c1(self):
        print("C1")
        self.c2()
    def c2(self):
        print("C2")
        self.a1()

    def a1(self):
        print("C - A1")
        self.b1()


obj=C()
obj.c1()

