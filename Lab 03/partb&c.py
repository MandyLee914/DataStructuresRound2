## Mandy Ewing
## Part B and C
## Feb. 18, 2018
## Worked w/ Autumn

import time

e = int(input("Nth Number: "))

def fib(d):
    time.clock()
    time.clock()
    a = 1
    b = 1
    c = 0

    for i in range(d-2):
        c = b + a
        a = b
        b = c

    return(c)

def fibRecursion(d):
    time.clock()
    time.clock()

    if(d < 1):
        return(i)
    else:
        return(fib(d-1)+fib(d-2))

Dictfib = [1,1]
n = e
for i in range(n):
    Dictfib.append(0)

def DynamicFib(d):
    time.clock()
    time.clock()

    if Dictfib[d] == 0:
        Dictfib[d] = DynamicFib(d-1)+DynamicFib(d-2)
    return Dictfib[d]

NonRecursion = ("Non-Recursion: ", fib(e), "Runtime for Non-Recursion: ", time.clock())
Recursion = ("Recursion: ", fibRecursion(e),"Runtime for Recursion: ", time.clock())
Dynamic = ("Dynamic: ", DynamicFib(n), "Runtime for Dynamic Programming", time.clock()) 

def Comparisons():
   
    NonRecursionTime = NonRecursion[3:4]
    RecursionTime = Recursion[3:4]
    DynamicTime = Dynamic[3:4]
    
    if (NonRecursionTime > RecursionTime and DynamicTime > RecursionTime):
        return("Recursion was faster")
    elif (RecursionTime > NonRecursionTime and DynamicTime > NonRecursionTime):
        return("NonRecursion was faster")
    else:
        return("Dynamic Programming was faster")

      
print(NonRecursion)
print(Recursion)
print(Dynamic)
print(Comparisons())











