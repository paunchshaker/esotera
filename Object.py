import libtcodpy as libtcod

class Object:
    #this is a generic object: the player, a monster, an item, the stairs...
    #it's always represented by a character on screen.
    def __init__(self, x, y, char, name, color, blocks=False, phenotype=None, ai=None):
        self.x = x
        self.y = y
        self.char = char
        self.color = color
        self.name = name
        self.blocks = blocks

        #components go here
        #each component has a property owner that gets set upon assignment
        self.phenotype = phenotype
        if self.phenotype:
            self.phenotype.owner = self
 
        self.ai = ai
        if self.ai:
            self.ai.owner = self
 
    def move(self, map, dx, dy):
        if not map.is_blocked(self.x + dx, self.y + dy):
            #move by the given amount
            self.x += dx
            self.y += dy
 
    def draw(self, con, fov_map):
        #set the color and then draw the character that represents this object at its position
        if libtcod.map_is_in_fov(fov_map, self.x, self.y):
            libtcod.console_set_foreground_color(con, self.color)
            libtcod.console_put_char(con, self.x, self.y, self.char, libtcod.BKGND_NONE)
 
    def clear(self, con):
        #erase the character that represents this object
        libtcod.console_put_char(con, self.x, self.y, ' ', libtcod.BKGND_NONE)
