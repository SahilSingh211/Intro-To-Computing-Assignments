#Q.1#
print()
number1=float(input("enter first number: "))
#It will represent the first number

number2=float(input("enter second number: "))
#It will represent the second number

number3=float(input("enter third number: "))
#It will represent the third number

sum=number1+number2+number3
#sum is the sum of all numbers

print(sum/3)
#this will give the answer

#Q.2
A=int(input("enter your Gross Income: "))
#here A is the gross income of a person

S=10000
#here S is the standard deduction all taxpayers are allowed

D=int(input("mention number of dependents: "))
#D is the number of dependents of taxpayer

d=3000
#d is deduction introduced with each dependent
P=d*D

#P is amount of tax deducted due to dependents

t=(A-10000-P)
#t is taxable income

T=(t*20/100)
#T is total Tax to be paid by taxpayer

print(T)

#Q.3
a=int(input("Enter your Student ID: "))
#a is the SID of student

b=str(input("Enter your Name: "))
#b is the name of student

c=str(input("Enter your gender, M for Male, F for Female, U for Unknown: "))
#c is for gender of student

d=str(input("Enter your Course Name: "))
#d is for course Name

e=float(input("Enter your CGPA: "))
#e is for CGPA of the student

p=(a, b, c, d, e)
#p is the set having all the information

L=list(p)
#L is the list of the elements in t

print(L)

#Q.4
print("enter marks of 5 students")
#It wil print the first line as "enter marks of 5 students"

A=int(input())
B=int(input())
C=int(input())
D=int(input())
E=int(input())
#A, B, C, D, E all will be input of marks obtained by students

t=(A,B,C,D,E)
#t is the set of all marks obtained by students

L=list(t)
#L is the list of elements in set t

list.sort
#this command sorts the numbers in list in increasing order

print(L)

#Q.5
color=['red', 'green', 'white', 'black', 'pink', 'yellow']
print(color)

#-----------PART A-----------#
color.pop(4)
#pop command rmoves that color
print("answer for part a is: ",color)

#----------PART B------------#
color=['red', 'green', 'white', 'black', 'pink', 'yellow']
color[3:5]=['purple']
print("answer for part b is: ",color)


