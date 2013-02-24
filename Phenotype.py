class Phenotype:
    '''The Phenotype class encompases basic attributes of a living being in the game'''
    def __init__(self, hp, defense, power, death_function=None):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
        self.death_function = death_function

    def take_damage(self, damage):
        #apply damage if possible
        if damage > 0:
            self.hp -= damage
        if self.hp <= 0:
            function = self.death_function
            if function is not None:
                function(self.owner)

    def attack(self, target):
        #a simple formula for attack damage
        damage = self.power - target.phenotype.defense
 
        if damage > 0:
            #make the target take some damage
            print self.owner.name.capitalize() + ' attacks ' + target.name + ' for ' + str(damage) + ' hit points.'
            target.phenotype.take_damage(damage)
        else:
            print self.owner.name.capitalize() + ' attacks ' + target.name + ' but it has no effect!'
