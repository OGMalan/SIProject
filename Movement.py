from GalaxyGen import galaxygen,System

def movement():
    '''keeps track and changes player's location'''
    location = [0,0]
    galaxy = galaxygen()
    galaxykeys = keys(galaxy)
    systems = []
    for i in galaxykeys[location[0]]:
        systems.append(i)
    print('The systems in range to move to are: '+str(systems))
    command = int(input('Choose a system to move to: '))
    location[1] = command
    print ('You have entered the '+str(systems[command-1])+' system')
    print (galaxy[0][systems[command-1]].blurb)
    eventhandler(command,galaxy,systems)
    location[0] += hyperlane(command,galaxy,systems)
    

def eventhandler(command,galaxy,systems):
    if galaxy[0][systems[command-1]].blurb == 1:
        print('Shit happens!')
    else:
        print('Nothing happens')

def hyperlane(command,galaxy,systems):
    if galaxy[0][systems[command-1]].lane == 1:
        print("There's a hyperlane to the next cluster")
        jump = input('Do you want to to jump to the next cluser?\ny/n')
        if jump == y:
            return 1
    else:
        return 0
    
def keys(galaxy):
    '''returns a list of the keys of the cluster dictionaries'''
    galaxykeys = []
    for i in galaxy:
        galaxykeys.append(i.keys())
    return galaxykeys
movement()
