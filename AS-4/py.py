def TowerOfHanoi (n, Starting, Targeted, Assistant):
    if n==1:
        print ("Move disk 1 from {0} rod to {1} rod".format(Starting,Targeted))
        return
    TowerOfHanoi(n - 1, Starting, Assistant, Targeted)
    print ("Move disk {0} from {1} rod to {2} rod".format(n,Starting,Targeted))
    TowerOfHanoi(n - 1, Assistant, Targeted, Starting)

n=int(input("Enter The number of Disks :"))
A="Start"
b=input(("Enter the Name of Rod where you want them to be, T for Targeted, A for Assistant :"))
b=b.upper()

if b=="T":
    b="Targeted"
    c="Assistant"

elif b=="A":
    b="Assistant"
    c="Targeted"

else:
    print("Wrong Rod Chosen")
    
TowerOfHanoi(n, A, b, c)