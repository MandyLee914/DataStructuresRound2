# Mandy Ewing
# Part B: 1/12/2018
# Had Troubles with this program, looked back on ICE from 11/7/16


counter = 0

infile = open("partb.py", 'r')
for line in infile.readlines():
    print(counter, line)
    counter = counter + 1
    
    
