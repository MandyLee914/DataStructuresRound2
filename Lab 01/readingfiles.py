# Mandy Ewing
# Reading Files 2.0
# Due 1-21-18
# Worked with Autumn

counter = 0

openfile = open((input("Name a .txt file: ")), 'r')
for line in openfile.readlines():
    print(counter, line)
    counter = counter + 1
    
