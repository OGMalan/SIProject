import util

def clusgen(name):
    '''Generates a dictionary containing 3 System instances'''
    import random
    cluster = {}
    cluster[0]=name
    r = random.randint(1,4)
    for i in range(1,r+1):
	    cluster[i]=System(name,i)
    cluster = lanecheck(cluster)
    return cluster

def eventgen(glist):
    '''Randomly generates what happens when a player enters a system'''
    import random
    for dic in glist:
        for key in dic:
            if key != 0:
                event = random.choice(('Nothing','Combat','Event'))
                dic[key].event = event
                if event != 'Nothing':
                    util.ecount +=1
    return glist
    

def galaxygen():
    '''Generates a list of clusgen dictionaries'''
    if util.debugflag:
        print('Generating game world...')
        print(util.ecount)
    galaxy = []
    galaxykeys = []
    names = ('Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa')
    for name in names:
        galaxy.append(clusgen(name))
        galaxykeys.append(clusgen(name).keys())
    util.ecount = 0
    while util.ecount < 10:
        galaxy = eventgen(galaxy)
    return galaxy

def lanecheck(cluster):
    '''Assures at least one System instance has a lane'''
    import random
    lanecount = 0
    for system in cluster:
        try:
            if cluster[system].lane == 1:
                lanecount += 1
            if lanecount == 0:
                 cluster[1].lane = 1
        except AttributeError:
            continue
    return cluster

class System():
    import random
    event = ''
    blurb = 'Descriptive text'
    def __init__(self, name, num):
        self.name = name + '-'+str(num)
    lane = random.randint(0,1)


    

#galaxy = galaxygen()
#print (galaxy[0]['Alpha-1'].event)
#print (galaxy[0]['Alpha-1'].blurb)
#print (galaxy[0]['Alpha-1'].lane) 
