import pygame
import math
import time

import pygame
from pygame.rect import Rect

from utils import DamageType
from towers.Projectile import Projectile
import time


class Tower:
    def __init__(self, damage_type: DamageType):
        self.damage_type: DamageType = damage_type
        self.attack_damage = 2
        self.rect = Rect(100, 250, 10, 10)
        self.image = pygame.image.load("towers/assets/tower_assets/small_tower.png")
        self.range = 500
        self.cooldown = 0.2
        self.projectiles = []
        self.current_time = time.time()

    def display(self, screen):
        screen.blit(self.image, self.rect)
        for projectile in self.projectiles:
            projectile.display(screen)

    def place(self, x, y):
        self.rect = Rect(x, y, 10, 10)

    def attack(self, monsters: list):
        if time.time() >= self.current_time + self.cooldown:
            count = []
            for monster in monsters:
                count.append(math.sqrt(
                    (monster.rect.center[0] - self.rect.center[0]) ** 2 + (
                                monster.rect.center[1] - self.rect.center[1]) ** 2))
            if count:
                nearest_position = count.index(min(count))
                nearest_monster = count[count.index(min(count))]
                # nearest_monster = min(monsters, key=lambda monster: (monster.rect.center[0] - self.rect.center[0]) ** 2 + (monster.rect.center[1] - self.rect.center[1]) ** 2)))

                if nearest_monster <= self.range:
                    self.projectiles.append(Projectile(*self.rect.center, monsters[int(nearest_position)], 10, 50))
            self.projectiles = [projectile for projectile in self.projectiles if not projectile.hit]
            self.current_time = time.time()
        for projectile in self.projectiles:
            projectile.move()
