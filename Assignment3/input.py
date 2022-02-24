print("="*80)

print("Program 1\nCharacter/Word Counter")

String = input("Enter your String :")
#Asking user to enter a string

String = String.lower().rstrip().lstrip()
#Removing all right and left whitespaces and lowering all characters

List_of_numbers = []

#applying condition in String
if " " not in String:

    for char in String: 
        Alphabet = (char, String.count(char))
        List_of_numbers.append(Alphabet)
    
    #Changing List to set
    sett = set(List_of_numbers)
    List0 = list(sett)
    List0.sort()

    for (Character, Occurence) in List0:
        print("The Occurence of", Character, "is", Occurence)
#prints the occurences of all alphabets in a string if string is one word.

else:
    String_list = String.split()

    for character in String_list:
        Word = (character, String_list.count(character))
        List_of_numbers.append(Word)

    sett = set(List_of_numbers)
    List0 = list(sett)
    List0.sort()

    for (Character, Occurence) in List0:
        print("Occurence of Character ",Character, "is ==>", Occurence)

#prints occurence of all words in a string if string is multiword.

print("="*80)

print("Program 2\nNext Date Finder")
Date = int(input("Enter a Date :"))
Month = int(input("Enter a Month :"))
Year = int(input("Enter a Year :"))
n_day=0
n_month=0
n_year=0
def next_date(a,b,c):
    return("{0}/{1}/{2}".format(a,b,c))

def Leap_year(Bin):
    if Bin % 4 == 0:
        if Bin % 100 == 0:
            if Bin % 400 == 0:
                Leap==True
            else:
                Leap=False
        else:
            Leap=True
    else:
        Leap=False
        


    
if Date >= 32 or Date <= 0 or Month <= 0 or Month >= 13 or Year <= 1800 or Year >= 2500:
    print("Wrong Date Given")

elif Month in (1, 3, 5, 7, 10):

    if Date == 31:
        n_day = 1
        n_month = Month+1
        n_year = Year

    else:
        n_day = Date+1
        n_month = Month
        n_year = Year

elif Month in (4, 6, 8, 9, 11):

    if Date == 30:
        n_day = 1
        n_month = Month+1
        n_year = Year

    else:
        n_day = Date+1
        n_month = Month
        n_year = Year

elif Month == 12:

    if Date == 31:
        n_day = 1
        n_month = 1
        n_year = Year+1

    else:
        n_day = Date+1
        n_month = Month
        n_year = Year

elif Month == 2:

    if Leap_year(Year):

        if Date>=30:
            print("Invalid Date Given")

        elif Date==29:
            n_day=1
            n_month=Month+1
            n_year=Year

        else:
            n_day=Date+1
            n_month=Month
            n_year=Year

    else:

        if Date>=29:
            print("Invalid Date Given")

        elif Date==28:
            n_day=1
            n_month=Month+1
            n_year=Year
            
        else:
            n_day=Date+1
            n_month=Month
            n_year=Year
else:
    print("No Such date")       
    
if n_day == 0 or n_month == 0 or n_year == 0:
    exit()           
        
print("The next date is",next_date(n_day, n_month, n_year))

print("="*80)

print("Program 3\nNumber Square tuple Pair Creator")

#Asking User to enter the numbers with spaces between them.
nums = input("Enter your numbers with space between them :")

List_of_numbers = nums.split()
Result_list = []

for i in List_of_numbers:
    Result_list.append((int(i), int(i)**2))

print(Result_list)
print("="*80)
    
print("Program 4\nGrade and Performance marker")

#Making Dictionary of grades and performance
Gradelist = {'A+': "Outstanding", 'A': "Excellent", 'B+': 'Very Good', 'B': 'Good', 'C+': 'Average', 'C': 'Below Average', 'D': 'Poor'}


def marks (a, b):
    return("Your Grade is '{0}' and {1} performance.".format(a, b))

grade = int(input("Enter your grade :"))
if grade<=3 and grade>=11:
    print("invalid grades")

elif grade == 4:
    Grade = 'D'

elif grade == 5:
    Grade = 'C'

elif grade == 6:
    Grade = 'C+'

elif grade == 7:
    Grade = 'B'

elif grade == 8:
    Grade = 'B+'

elif grade == 9:
    Grade = 'A'

elif grade == 10:
    Grade = 'A+'

Performance = Gradelist[Grade]

print(marks(Grade,Performance))
print("="*80)

print("Program 5\nString Triangle maker")

#Makes Triangle with a String
str = "ABCDEFGHIJK"

i = 0
print(str)

while i <= len(str):
    str = str[:-2]

    a = str.center(11)
    print(a)

    if str == 'A':
        break

print("=" * 80)

print("Program 6\nStudents Details Dictionary")

#Starting with an empty dictionary.
Dict = {}

def Dictionary(d):
        Name = input("Enter your name :").lower()
        Sid = int(input("Enter your Sid :"))
        d[Sid] = Name

#applying Conditions
Answer = "Y"
while Answer == "Y":
    Dictionary(Dict)
    More = input("Want to enter more numbers? 'Y' or 'N'").upper()

    if More == "Y":
        Answer = "Y"

    elif More == "N":
        Answer = "N"
        break

    else:
        print("Wrong input Given")

#part(a)
print("All the student's details are:")

for Sid in Dict:
    print("Name     =>     SID")
    print(Dict[Sid],"   =>    ",Sid)

#part(b)
print("Sorting the dictionary by SID:")

L=list(Dict.keys())
L.sort()
Sort_by_SID = {}

for i in L:
    Sort_by_SID[i] = Dict[i]
print(Sort_by_SID)

#Part(c)
print("Sorting the dictionary by Names:")

List1 = list(Dict.values())
List1.sort()
sort_by_name = {}

for j in List1:
    temp = list(Dict.keys())[list(Dict.values()).index(j)]
    sort_by_name[temp] = Dict[temp]
print(sort_by_name)

#part(d)
Key = int(input("Enter the SID of person you want to Find.\n"))

if Key in Dict.keys():
    print("Name Of the Student with SID =",Key,"is ==>",Dict[Key])
else:
    print("No person with such SID")  

print("="*80)

print("Program 7\nFibonacci Sequence and average teller")

#Defining the first two numbers.
number_1 = 0
number_2 = 1

count = 0
List_of_numbers = []

#Applying Conditions on nth term
nth_term = int(input("Enter Your Number of terms :"))

if nth_term <= 0:
    print("enter valid number")

elif nth_term >= 1:

    if nth_term == 1:
        print("Your Number Is :", number_1)

    else:
        print("All of the", nth_term, "terms are :")

        while nth_term > count:
            nth_number = number_1+number_2
            List_of_numbers.append(number_1)
            Sum_of_numbers = sum(List_of_numbers)
            print(number_1, end=", ")
            number_1 = number_2
            number_2 = nth_number
            count += 1

    print("\nSum of all terms is :", Sum_of_numbers/nth_term)
    
print("="*80)

print("Program 8\nSet operations")
#Giving names to all Sets first

s1=[1, 2, 3, 4, 5]
s2=[2, 4, 6, 8]
s3=[1, 5, 9, 13, 17]
s4=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

set1 = set(s1)
set2 = set(s2)
set3 = set(s3)
set4 = set(s4)

print("part A")
set_a = ((set1.union(set2))-(set1.intersection(set2)))
print(set_a)

print("part B")
set_b = ((set1.union(set2.union(set3)))-(set1.intersection(set2.intersection(set3))))
print(set_b)

print("part C")
set_c = (set1.intersection(set2).union(set2.intersection(set3).union(set1.intersection(set3)))-(set1.intersection(set2.intersection(set3))))
print(set_c)

print("part D")
set_d = ((set4)-(set1))
print(set_d)

print("Part E")
set_e = ((set4)-(set1.union(set2).union(set3)))
print(set_e)

print("="*80)


