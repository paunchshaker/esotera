import libtcodpy as libtcod
class BasicMonsterAI:
    def take_turn(self,player, map, fov_map):
        monster = self.owner
        if libtcod.map_is_in_fov(fov_map, monster.x, monster.y):
            if monster.distance_to(player) >= 2:
                monster.move_towards(map, player.x, player.y)
            elif player.phenotype.hp > 0:
                monster.phenotype.attack(player)
