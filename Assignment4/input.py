print("~"*30,"Assignment 4","~"*30)
print()

print("Program 1\nTower of Hanoi")
print()

# Program to solve the problem for Tower of Hanoi.

# Defining a function for movement of rods in Tower of Hanoi.
def TowerOfHanoi(n: int, Starting: str, Target: str, Assistant: str):
    # Starting with first disk.
    if n == 1:
        print("Move disk 1 from {0} rod to {1} rod".format(Starting, Target))

        return
    # Recursive approach for nth disk.

    TowerOfHanoi(n - 1, Starting, Assistant, Target)
    print("Move disk {0} from {1} rod to {2} rod".format(n, Starting, Target))
    TowerOfHanoi(n - 1, Assistant, Target, Starting)


Disk_num = 3

Entry = "Start"  # Starting Rod
Exit = input("Enter the Name of Rod where you want them to be, T for Targeted, A for Assistant :")
Exit = Exit.upper().strip()
print()

if Exit == "T":
    Exit = "Target"
    Helper = "Assistant"

elif Exit == "A":
    Exit = "Assistant"
    Helper = "Target"

else:
    print("Wrong Rod Chosen")
    exit()

TowerOfHanoi(Disk_num, Entry, Exit, Helper)
print()

print("All of the disks have been moved from {} rod to {} rod".format(Entry, Exit))

print()
print("_."*30)
print()

print("Program 2\nPascal's Triangle")
# Program To create Pascal's Triangle by both Recursive and Iterative way.

print()


# Defining a function for factorial of number using recursion.

def Fac(Number):
    if Number == 0:
        return 1
    else:
        b = (Number * Fac(Number - 1))
    return b


# Asking user to input Number of rows for Pascal Triangle.
num = int(input("Enter the number of rows you want :"))
print()
list1 = []
# Building numbers for Pascal Triangle.
for n in range(0, num):
    L = []
    for i in range(n + 1):
        L.append(str(int(Fac(n)) // (int(Fac(n - i)) * (int(Fac(i))))))
    list1.append(L)

# making the Triangle.

print("The Pascal's Triangle by Recursive method is as follows :")
print()

for i in range(num):
    print("    " * (num - i), end="")
    for j in range(0, i + 1):
        print('{0:6}'.format(list1[i][j]), end=" ")
    print()
print()

# Making Pascal's Triangle the Iterative way.

Tri_List = []
# An empty list

for i in range(num):
    Tri_List.append([])
    Tri_List[i].append(1)

    # Above lines make nested list of same number as input.

    for j in range(1, i):
        Tri_List[i].append(Tri_List[i - 1][j - 1] + Tri_List[i - 1][j])

    if num != 0:
        Tri_List[i].append(1)

print("The Pascal's Triangle made in Iterative Format is :")
print()

for i in range(num):
    print("    " * (num - i), end=" ")

    for j in range(0, i + 1):
        print('{0:6}'.format(Tri_List[i][j]), end=" ")

    print()

print()
print("_."*30)
print()

print("Program 3\nBuilt-in Functions")
# Programs to find quotient, remainder and use in-built Function.
print()

# Asking User to input Numbers.
num1 = int(input("Enter first number :"))
num2 = int(input("Enter Second number :"))
print()

# Using Div-mod function for Quotient and remainder.
Quotient_Remainder = (divmod(num1, num2))

# Lists to use in future parts of Question.
List2 = []
print("The quotient and Remainder are as follows :", Quotient_Remainder)

List1 = list(Quotient_Remainder)
List3 = list(Quotient_Remainder)
# part a.
print("Part(a)\nThe statement that the function is Callable is", callable(divmod))
print("The statement that the function with values is Callable is", callable(divmod(num1, num2)))
print()

# Part B, Counting zeroes in L.
print("Part(b)")

print("The statement that all values are non-Zero is :", all(List1))
print()

# part c, Printing numbers greater than 4.
for j in [4, 5, 6]:
    List1.append(j)

List1.sort()
List_of_num = filter((5).__le__,List1)

Set_of_num = set(List_of_num ) 
print("Part(c)\nSet of numbers greater than 4 is :", Set_of_num)

Froze_Set = frozenset(Set_of_num)

# part d.
print("Part(d)\nThe immutable set is :", Froze_Set)
print()

# part e.
print("Part(e)\nMaximum Value in the set is :", max(Froze_Set))
print()

# Part f.
print("Part(f)\nHash of max value is :", hash(max(Froze_Set)))

print()
print("_."*30)
print()

print("Program 4\nStudent's Records creator")
# Program for creating and deleting a student's record.
print()


# Creating a Class for student's Records.
class Student:
    def __init__(self, Name: str, Roll: int):
        self.name = Name
        self.roll = Roll
        print("Created Record for", self.name)

    def __del__(self):
        print("Destroyed the record of", self.name)


print()

# Taking input from user.
Name_ = input("Enter Name of Student :").capitalize()
SID = int(input("Enter {}'s SID :".format(Name_)))

S1 = Student(Name_, SID)
print()

print("Student's Name is {0}, and Roll number is {1}.".format(Name_, SID))

print("Destroyed the record of", S1.name)


print()
print("_."*30)
print()

print("Program 5\nEmployee name salary Records")
print()

# Creating a class for Employees.

class Employee:
    def __init__(self, name: str, salary: int):
        self.name = name  # Name of Employee
        self.salary = salary  # Salary of Employee


# Creating Records for Employees.
E1 = Employee("Mehak", 40000)
E2 = Employee("Ashok", 50000)
E3 = Employee("Viren", 60000)

# Making a Table for Employees and their respective salaries.
print(
    "| Employee   <==>   Salary   |\n|   {}    <==>    {}   |\n|   {}    <==>    {}   |\n|   {}    <==>    {}   |".format(
        E1.name, E1.salary,
        E2.name, E2.salary,
        E3.name, E3.salary))

print()
# part(a)
E1.salary = 70000
print("The salary of {} is updated to {}".format(E1.name, E1.salary))
print()

# part(b)
print("{0}'s Record is deleted".format(E3.name))
del E3

print()
print("_."*30)
print()

print("Program 6\nFriendship Checker")
print()

# Taking input for both George's and Barbie's word
George = input("Enter George's Word :")
Barbie = input("Enter Barbie's Word :")
George=George.strip().lower()
Barbie=Barbie.strip().lower()

# Making a list of all alphabets in both words and sorting them.
G = list(George)
B = list(Barbie)
print()

G.sort()
B.sort()

if G==[] or B==[]:
    print("Word Given is invalid")
    exit()
else:
    print(f"George and Barbie have {G==B} friendship.")
print()

print("~"*30,"End Of Assignment","~"*30)
