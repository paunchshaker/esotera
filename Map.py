import libtcodpy as libtcod

class Rect:
#a rectangle on the map.
    def __init__(self, x, y, w, h):
        self.x1 = x
        self.y1 = y
        self.x2 = x + w
        self.y2 = y + h

    def center(self):
        center_x = (self.x1 + self.x2) / 2
        center_y = (self.y1 + self.y2) / 2
        return (center_x, center_y)
 
    def intersect(self, other):
        #returns true if this rectangle intersects with another one
        return (self.x1 <= other.x2 and self.x2 >= other.x1 and
                self.y1 <= other.y2 and self.y2 >= other.y1)

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
    color_light_wall = libtcod.Color(130, 110, 50)
    color_dark_ground = libtcod.Color(50, 50, 150)
    color_light_ground = libtcod.Color(200, 180, 50)

    
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tile = [[ Tile(True)
            for y in range(height) ]
                for x in range(width) ]

    def __getitem__(self, key):
        #alias to allow the map to act like an array...I hope
        return self.tile[key]


    def draw(self, con, fov_map):
        for y in range(self.height):
            for x in range(self.width):
                wall = self[x][y].block_sight
                visible = libtcod.map_is_in_fov(fov_map, x, y)
                if not visible:
                    #it's out of the field of view
                    if wall:
                        libtcod.console_set_back(con, x, y, Map.color_dark_wall, libtcod.BKGND_SET )
                    else:
                        libtcod.console_set_back(con, x, y, Map.color_dark_ground, libtcod.BKGND_SET )
                else:
                    #it's visible
                    if wall:
                        libtcod.console_set_back(con, x, y, Map.color_light_wall, libtcod.BKGND_SET )
                    else:
                        libtcod.console_set_back(con, x, y, Map.color_light_ground, libtcod.BKGND_SET )


