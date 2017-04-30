##############
# utilities
##############
#
# the game state and variables will all be collected here to enable persitent
# game restart for version 2
#

debugflag = 0
location = [0,0]
cluster = 0
sector = 0
player = 0
state = 0
enemy = 0
ecount = 0

def fancyprint(text):
    import time
    for i in text:
        print(i,end='')
        if not debugflag:
            time.sleep (0.025)

def fancyinput(validlist):
    while True:
        entry = input('')
        if entry in validlist:
            return entry
        else:
            fancyprint('You cannot do that...\n' + 'Please enter one of the following:\n' + str(validlist)+'\n')


