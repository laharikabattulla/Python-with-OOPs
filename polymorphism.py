class shape:
    def area(self):
        print("area of shape")
class circle:
    def area(self):
        r=6
        print("circle area:",3.14*r*r)
class rectangle:
    def area(self):
        l=2
        b=3
        print("rectangle area:",l*b)
class triangle:
    def area(self):
        B=5
        H=9
        print("triangle area:",0.5*B*H)
c=circle()
r=rectangle()
t=triangle()

c.area()
r.area()
t.area()