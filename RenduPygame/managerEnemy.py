import pygame
import random
from Enemy import Enemy


class managerEnemy:
    def __init__(self, resolution, mainCharacter):
        self.groupSprite = pygame.sprite.Group()
        self.bombGroup = pygame.sprite.Group()
        self.bombImg = pygame.image.load("assets/bomb.png")
        self.firstEnemy = pygame.image.load("assets/enemy/enemy.png")
        self.secondEnemy = pygame.image.load("assets/enemy/enemy2.png")
        self.listEnemy = [self.firstEnemy, self.secondEnemy]
        self.resolution = resolution
        self.mainCharacter = mainCharacter
        self.zone = (self.resolution[0] / 2 - 20, self.resolution[1] / 2 - 10)
        self.gameLevel = 1
        self.spawnEnemy(self.gameLevel)

    def drawEnemy(self, surface):
        self.groupSprite.draw(surface)
        self.bombGroup.draw(surface)

    def spawnEnemy(self, nbEnemy):
        for nbRandom in range(nbEnemy):
            enemy_img = random.choice(self.listEnemy)
            enemy = Enemy((400, 75 * nbRandom), self.mainCharacter.speed, enemy_img, self.bombImg, self.zone, self.resolution)
            self.groupSprite.add(enemy)

    def update(self):
        if len(self.groupSprite.sprites()) == 0:
            self.gameLevel += 1
            self.spawnEnemy(self.gameLevel)
        for enemy in self.groupSprite.sprites():
            bomb = enemy.pre_update(self.mainCharacter)
            if bomb:
                self.bombGroup.add(bomb)
        self.groupSprite.update()
        self.bombGroup.update()
