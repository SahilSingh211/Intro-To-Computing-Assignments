def Divmod(a,b):
    x= a//b
    y= a%b
    return(x,y)
num1=int(input("Enter first number :"))
num2 = int(input("Enter Second number :"))
d=(Divmod(num1,num2))
L=[]
e=[]
print(d)
for i in d:
    L.append(i)
L.append(num1)
L.append(num2)
print(callable(Divmod)) #parta
if 0 in L:
    print(True)
else:
    print(False)
        

#part c
for j in [4,5,6]:
    L.append(j)
for k in range(len(L)):
    if L[k]>4:
        e.append(L[k])
f=set(e)
g=frozenset(f)
print(g)
h=max(g)
print(h)
print(hash(g))

