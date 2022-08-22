class Base1 :
    def Base1Display(self):
        print("Base1 Display")

class Base2 :
    def Base2Display(self):
        print("Base2 Display")

class Derived(Base1,Base2) :
    def DerivedDisplay(self):
        print("Derived Display")

obj=Derived()
obj.Base1Display()
obj.Base2Display()
obj.DerivedDisplay()