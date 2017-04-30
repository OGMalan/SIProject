from util import fancyprint,fancyinput
import util

def navigation():
    '''Main navigation function'''   
    fancyprint('''Jump complete\n''')
    if util.debugflag:
        print (util.location)
    loc_check()    
    move()
    

def loc_cluster():
    fancyprint('''\n---navigation computer---
we have arrived at the '''+str(util.sector[util.cluster][0])+' cluster\n')
    fancyprint('The systems in this cluster are:\n')
    for i in util.sector[util.cluster]:
        try:            
            fancyprint(util.sector[util.cluster][i].name+'\n')
        except AttributeError:
            continue

def loc_system():
    if util.debugflag:
        print('    event: '+ str(util.sector[util.cluster][util.location[1]].event))
        print('    lane: '+ str(util.sector[util.cluster][util.location[1]].lane))
    fancyprint('''\n---navigation computer---
we have arrived at the '''+str(util.sector[util.cluster][util.location[1]].name)+' system\n')   
    fancyprint('We can move to:\n')
    if len(util.sector[util.cluster]) == 2:
        fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
    if len(util.sector[util.cluster]) == 3:
        if util.location[1] == 1:
            fancyprint(util.sector[util.cluster][2].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
        else:
            fancyprint(util.sector[util.cluster][1].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
    if len(util.sector[util.cluster]) == 4:
        if util.location[1] == 1:
            fancyprint(util.sector[util.cluster][2].name+'\n')
            fancyprint(util.sector[util.cluster][3].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
        if util.location[1] == 2:
            fancyprint(util.sector[util.cluster][1].name+'\n')
            fancyprint(util.sector[util.cluster][3].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
        if util.location[1] == 3:
            fancyprint(util.sector[util.cluster][2].name+'\n')
            fancyprint(util.sector[util.cluster][1].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
    if len(util.sector[util.cluster]) == 5:
        if util.location[1] == 1:
            fancyprint(util.sector[util.cluster][2].name+'\n')
            fancyprint(util.sector[util.cluster][4].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
        if util.location[1] == 2:
            fancyprint(util.sector[util.cluster][1].name+'\n')
            fancyprint(util.sector[util.cluster][3].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
        if util.location[1] == 3:
            fancyprint(util.sector[util.cluster][2].name+'\n')
            fancyprint(util.sector[util.cluster][4].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')
        if util.location[1] == 4:
            fancyprint(util.sector[util.cluster][3].name+'\n')
            fancyprint(util.sector[util.cluster][1].name+'\n')
            fancyprint(str(util.sector[util.cluster][0])+'-0 (cluster)''\n')

def move():
    '''Does a check to determine which systems the player can move to and adjusts location'''
    fancyprint('Select a system to move to: ')
    validlist = []
    for i in util.sector[util.cluster]:
        try:            
            validlist.append(util.sector[util.cluster][i].name[-1])
        except AttributeError:
            continue
    select = fancyinput(validlist)
    if select == 'info':
        info()
    else:
        util.location[1] = int(select)
                

def loc_check():
    if util.location[1] == 0:
        loc_cluster()
    else:
        loc_system()

def info():
    print('    name: ' + util.sector[util.cluster][util.location[1]].name)
    print('    event: ' + util.sector[util.cluster][util.location[1]].event)
    print('    lane: ' + str(util.sector[util.cluster][util.location[1]].lane))
    
    
