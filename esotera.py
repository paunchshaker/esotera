import libtcodpy as libtcod
from Player import Player

class Game:
    """The Esotera game engine"""
    SCREEN_WIDTH = 80
    SCREEN_HEIGHT = 50
    LIMIT_FPS = 20

    def __init__(self,title):
        #set up a custom font
        libtcod.console_set_custom_font('arial10x10.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)

        #initialize the window
        libtcod.console_init_root(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT, title, False)
        #set up a buffer console to draw to
        self.con = libtcod.console_new(Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT)
        libtcod.sys_set_fps(Game.LIMIT_FPS)
    
    def new_game(self):
        self.player = Player(Game.SCREEN_WIDTH/2, Game.SCREEN_HEIGHT/2)
        self.start()

    def start(self):
        while not libtcod.console_is_window_closed():
            libtcod.console_set_foreground_color(self.con, libtcod.white)

            libtcod.console_print_left(self.con, self.player.x, self.player.y, libtcod.BKGND_NONE, '@')
            
            #blit the offscreen buffer
            libtcod.console_blit(self.con, 0, 0, Game.SCREEN_WIDTH, Game.SCREEN_HEIGHT, 0, 0, 0)
            libtcod.console_flush()
           
            #clear player character
            libtcod.console_print_left(self.con, self.player.x, self.player.y, libtcod.BKGND_NONE, ' ')
            #handle user input
            exit = self._handle_keys()
            if exit:
                return


    def _handle_keys(self):
        key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
        if key.vk == libtcod.KEY_ENTER and libtcod.KEY_ALT:
            #Alt+Enter: toggle fullscreen
            libtcod.console_set_fullscreen(not libtcod.console_is_fullscreen())
 
        elif key.vk == libtcod.KEY_ESCAPE:
            return True
        
        #movement keys
        if libtcod.console_is_key_pressed(libtcod.KEY_UP):
            self.player.y -= 1
 
        elif libtcod.console_is_key_pressed(libtcod.KEY_DOWN):
            self.player.y += 1
 
        elif libtcod.console_is_key_pressed(libtcod.KEY_LEFT):
            self.player.x -= 1
 
        elif libtcod.console_is_key_pressed(libtcod.KEY_RIGHT):
            self.player.x += 1


#Start the game here
esotera = Game('Esotera Demo')
esotera.new_game()


