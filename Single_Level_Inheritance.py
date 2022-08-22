class Base :
    def baseDisplay(self):
        print("Base Class")

class Derived(Base) :
    def derivedDisplay(self):
        print("Derived Class")

obj=Derived()
obj.baseDisplay()
obj.derivedDisplay()