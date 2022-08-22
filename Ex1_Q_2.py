import math
class Rectangle:
    def r_Perimeter(self,l,b):
        self.l=l
        self.b=b
        return 2*(l+b)

    def r_Area(self,l,b):
        self.l=l
        self.b=b
        return l*b

class Circle:
    def c_Perimeter(self,r):
        self.r=r
        return 2*math.pi*r

    def c_Area(self,r):
        self.r=r
        return math.pi*r*r

class Triangle:
    def t_Perimeter(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
        return a+b+c

    def t_Area(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        s=(a+b+c)/2
        return math.sqrt(s*(s-a)*(s-b)*(s-c))

r=Rectangle()
c=Circle()
t=Triangle()
ll=int(input("enter length of Rectangle:"))
bb=,int(input("enter breadth of Rectangle:"))
rr=int(input("enter Radius of Circle:"))

print("Area of Rectangle is:",r.r_Area(ll,bb)," perimeter of Rectangle is:",r.r_Perimeter(ll,bb))
print("Area of Circle is:",c.c_Area(rr)," perimeter of Circle is:",c.c_Perimeter(rr))
print(" Area of Triangle is:",t.t_Area(3,4,5)," perimeter of Triangle is:",t.t_Perimeter(3,4,5))