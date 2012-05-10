import libtcodpy as libtcod
from Object import Object
from Map import Map
from Dungeon import Dungeon

class Game:
    """The Esotera game engine"""
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    LIMIT_FPS = 20

    MAP_WIDTH = 80
    MAP_HEIGHT = 45

    FOV_ALGO = 0  #default FOV algorithm
    FOV_LIGHT_WALLS = True
    TORCH_RADIUS = 10

    def __init__(self,title):
        #set up a custom font
        libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

        #initialize the window
        libtcod.console_init_root(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT, title, False)
        #set up a buffer console to draw to
        self.con = libtcod.console_new(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT)
        libtcod.sys_set_fps(Game.LIMIT_FPS)
    
    def new_game(self):
        self.current_map = Dungeon(Game.MAP_WIDTH, Game.MAP_HEIGHT)

        #initialize the field of view
        self.fov_map = libtcod.map_new(Game.MAP_WIDTH, Game.MAP_HEIGHT)
        for y in range(Game.MAP_HEIGHT):
            for x in range(Game.MAP_WIDTH):
                libtcod.map_set_properties(self.fov_map, x, y, not self.current_map[x][y].block_sight, not self.current_map[x][y].blocked)
        self.fov_recompute = True

        self.player = Object(self.current_map.player_start_x, self.current_map.player_start_y, '@', libtcod.white)
        self.npc = Object(Game.SCREEN_WIDTH/2 - 5, Game.SCREEN_HEIGHT/2, '@', libtcod.yellow)
        self.game_objects = [self.player, self.npc]
        self.start()

    def start(self):
        while not libtcod.console_is_window_closed():
            self._render_all()
            libtcod.console_flush()
           
            for object in self.game_objects:
                object.clear(self.con)

            #handle user input
            exit = self._handle_keys()
            if exit:
                return

    def _render_all(self):
        for object in self.game_objects:
            object.draw(self.con, self.fov_map)

        if self.fov_recompute:
            #recompute FOV if needed (the player moved or something)
            self.fov_recompute = False
            libtcod.map_compute_fov(self.fov_map, self.player.x, self.player.y, Game.TORCH_RADIUS, Game.FOV_LIGHT_WALLS, Game.FOV_ALGO)

        #draw the map
        self.current_map.draw(self.con, self.fov_map)

        #blit the offscreen buffer
        libtcod.console_blit(self.con, 0, 0, Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT, 0, 0, 0)



    def _handle_keys(self):
        key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
        if key.vk == libtcod.KEY_ENTER and libtcod.KEY_ALT:
            #Alt+Enter: toggle fullscreen
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
        elif key.vk == libtcod.KEY_ESCAPE:
            return True
        
        #movement keys
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            self.player.move(self.current_map,0,-1)
            self.fov_recompute = True
 
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            self.player.move(self.current_map,0,1)
            self.fov_recompute = True
 
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            self.player.move(self.current_map,-1,0)
            self.fov_recompute = True
 
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            self.player.move(self.current_map,1,0)
            self.fov_recompute = True

