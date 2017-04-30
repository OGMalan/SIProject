from util import fancyprint
import util

def eventcheck(s):
    try:
        fancyprint('Scanning system...\n')
        if util.location[1]==0:
            return 1
        else:
            if util.sector[util.cluster][util.location[1]].event == 'Combat':
                fancyprint("We've detected a hostile ship!\n")
                return 2
            if util.sector[util.cluster][util.location[1]].event == 'Event':
                return 3    
            if util.sector[util.cluster][util.location[1]].event == 'Nothing':
                return 4
        return 1
    except KeyError:
        return 1
    
def lanecheck():    
    if util.sector[util.cluster][util.location[1]].lane == 1:
        return True
    else:
        return False

def event():
    fancyprint('An event happens!\n')

def lane():
    if util.sector[util.cluster][util.location[1]].lane == 1:
        fancyprint('This system has a hyperlane to the next cluster!\n')
        fancyprint('Do we enter?: ')
        laneinput = input('')
        yes = ['yes','y']
        no = ['no','n']
        if laneinput in 'yes':
            util.cluster+=1
            if util.cluster >10:
                util.cluster=0 
            util.location[1]=0
        if laneinput in 'no':
            return
    
    
    
