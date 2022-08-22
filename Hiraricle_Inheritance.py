class Base :
    def BaseDisplay(self):
        print("Base Display")

class Derived1(Base) :
    def Derived1Display(self):
        print("Derived1 Display")

class Derived2(Base):
    def Derived2Display(self):
        print("Derived2 Disply")

obj1=Derived1()
obj2=Derived2()
obj1.BaseDisplay()
obj1.Derived1Display()
obj2.Derived2Display()