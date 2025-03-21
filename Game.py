

class Game:
    def __init__(self,monsters,towers,map):
        self.monsters=monsters
        self.towers=towers
        self.map = map
    def display(self,screen):
        for monster in self.monsters:
            monster.display(screen)
        for tower in self.towers:
            tower.display(screen)
        self.map.display(screen)
    def run(self):
        for tower in self.towers:
            tower.attack(self.monsters)
        for monster in self.monsters:
            monster.move(self.map.route[monster.counter])


