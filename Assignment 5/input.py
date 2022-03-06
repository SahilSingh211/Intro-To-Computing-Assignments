from tkinter import *


# Question 1.
# Finding GST rate from Net Price and Original Cost given by User.

def Calculation():
    # Creating a function to calculate GST and tax.

    global Net_Price, Original_Cost, GST_Rate, Difference                                                               # Defining global variables for GST calculation.

    # Giving an error if user input value is empty(none).
    if len(Var1.get()) == 0 or len(Var2.get()) == 0:
        messagebox.showerror("Error", "No value has been entered in Original Cost or Net Price.")

    else:
        # Creating an exception for errors.
        try:
            Original_Cost = float(Var1.get())
            Net_Price = float(Var2.get())
            Difference = Net_Price - Original_Cost
            GST_Rate = (Difference * 100) / Original_Cost                                                               # Calculating GST.

        except Exception as e:
            messagebox.showerror("Error", str(e))                                                                       # Prompting an error message if any error occurs.

        # Giving an error window if original cost is greater than net price .
        if Original_Cost > Net_Price:
            Q = messagebox.askokcancel("Warning",
                                       "The value of Original Cost is given greater than Net Price.\
                                       Do you wish to continue?")

            # Displaying the result if user selects ok.
            if Q:
                nb3.config(
                    text="Result :\n\nCalculated GST rate : {0:.2f}%\nTotal tax on given Net Price : ₹{1:.2f}".format(
                        GST_Rate,
                        Difference))
                nb3.grid(row=3, columnspan=2, pady=10)
            else:
                pass
        else:
            nb3.config(
                text="Result :\n\nCalculated GST rate : {0:.2f}%\nTotal tax on given Net Price : ₹{1:.2f}".format(
                    GST_Rate,
                    Difference))
            nb3.grid(row=3, columnspan=2, pady=10)


Main1 = Tk()

# Title of GUI.
Main1.title("Question 1")                                                                                               # Geometry of GUI.
Main1.geometry('600x600')
Main1.minsize(450, 370)
Main1.maxsize(700, 700)

# Background Color
Main1['bg'] = '#90a98a'

# Heading.
Heading = Label(Main1, text="GST Calculator", bg='#90a98a', fg='white', font=('Times New Roman', 22, 'underline'), bd=5)
Heading.pack(pady=15, ipadx=15)

# Creating a frame.
frame1 = Frame(Main1, bd=20)
frame1.pack()

# Content inside Frame.
lb1 = Label(frame1, text="Original Cost :", font=("Times New Roman", 12, "bold"))                                       # Label 1.
lb1.grid(row=0, column=0, pady=15)

Var1 = Entry(frame1, font=("Times New Roman", 12))                                                                      # Entry box 1
Var1.grid(row=0, column=1, pady=15)

lb2 = Label(frame1, text="Net Price :", font=("Times New Roman", 12, "bold"))                                           # Label 2
lb2.grid(row=1, column=0, pady=15)

Var2 = Entry(frame1, font=("Times New Roman", 12))  # Entry box 2
Var2.grid(row=1, column=1, pady=15)

bt1 = Button(frame1, text="Calculate", command=Calculation, cursor='hand2', font=("Times New Roman", 12))               # Button 1
bt1.grid(row=2, columnspan=2, pady=15)

nb3 = Label(frame1, bg='#293027', fg='white', font=("Times New Roman", 12), bd=7)                                       # Label 3 (for displaying result)

Main1.mainloop()

# Question 2.
# Program to show Calendar of a Given Year.

import calendar


def Calendar():
    # Defining a function to Create a separate window to display the calendar.

    global Year                                                                                                         # Defining a global variable.

    try:
        int(Var1.get())
    except Exception as e:
        messagebox.showerror("Error", str(e))

    # Prompting Error if user enters no input.
    if len(Var1.get()) == 0:
        messagebox.showerror("Error", "No value has been entered for year.")

    elif int(Var1.get()) <= 0:
        messagebox.showerror("Error", " Year cannot be -ve or 0.")

    else:
        # Creating an exception if invalid integer is entered by the user.
        try:
            Year = int(Var1.get())  # Getting value from entry box 1.

        except Exception as e:
            messagebox.showerror("Error", str(e))

        # Using calendar library to print the Calendar.
        Calendar = calendar.calendar(Year)

        # Creating a different window to print Calendar
        Top1 = Toplevel(Main2)

        # Title.
        Top1.title(f"{Year} Calendar")
        # Geometry.
        Top1.geometry('640x630')
        Top1.minsize(640, 640)
        Top1.maxsize(640, 640)

        # Content.
        txt1 = Text(Top1, width=100, height=100, borderwidth=2, relief=RAISED)                                          # Text box 1.
        txt1.pack(padx=20, pady=10)

        txt1.insert('end', Calendar)                                                                                    # Inserting calendar string in Text box 1.

        Top1.mainloop()


Main2 = Tk()

# Title.
Main2.title("Question 2")                                                                                               # Geometry
Main2.geometry('400x300')
Main2.minsize(350, 250)
Main2.maxsize(500, 400)

# Background Color.
Main2['bg'] = '#45adbd'

# Heading
Head = Label(Main2, text=" Calendar ", bd=5, font=('Times New Roman', 40, 'underline'), bg='#45adbd', fg='white')
Head.pack(pady=10, ipadx=10)

# Creating a frame.
f1 = Frame(Main2, bd=20)
f1.pack()

# Content
lb1 = Label(f1, text="Enter year :", font=("Times New Roman", 15))  # Label 1
lb1.pack(pady=5)

Var1 = Entry(f1, font=("Times New Roman", 12))  # Entry box 1
Var1.pack(pady=5)

bt1 = Button(f1, text="Show Calendar", command=Calendar, cursor='hand2', font=("Times New Roman", 15))  # Button 1
bt1.pack(pady=5)

Main2.mainloop()

# Question 3.
# Program to create a GUI-based calculator.

from tkinter import messagebox


def btn(e):
    # Defining a function for buttons to perform functions when pressed.

    global val                                                                                                          # Defining a global variable.

    text = e.widget.cget("text")

    # calculating the result if '=' button is pressed.
    if text == "=":

        if val.get().isdigit():
            try:
                value = eval(val.get())
            except Exception as exp:
                messagebox.showerror("Error", str(exp))
                value = "Error"
        else:
            try:
                value = eval(cal_screen.get())
            except Exception as exp:
                value = "Error"
                messagebox.showerror("Error", str(exp))

        val.set(value)                                                                                                  # Setting the value of entry box to the result.
        cal_screen.update()                                                                                             # Updating the Entry box.

    # Clearing the screen if 'C' button is pressed clearing the screen.
    elif text == 'C':
        val.set("")
        root3.update()

    else:
        val.set(str(val.get()) + str(text))
        cal_screen.update()


def equals(n):
    #Defining a Function which gives output when enter is pressed.

    # Same as '=' condition above.
    if val.get().isdigit():
        try:
            value = eval(val.get())
        except Exception as exp:
            messagebox.showerror("Error", str(exp))
            value = "Error"
    else:
        try:
            value = eval(cal_screen.get())
        except Exception as exp:
            value = "Error"
            messagebox.showerror("Error", str(exp))

    val.set(value)
    cal_screen.update()


root3 = Tk()

# Title.
root3.title("Question 3")

# Geometry.
root3.geometry('600x750')
root3.minsize(425, 620)

# Background Color.
root3['bg'] = '#fff2cc'

# Heading.
Heading = Label(root3, text="Calculator", bd=5, font=('Times New Roman', 40, 'underline'), bg='#fff2cc', fg='black')
Heading.pack(pady=15, ipadx=15)

# Content.
val = StringVar()                                                                                                       # val(a String variable for entry box)
val.set("")                                                                                                             # setting val's value to ""
cal_screen = Entry(root3, textvariable=val, font=("Helvetica", 30, "bold"),
                   width=19)                                                                                            # cal_screen - Entry box for calculator input.
cal_screen.pack(fill=X, padx=25)
cal_screen.bind('<Return>', equals)

f1 = Frame(root3, bg='LightYellow3')  # Frame 1.
f1.pack(pady=15, fill=BOTH, padx=25, side=TOP)

# Creating Buttons.
bt1 = Button(f1, text="/", font=("Helvetica", 25, "bold"), width=3)
bt2 = Button(f1, text="*", font=("Helvetica", 25, "bold"), width=3)
bt3 = Button(f1, text="-", font=("Helvetica", 25, "bold"), width=3)
bt4 = Button(f1, text="C", font=("Helvetica", 25, "bold"), width=3)
bt5 = Button(f1, text=7, font=("Helvetica", 25, "bold"), width=3)
bt6 = Button(f1, text=8, font=("Helvetica", 25, "bold"), width=3)
bt7 = Button(f1, text=9, font=("Helvetica", 25, "bold"), width=3)
bt8 = Button(f1, text="+", font=("Helvetica", 25, "bold"), height=4, width=3)
bt9 = Button(f1, text=4, font=("Helvetica", 25, "bold"), width=3)
bt10 = Button(f1, text=5, font=("Helvetica", 25, "bold"), width=3)
bt11 = Button(f1, text=6, font=("Helvetica", 25, "bold"), width=3)
bt12 = Button(f1, text=1, font=("Helvetica", 25, "bold"), width=3)
bt13 = Button(f1, text=2, font=("Helvetica", 25, "bold"), width=3)
bt14 = Button(f1, text=3, font=("Helvetica", 25, "bold"), width=3)
bt15 = Button(f1, text="=", font=("Helvetica", 25, "bold"), height=4, width=3)
bt16 = Button(f1, text=0, font=("Helvetica", 25, "bold"), width=8)
bt17 = Button(f1, text=".", font=("Helvetica", 25, "bold"), width=3)

# Grid Configuring.
Grid.columnconfigure(f1, 0, weight=1)
Grid.columnconfigure(f1, 6, weight=1)

# Griding all the buttons.
bt1.grid(row=0, column=1, padx=15, pady=15)
bt2.grid(row=0, column=2, padx=15, pady=15)
bt3.grid(row=0, column=3, padx=15, pady=15)
bt4.grid(row=0, column=4, padx=15, pady=15)
bt5.grid(row=1, column=1, padx=15, pady=15)
bt6.grid(row=1, column=2, padx=15, pady=15)
bt7.grid(row=1, column=3, padx=15, pady=15)
bt8.grid(row=1, column=4, columnspan=2, rowspan=2, padx=15, pady=15)
bt9.grid(row=2, column=1, padx=15, pady=15)
bt10.grid(row=2, column=2, padx=15, pady=15)
bt11.grid(row=2, column=3, padx=15, pady=15)
bt12.grid(row=3, column=1, padx=15, pady=15)
bt13.grid(row=3, column=2, padx=15, pady=15)
bt14.grid(row=3, column=3, padx=15, pady=15)
bt15.grid(row=3, column=4, columnspan=2, rowspan=2, padx=15, pady=15)
bt16.grid(row=4, column=1, columnspan=2, rowspan=2, padx=15, pady=15)
bt17.grid(row=4, column=3, padx=15, pady=15)

# Binding all the buttons to functions.
bt1.bind("<Button-1>", btn)
bt2.bind("<Button-1>", btn)
bt3.bind("<Button-1>", btn)
bt4.bind("<Button-1>", btn)
bt5.bind("<Button-1>", btn)
bt6.bind("<Button-1>", btn)
bt7.bind("<Button-1>", btn)
bt8.bind("<Button-1>", btn)
bt9.bind("<Button-1>", btn)
bt10.bind("<Button-1>", btn)
bt11.bind("<Button-1>", btn)
bt12.bind("<Button-1>", btn)
bt13.bind("<Button-1>", btn)
bt14.bind("<Button-1>", btn)
bt15.bind("<Button-1>", btn)
bt16.bind("<Button-1>", btn)
bt17.bind("<Button-1>", btn)

root3.mainloop()

# Question 4

print("Question 4\nQuick-Sorting")


# Defining Quicksort for list
def quicksort(array, left, right):
    if left < right:
        partition_pos = partition(array, left, right)                                                                   # Partition_pos is position from where to part List.

        quicksort(array, left, partition_pos - 1)                                                                       # Quicksort in left List.
        quicksort(array, partition_pos + 1, right)                                                                      # Quicksort in Right List.


# Defining Partition function for quick sorting
def partition(array, left, right):
    i = left
    j = right - 1
    pivot = array[right]

    while i < j:

        while i < right and array[i] < pivot:                                                                           # Condition for i.
            i += 1
        while j > left and array[j] >= pivot:                                                                           # Condition for j.
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]                                                                     # Interchanging elements of array.

    if array[i] > pivot:
        array[i], array[right] = array[right], array[i]                                                                 # Interchanging element and pivot.

    return i


# asking user to input number of students and their marks one by one
while True:
    try:
        num_of_students = int(input("\nEnter number of students :"))
        if num_of_students <= 0:
            print("\nPlease enter a positive integer value!\n")

            continue
        else:
            break
            
    except ValueError:
        print("\nError! Please enter a positive integer value only!\n")

List_of_num = []

# appending all student's numbers in a list
for k in range(1, num_of_students + 1):
    while True:
        try:
            val_=(eval(input("\nEnter the marks of student {} ==>".format(k))))
            List_of_num.append(val_)
            break
        
        except Exception as e:
            print("Error! Please try again!")
            continue
        

print("\nList of marks of Students entered by the User is:", List_of_num)

quicksort(List_of_num, 0, len(List_of_num) - 1)

print("\nList of marks of Students after quick sorting is:", List_of_num)

# Question 5
print("\nProgram 5\nBinary Searching and Occurrence finder")


# Defining the function for Binary Search.
def Binary_Search(arr, n, low, high):
    if low <= high:  # Always True.
        mid = (low + high) // 2
        if arr[mid] == n:
            return mid                                                                                                  # Gives index of number to find.

        # Applying conditions if middle number is not equal to n.
        elif arr[mid] < n:
            return Binary_Search(arr, n, mid + 1, high)

        else:
            return Binary_Search(arr, n, low, mid - 1)

    else:
        return -1


# Asking user to input numbers with a space between them.
numbers = list(map(int, input("Enter all numbers with spaces between them:\n").split()))

numbers.sort()
print("The sorted list of numbers given is :", numbers)

Search_num = int(
    input("\nWhich number's index do you want to know?: ").strip())                                                     # Asking user to input number to find index of

if Search_num not in numbers:
    print(f"\nNumber {Search_num}, is not in the list!")


else:
    result = Binary_Search(numbers, Search_num, 0, len(numbers))
    if result != -1:
        print(f"\nThe number {Search_num} is found at index {result} and it's position in the list is {result + 1}.")
    else:
        pass
print(f"\nNumber {Search_num} is occurred {numbers.count(Search_num)} times in the given List.")
