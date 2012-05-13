class Phenotype:
    '''The Phenotype class encompases basic attributes of a living being in the game'''
    def __init__(self, hp, defense, power):
        self.max_hp = hp
        self.hp = hp
        self.defense = defense
        self.power = power
