from Ships import Ship,Weapon,Shield
import random
import time

def combat():
    '''starts and ends a combat event'''
    in_combat=True
    while in_combat:
        print ('')
        print ('player health = '+str(player.health))
        print ('enemy health = '+str(enemy.health))
        command = fight_or_flight()
        if command == 'flight':
            in_combat = False
            return
        if command == 'fight':
            combat_loop(sensor_check())
        if player.health < 1:
            time.sleep(0.5)
            print ('systems criti-')
            print ('GAME OVER')
            in_combat=False
            return        
        if enemy.health < 1:
            time.sleep(0.5)
            print ('You watch as the enemy ship breaks apart')
            in_combat=False
            return
            
            
def combat_loop(shiplist):
    '''the main combat loop where ships are damaged'''
    if shiplist[1] == player:
        print('the enemy ship lines up to attack!')
        damage = combat_roll()+enemy.attack
        player.damage(damage)
        time.sleep(0.5)
        print ('the attack does '+damagecalc(damage,player)+' damage!')
        time.sleep(0.5)
        print('we line up to attack')
        time.sleep(0.5)
        damage = combat_roll()+player.attack
        enemy.damage(damage)
        print ('the attack does '+damagecalc(damage,enemy)+' damage!')
    else:
        print('we line up to attack')
        damage = combat_roll()+player.attack
        enemy.damage(damage)
        time.sleep(0.5)
        print ('the attack does '+damagecalc(damage,enemy)+' damage!')
        time.sleep(0.5)
        print('the enemy ship lines up to attack!')
        time.sleep(0.5)
        damage = combat_roll()+enemy.attack
        player.damage(damage)
        print ('the attack does '+damagecalc(damage,player)+' damage!')

def damagecalc(damage,ship):
    '''returns net damage when above 0 as a string'''
    netdamage = damage-ship.defence
    if netdamage > 0:
        return str(netdamage)
    else:
        return str(0)

def fight_or_flight():
    '''allows player to either engage (or continue) or exit combat'''
    command = input('orders captain?\n')    
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
    if enemy.sensor > player.sensor:
        return [enemy,player]
    else:
        return [player,enemy]

def shipgen():
    '''generates a random enemy ship'''
    enemy = Ship('new')
    enemy.attack = random.randint(1,10)
    enemy.defence = random.randint(1,10)
    enemy.sensor = random.randint(1,2)
