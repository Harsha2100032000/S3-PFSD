class Class1 :
    def class1Display(self):
        print("Class1 Display")

class Class2(Class1) :
    def class2Display(self):
        print("Class2 Display")

class Class3(Class2) :
    def class3Display(self):
        print("Class3 Display")

obj=Class3()
obj.class1Display()
obj.class2Display()
obj.class3Display()