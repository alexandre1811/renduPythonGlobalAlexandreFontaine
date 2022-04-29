import pygame
import time

from Bomb import *


class mainCharacter(pygame.sprite.Sprite):
    def __init__(self, positionCharacter, speedCharacter, imgCharacter, imgBomb):
        self.explosionChannel = pygame.mixer.Channel(0)
        self.bombChanel = pygame.mixer.Channel(1)
        self.explosionSound = pygame.mixer.Sound("assets/sounds/explosion.ogg")
        self.bombSound = pygame.mixer.Sound("assets/sounds/bomb.mp3")
        pygame.sprite.Sprite.__init__(self)
        self.bombImg = imgBomb
        self.bombTimer = 0.2
        self.timeStart = 0
        self.fireAuth = True
        self.pos = positionCharacter
        self.speed = speedCharacter
        self.speedAngle = 5
        self.scale = 1.5
        self.rotation = 0
        self.direction = pygame.math.Vector2(0, 1)
        self.originImage = imgCharacter
        self.image = imgCharacter
        self.rect = self.image.get_rect()

    def Move(self, x_axis, y_axis):
        rotationDelta = x_axis * self.speedAngle
        self.rotation -= rotationDelta
        vector = pygame.math.Vector2(0, 1)
        vector.y = y_axis * self.speed
        vector.rotate_ip(-self.rotation)
        self.direction.rotate_ip(rotationDelta)
        self.direction.normalize_ip()
        self.pos = (self.pos[0] + vector.x, self.pos[1] + vector.y)

    def Fire(self):
        if self.fireAuth:
            self.fireAuth = False
            self.bombChanel.play(self.bombSound)
            self.timeStart = time.time()
            return Bomb(self.pos, (self.direction.x, self.direction.y), 15, self.bombImg)

    def explosionSoundPlay(self):
        self.explosionChannel.play(self.explosionSound)

    def update(self):
        self.image = pygame.transform.rotozoom(self.originImage, self.rotation, self.scale)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        if time.time() - self.timeStart >= self.bombTimer:
            self.fireAuth = True
