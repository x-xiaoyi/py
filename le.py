class student:
    def __init__(self,a,b,c):
        self.name=a
        self.age=b
        self.grad=c
    def display_inf0(self):
        print("name",self.name)
        print("age",self.age)
        print("grad",self.grad)
    def upgrade_age(self,d):
        self.age=d
        print("new age is:",self.age)