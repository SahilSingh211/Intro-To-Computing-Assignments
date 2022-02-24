class Student:
    def __init__(self,Name,Roll):
        self.Name=Name
        self.Roll=Roll
a=input("Enter Your Name :")
b=int(input("Enter your SID :"))
s1=Student(a,b)
print(s1.Name,s1.Roll)
del s1
