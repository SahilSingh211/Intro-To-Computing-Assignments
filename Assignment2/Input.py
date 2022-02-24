import string
print()

print("===================================================== ASSIGNMENT 2, 21104050 =====================================================")

print()
print()

print( "   Program-1\nString Operations")
#program-1==>To do Operations on a given input string.
print()

str="Python is a case sensitive language"

print(str)

print()

#For Part a.)
#finding length of string
print("length of string is : ",len(str))
print()

#For part b.)
#reversing the string
print("The string when reversed is :",str[::-1])
print()

#For part c.)
#slicing the string
str1=(str[10:26])

print("The new string is :",str1)
print()

#For part d.)
#replacing words
print("New string is :",str.replace("a case sensitive", "object oriented"))
print()

#For part e.)
#Finding index of "a"
print("Index of a is :",str.find("a"))
print()

#For part f.)
#removing all whitespaces
print("The string is : \"{}\"".format(str.replace(" ", "")))

print()
print()
print("*"*80)
print()

print("    Program-2\nString Formatting")

#Program Used in string formatting.
print()

#take input from the User.
Name=input("Enter Your Name : ")                                                                                                #Name

SID=(input("Enter Your SID : "))                                                                                                #SID

Department_Name=(input("enter your department Name : "))                                                                        #Department Name

CGPA=float(input("Enter your CGPA : "))                                                                                         #CGPA

print("Hey, {0} Here!\nMy SID is {1}\nI am from {2} department and my CGPA is {3}.".format(Name, SID, Department_Name, CGPA))
#final Answer

print()
print()
print("*"*80)
print()

print("    Program-3\nBitwise functions")

#Program to handle all bitwise functions for two numbers
print()

a=56
b=10

#Finding a&b
print("The value of a&b=",a&b)
print()

#Finding a|b
print("The value of a|b=",a|b)
print()

#Finding a^b
print("The value of a^b=",a^b)
print()

#Left shifting both a and b with 2 bits
print("both a and b shifted left by 2 bits =",a<<2,",", b<<2)
print()

#Right shifting a with 2 bits and b with 4 bits.
print("a shifted right by 2 units and b by 4 units =",a>>2,",", b>>4)

print()
print()
print("*"*80)
print()

print("    Program-4\nThe Greatest Number")
#Program to find the greatest number from the three numbers entered by user.

print()

#Input of the three numbers
num1=int(input("enter first number :"))
num2=int(input("enter second number :"))
num3=int(input("enter third number :"))
#num=number

#making list of numbers
List=[num1,num2,num3]

#Printing the Maximum of the three numbers.
print("greatest number in given is :",max(List))

print()

print("*"*80)
print()

print("      Program-5\nFinding word in String")
#Program to find a given word in a user input string

print()
String=(input("enter your sentence :"))

#checking if "name" is in the string.
if "name" in String:
    print("yes")

else:
    print("no")

print()
print()
print("*"*80)
print()

print("Program-6\nTriangle Checker from Side length")
#Program to find whether the three side lengths given by a user can join to form a Triangle

print()

#Entering the length of three Sides

side1=int(input("Enter Length of First Side :"))
side2=int(input("Enter Length of second Side :"))
side3=int(input("Enter Length of Third Side :"))
#side=length of each side

if (side1)>=(side2)+(side3):
    print("No.")

elif (side2)>=(side1)+(side3):
    print("No.")

elif (side3)>=(side1)+(side2):
    print("No.")

else:
    print("Yes.")

print()
print()
print("===================================================== END OF ASSIGNMENT! =====================================================")
