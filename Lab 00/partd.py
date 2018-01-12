# Mandy Ewing
# Part D: 1/12/2018
# Recrusive (iff-y on)


def factorial (n): # base case that never changes
    if n == 1:
        return 1
    else:
        print(n)
        return(n * factorial(n-1))


print(factorial(10))
