class System():
    import random
    event = random.randint(0,1)
    blurb = 'Descriptive text'
    def __init__(self, name, num):
        self.name = name + '-'+str(num)
    lane = random.randint(0,1)    

def clusgen(name):
    '''Generates a dictionary containing 3 System instances'''
    cluster = {}
    for i in range(1,4):
	    cluster[name+'-'+'{0}'.format(i)]=System(name,i)
    cluster = lanecheck(cluster)
    return cluster

def galaxygen():
    '''Generates a list of clusgen dictionaries'''
    galaxy = []
    galaxykeys = []
    names = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Epsilon', 'Zeta', 'Eta', 'Theta', 'Iota', 'Kappa']
    for name in names:
        galaxy.append(clusgen(name))
        galaxykeys.append(clusgen(name).keys())
    return galaxy

def lanecheck(cluster):
    '''Assures at least one System instance has a lane'''
    import random
    lanecount = 0
    for system in cluster:
        if cluster[system].lane == 1:
            lanecount += 1
    if lanecount == 0:
         cluster[random.choice(list(cluster.keys()))].lane = 1
    return cluster

#galaxy = galaxygen()
#print (galaxy[0]['Alpha-1'].event)
#print (galaxy[0]['Alpha-1'].blurb)
#print (galaxy[0]['Alpha-1'].lane) 
