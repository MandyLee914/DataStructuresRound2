##Simulation 2.0
##Mandy Ewing
##Worked w/ Autumn
##2-4-2018
##Also Used In Class Examples/Stuff you gave us.
## https://wiki.python.org/moin/HowTo/Sorting
##https://stackoverflow.com/questions/10695139/ \(divided it into two lines)
##sort-a-list-of-tuples-by-2nd-item-integer-value

import random
import time

names = ["Joey","Bobby","SueAnn","Loretta","Grant",\
         "Jenny","Billy","Tucker","Cletus","Hunter",\
         "Gunner","Rose","Amy","Charlette","Duke","Ricky",\
         "Bo","Luke","Jesse"]

waitingRoom = []
triageRoom = []
examRoom = []
examRoomSize = 6
doctors = 6

time.clock()

class Patient:
    def __init__(self):
        self.triageNumber = (random.randint(0,100))
        self.name = names[random.randint(1, len(names)-1)]\
                    + " " + names[random.randint(0, len(names)-1)]
        self.arrivalTime = time.clock()
        self.treatmentTime = random.randrange(15,20)
    
    def exit(self):
        examRoom.remove(Patient)

def TriageNurse():
    from operator import itemgetter, attrgetter, methodcaller

    """ Move patient from waitingRoom to traigeRoom"""
    triageRoom.append(waitingRoom.pop(0))
    sorted(triageRoom, key = lambda x: x[2])
    print("Triage Room: ", triageRoom)
    
    """Move patient from triageRoom to examRoom""" 

def ExamRoom():
    if len(examRoom) < 7:
        examRoom.append(triageRoom.pop(0))
        print("Exam Room: ", examRoom)
    else:
        print("Triage Room: ", triageRoom)
        
def WaitingRoom():
    waitingRoom.append((patientName.name, patientName.triageNumber, \
                       patientName.arrivalTime))
    print("Waiting Room: ", waitingRoom)
    
patientName = Patient()
time.clock()

WaitingRoom()
TriageNurse()
ExamRoom()





















