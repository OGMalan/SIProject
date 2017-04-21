class Ship():
    health = 10
    attack = 1
    defence = 1
    equipped = []
    sensor = 1
    
    def __init__(self,name):
        self.name = name
        
    def damage(self,damage):
        netdamage = damage-self.defence
        if netdamage > 0:
            self.health -= netdamage
            return self.health

    def equip_weapon(self,weapon):
        self.attack += weapon.damage

    def equip_shield(self,shield):
        self.attack += shield.defence

    def equip_sensor(self,sensor):
        self.sensor += sensor.value

class Weapon():
    equipment_type = 'weapon'
    def __init__(self,name,damage):
        self.name = name
        self.damage = damage

class Shield():
    equipment_type = 'shield'
    def __init__(self,name,defence):
        self.name = name
        self.defence = defence

class Sensor():
    equipment_type = 'sensor'
    def __init__(self,name,value):
        self.name = name
        self.sensor = sensor






    
    
    
