import pygame


class Bomb(pygame.sprite.Sprite):
    def __init__(self, positionBomb, directionBomb, speedBomb, imgBomb):
        pygame.sprite.Sprite.__init__(self)
        self.pos = positionBomb
        self.direction = pygame.math.Vector2(directionBomb[0], directionBomb[1])
        self.speed = speedBomb
        self.img = imgBomb

        self.rotation = self.direction.angle_to(pygame.math.Vector2(0, 1))
        self.image = pygame.transform.rotate(self.img, self.rotation)
        self.rect = self.image.get_rect()

    def update(self):
        self.pos = (self.pos[0] - self.speed*self.direction[0], self.pos[1] - self.speed*self.direction[1])
        self.rect.center = self.pos