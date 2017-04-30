from Ships import Ship,Weapon,Shield,Sensor
from GalaxyGen import galaxygen,System
from Navigation import navigation
from Combat import combat
from Event import eventcheck,lane,lanecheck,event
from util import fancyprint,fancyinput
import util
import random


def newgame():
    '''Generates a player named ship, with a bonus in a selected attribute as well as the game world'''
    fancyprint ('''-begin transmission-

The year is 2134.
The United Nations of Earth have just launched the "Systems Initiative" project.
As part of the project a number of exploratory vessels have been launched to chart unknown parts of the Milky Way.

You are the captain of one of these vessels, the UNE: ''')
    name = input('')
    util.player = Ship(name)
    fancyprint('\nThe ')
    fancyprint(name)
    fancyprint(' is a state of the art vessel equipped with a cutting edge jump drive, as well as state of the art ')
    while True:
        freegear = input('')
        if freegear == 'weapons':
            LMk1 = Weapon('Mk1 Laser',3)
            util.player.equip_weapon(LMk1)
            break
        
        if freegear == 'shields':
            SMk1 = Shield('Mk1 Shield',3)
            util.player.equip_shield(SMk1)
            break
        if freegear == 'sensors':
            SensMk1 = Sensor('Mk1 Sensor Suite',3)
            util.player.equip_sensor(SensMk1)
            break
        else:
            print("Invalid input, please choose either 'weapons', 'shields' or 'sensors'")
    print('')
    fancyprint ('''Your task is to map the all the systems in the ''')
    names = ('Alpha','Beta','Gamma','Delta','Epsilon','Zeta','Eta','Theta','Iota','Kappa','Lambda','Mu','Nu','Xi','Omicron','Pi','Rho','Sigma','Tau','Upsilon','Phi','Chi','Psi','Omega')
    sectorname = random.choice(names)
    fancyprint(sectorname)
    fancyprint(''' sector.
The sector has been arbitrarily arranged into 10 clusters, each containing a number of solar systems.

The systems are all within range for short
range jumps, but to move between clusters you will have to find and utilise hyperlanes.

When you are finished investigating all the systems, or wish to abandon your mission, you can conduct a jump out of the sector. Keep in mind you will not be able to return when you do this.

Good luck, captain.
-end of transmission-


---system computer---
Starting Jump\n''')
    util.sector = galaxygen()
    util.state = 1

def debug():
    '''Debug function to mimic the result of ghe newgame function'''
    print('debugging')
    util.sector = galaxygen()
    util.player = Ship('name')
    util.state = 1
    
def main():
    running = True
    util.state = 0
    print('Welcome to SISpace!')
    while running:
        if util.state == 0:
            if util.debugflag == 0:
                newgame()
            else:
                debug()
        if util.state == 1:
            navigation()
            util.state = eventcheck(util.state)
        if util.state == 2:
            util.state = combat()
        if util.state == 3:
            event()
            util.state = 4
            util.sector[util.cluster][util.location[1]].event = 'Nothing'
            util.ecount -= 1
            if util.ecount == 0:
                fancyprint("You've Won!\n")
                util.state=9
        if util.state == 4:
            if lanecheck() == True:
                lane()
                util.state = 1
            else:
                util.state = 1
        if util.state == 9:
            fancyprint('Play again?\n')
            if fancyinput(['y','yes','n','no'])[:1] != 'y':
                fancyprint('Goodbye!')
                quit()
            else:
                util.state=0
            
main()
