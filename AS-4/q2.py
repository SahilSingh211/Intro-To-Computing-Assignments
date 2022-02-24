def factorial(Number):
    if Number == 0:
        return 1
    else:  
        b = (Number * factorial(Number - 1))
    return b


a = int(input())
for n in range(0, a):
    L = []
    for i in range(n+1):
        L.append(str(int(factorial(n))//(int(factorial(n-i))*(int(factorial(i))))))
            
    d = (" ".join(L))

    print(d.center(a*a))

        

   

    


