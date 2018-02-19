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

NonRecursion = ("Non-Recursion: ", fib(e), "Runtime for Non-Recursion: ", time.clock())
Recursion = ("Recursion: ", fibRecursion(e),"Runtime for Recursion: ", time.clock())

NonRecursionTime = NonRecursion[3:4]
RecursionTime = Recursion[3:4]
#Part C

def DynamicFib(d):
    Dictfib = {}
    time.clock()
    time.clock()

    if d < 2:
        return d
    if d in Dictfib:
        return Dictfib[d]
        Dictfib[d] = DynamicFib(d-1) + DynamicFib(d-2)
        return Dictfib[d]


Dynamic = ("Dynamic: ", DynamicFib(e), "Runtime for Dynamic ", time.clock())


def Comparisons():
    if NonRecursionTime > RecursionTime:
        return("Recursion was somehow faster")
    else:
        return("NonRecursion was suprisingly faster")



        
print(NonRecursion)
print(Recursion)
print(Dynamic)
print(Comparisons())











