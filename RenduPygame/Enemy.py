import pygame
from math import cos, sin, pi
import random
import time
from mainCharacter import *


class Enemy(mainCharacter):
    def __init__(self, posEnemy, speedEnemy, imgEnemy, bombImg, ellipse, res):
        mainCharacter.__init__(self, posEnemy, speedEnemy, imgEnemy, bombImg)
        self.res = res
        self.ellipse_origin = ellipse
        self.ellipse = self.ellipse_origin
        self.ellipse_speed = 0.015
        self.time = random.random() * 100
        self.clockwise = False
        self.rangeFireTimer = [1.2, 1.5]
        self.startFireTimer = time.time()
        self.fireTimer = self.timerCalculator(self.rangeFireTimer)
        self.reverseRangeTimer = [2.5, 5]
        self.startReverseTimer = time.time()
        self.reverseTimer = self.timerCalculator(self.reverseRangeTimer)

    def timeIncrease(self):
        if self.clockwise:
            self.time += self.ellipse_speed
        else:
            self.time -= self.ellipse_speed
    
    def ellipseCalculator(self, aEllipse, bEllipse, tEllipse):
        return self.res[0] / 2 + aEllipse * cos(tEllipse), self.res[1] / 2 + bEllipse * sin(tEllipse)
    
    def pre_update(self, player):
        direction = pygame.math.Vector2(self.pos[0] - player.pos[0], self.pos[1] - player.pos[1]).normalize()
        self.rotation = direction.angle_to(pygame.math.Vector2(0, -1))
        self.direction = pygame.math.Vector2(float(direction.x), float(direction.y))
        self.timeIncrease()
        self.pos = self.ellipseCalculator(self.ellipse[0], self.ellipse[1], self.time)
        if time.time() - self.startReverseTimer >= self.reverseTimer:
            self.startReverseTimer = time.time()
            self.reverseTimer = self.timerCalculator(self.reverseRangeTimer)
            self.clockwise = not self.clockwise
        if time.time() - self.startFireTimer >= self.fireTimer:
            self.startFireTimer = time.time()
            self.fireTimer = self.timerCalculator(self.rangeFireTimer)
            return self.Fire()
        else:
            return None

    def timerCalculator(self, L):
        return random.random() * (L[1] - L[0]) + L[0]
