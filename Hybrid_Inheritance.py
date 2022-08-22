class Class1 :
    def Class1Display(self):
        print("Class1 Display")

class Class2(Class1) :
    def Class2Display(self):
        print("Class2 Display")

class Class3(Class1):
    def Class3Display(self):
        print("Class3 Disply")

class Class4(Class2,Class3):
    def Class4Display(self):
        print("Class4 Display")

obj=Class4()
obj.Class1Display()
obj.Class2Display()
obj.Class3Display()
obj.Class4Display()