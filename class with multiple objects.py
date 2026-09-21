class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def read(self):
        print(self.name)
        print(self.age)
s1=student("Lahari",18)
s1.read()
s2=student("Bhavani",20)
s2.read()