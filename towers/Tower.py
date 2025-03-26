import pygame
import math
from utils import DamageType


class Tower:
    def __init__(self, attack_speed: float, damage_type: DamageType, demage: int):
        self.attack_speed = attack_speed
        self.damage_type: DamageType = damage_type
        self.attack_damage = demage
        self.rect = pygame.Rect(100,250,10,10)
        self.image = pygame.image.load("towers/assets/tower_assets/small_tower.png")
        self.range = 40
        self.cooldown = 0.2
        self.projectiles = []

    def display(self, screen):
        screen.blit(self.image, self.rect)

    def place(self, x, y):
        self.rect = pygame.rect(x, y, 10, 10)

    def attack(self, monsters):
        count = []
        for monster in monsters:
            count.append(math.sqrt(
                (monster.rect.center[0] - self.rect.center[0]) ** 2 + (monster.rect.center[1] - self.rect.center[1]) ** 2))
        count_smallest = count.index(min(count))
        self.projectiles.append(monsters[count_smallest])
        return monsters[count_smallest]
