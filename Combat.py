from Ships import Ship,Weapon,Shield

player = Ship('Player')
enemy = Ship('Hawk')

def combat():
    in_combat=True
    print('combat event!')
    while in_combat:
        print ('player health = '+str(player.health))
        print ('enemy health = '+str(enemy.health))
        command = fight_or_flight()
        if command == 'flight':
            in_combat = False
            return
        if command == 'fight':
            combat_loop([player,enemy])
        if player.health < 1:
            print ('systems criti-')
            print ('GAME OVER')
            in_combat=False
            return        
        if enemy.health < 1:
            print ('You watch as the enemy ship breaks apart')
            in_combat=False
            return
            
            
def combat_loop(shiplist):
        if shiplist[1] == player:
                print('the enemy ship lines up to attack!')
                damage = combat_roll()+enemy.attack
                player.damage(damage)
                print ('the attack does '+str(damage)+' damage!')
        else:
            print('we line up to attack')
            damage = combat_roll()+player.attack
            enemy.damage(damage)
            print ('the attack does '+str(damage)+' damage!')

def fight_or_flight():
    command = input('orders captain?\n')
    if command == 'flee':
        return 'flight'
    if command == 'attack':
        return 'fight'
    
        
def combat_roll():
    import random
    roll = random.randint(1,6)
    if roll == 6:
        roll += random.randint(1,6)
    return roll

def sensor_check():
    if enemy.sensor > player.sensor:
        return [enemy,player]
    else:
        return [player,enemy]

running = True
while running:
    print('combat test')
    combat()
    yesno = input('Run again? ')
    if yesno == 'y':
        continue
    else:
        running = False


    
