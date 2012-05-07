import libtcodpy as libtcod

class Tile:
    #a tile of the map and its properties
    def __init__(self, blocked, block_sight = None):
        self.blocked = blocked
 
        #by default, if a tile is blocked, it also blocks sight
        if block_sight is None: block_sight = blocked
        self.block_sight = block_sight

class Map:
    #define colors here. Seems silly.
    color_dark_wall = libtcod.Color(0, 0, 100)
    color_dark_ground = libtcod.Color(50, 50, 150)
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile = [[ Tile(False)
            for y in range(height) ]
                for x in range(width) ]

        
        #test code
        self.tile[30][22].blocked = True
        self.tile[30][22].block_sight = True
        self.tile[50][22].blocked = True
        self.tile[50][22].block_sight = True

    def __getitem__(self, key):
        #alias to allow the map to act like an array...I hope
        return self.tile[key]


    def draw(self, con):
        for y in range(self.height):
            for x in range(self.width):
                wall = self[x][y].block_sight
                if wall:
                    libtcod.console_set_back(con, x, y, Map.color_dark_wall, libtcod.BKGND_SET )
                else:
                    libtcod.console_set_back(con, x, y, Map.color_dark_ground, libtcod.BKGND_SET )
