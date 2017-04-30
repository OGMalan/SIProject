from Ships import Ship,Weapon,Shield
from util import fancyprint,fancyinput
import util
import random
import time

def combat():
    '''starts and ends a combat event'''
    util.enemy=shipgen()
    in_combat=True
    while in_combat:
        fancyprint ('')
        fancyprint ('player health = '+str(util.player.health)+'\n')
        fancyprint ('enemy health = '+str(util.enemy.health)+'\n')
        command = fight_or_flight()
        if command == 'flight':
            in_combat = False
            util.location[1]=0
            return 1
        if command == 'fight':
            combat_loop(sensor_check())
        if util.player.health < 1:
            time.sleep(1)
            fancyprint ('systems criti-'+'\n')
            fancyprint ('GAME OVER'+'\n')
            util.state=9
            in_combat=False
            return 0     
        if util.enemy.health < 1:
            time.sleep(1)
            fancyprint ('You watch as the enemy ship breaks apart'+'\n')
            util.sector[util.cluster][util.location[1]].event = 'Nothing'
            in_combat=False
            return 4
            
            
def combat_loop(shiplist):
    '''the main combat loop where ships are damaged'''
    if shiplist[1] == util.player:
        fancyprint('the enemy ship lines up to attack!'+'\n')
        damage = combat_roll()+util.enemy.attack
        util.player.damage(damage)
        time.sleep(1)
        fancyprint ('the attack does '+damagecalc(damage,util.player)+' damage!'+'\n')
        time.sleep(1)
        fancyprint('we line up to attack'+'\n')
        time.sleep(1)
        damage = combat_roll()+util.player.attack
        util.enemy.damage(damage)
        fancyprint ('the attack does '+damagecalc(damage,util.enemy)+' damage!'+'\n')
    else:
        fancyprint('we line up to attack'+'\n')
        damage = combat_roll()+util.player.attack
        util.enemy.damage(damage)
        time.sleep(1)
        fancyprint ('the attack does '+damagecalc(damage,util.enemy)+' damage!'+'\n')
        time.sleep(1)
        fancyprint('the enemy ship lines up to attack!'+'\n')
        time.sleep(1)
        damage = combat_roll()+util.enemy.attack
        util.player.damage(damage)
        fancyprint ('the attack does '+damagecalc(damage,util.player)+' damage!'+'\n')

def damagecalc(damage,ship):
    '''returns net damage when above 0 as a string'''
    netdamage = damage-ship.defence
    if netdamage > 0:
        return str(netdamage)
    else:
        return str(0)

def fight_or_flight():
    '''allows player to either engage (or continue) or exit combat'''
    fancyprint('Orders captain?\n')
    command = fancyinput(['flee','attack'])    
    if command == 'flee':
        return 'flight'
    if command == 'attack':
        return 'fight'  
        
def combat_roll():
    '''a random dice roll that adds on to a ship's weapon stat'''
    import random
    roll = random.randint(1,6)
    if roll == 6:
        roll += random.randint(1,6)
    return roll

def sensor_check():
    '''determines which ship starts combat'''
    if util.enemy.sensor > util.player.sensor:
        return [util.enemy,util.player]
    else:
        return [util.player,util.enemy]

def shipgen():
    '''generates a random enemy ship'''
    level = int(util.location[0]+random.randint(1,3))
    util.enemy = Ship('Pirate')
    util.enemy.attack = random.randint(1,level)
    util.enemy.defence = random.randint(1,level)
    util.enemy.sensor = random.randint(1,level)
    return util.enemy
