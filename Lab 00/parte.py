# Mandy Ewing
# Part E: 1/12/2018

for i in range(1,50):
    isPrime = True
    for j in range(1, i):
        if i % j == 0:
            isPrime = False
            break
    if isPrime:
        print(i)
