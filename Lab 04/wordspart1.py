## Mandy Ewing
## WORKED WITH AUTUMN
## March 4, 2018


# PART A
import time
import wordlist.py

userinput = input("Choose a word: ")

def WordListsSearch(file, Swords):
    count = 0
    time.clock()
   
    for i in range(len(file)):
        if file[i] == Swords:
            return(i)
        else:
            count += 1
    return(file, time.clock(), count)

print(WordListsSearch(userinput, words))



# PART B

