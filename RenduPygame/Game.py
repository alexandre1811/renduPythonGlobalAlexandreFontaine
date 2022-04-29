import pygame
from pygame.locals import *
import time
from mainCharacter import *
from managerEnemy import managerEnemy
from Text import *
pygame.mixer.init()


class Game:
    def __init__(self, res):
        self.res = res
        self.bordsBomb = [[-30, self.res[0] + 30], [-30, self.res[1] + 30]]
        self.bordsCharacter = [[20, self.res[0] - 20], [20, self.res[1] - 20]]
        self.windowTitle = "Rendu Pygame Alexandre Fontaine"
        self.gameRunning = True
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("assets/backgroundOcean.png")
        self.imgMainCharacter = pygame.image.load("assets/boat.png")
        self.imgBomb = pygame.image.load("assets/bomb.png")
        self.mainCharacter = mainCharacter((self.res[0] / 2, self.res[1] / 2), 10, self.imgMainCharacter, self.imgBomb)
        self.groupCharacterBomb = pygame.sprite.Group()
        self.managerEnemy = managerEnemy(self.res, self.mainCharacter)
        self.score = 0
        self.scoreFontSize = 40
        self.scoreTextPosistion = (self.res[0] / 2, 30)
        self.timerGameover = 2
        self.startGameoverTimer = 0
        self.Start()

    def Start(self):
        pygame.init()
        self.screen = pygame.display.set_mode(self.res)
        pygame.display.set_caption(self.windowTitle)
        self.Run()

    def Run(self):
        while self.gameRunning:
            for evt in pygame.event.get():
                self.manageEvenement(evt)
            self.pressedKeysManage()
            self.update()
        self.Quit()

    def manageEvenement(self, evenement):
        if evenement.type == QUIT:
            self.gameRunning = False
        if evenement.type == KEYDOWN:
            if evenement.key == K_SPACE:
                bomb = self.mainCharacter.Fire()
                if bomb:
                    self.groupCharacterBomb.add(bomb)

    def pressedKeysManage(self):
        pressedKey = pygame.key.get_pressed()
        vector = [0, 0]
        if pressedKey[K_q] or pressedKey[K_LEFT]:
            vector[0] -= 1
        if pressedKey[K_d] or pressedKey[K_RIGHT]:
            vector[0] += 1
        if pressedKey[K_z] or pressedKey[K_UP]:
            vector[1] -= 1
        if pressedKey[K_s] or pressedKey[K_DOWN]:
            vector[1] += 1
        self.mainCharacter.Move(vector[0], vector[1])
        if self.mainCharacter.pos[0] < self.bordsCharacter[0][0]:
            self.mainCharacter.pos = (self.bordsCharacter[0][0], self.mainCharacter.pos[1])
        elif self.mainCharacter.pos[0] > self.bordsCharacter[0][1]:
            self.mainCharacter.pos = (self.bordsCharacter[0][1], self.mainCharacter.pos[1])
        if self.mainCharacter.pos[1] < self.bordsCharacter[1][0]:
            self.mainCharacter.pos = (self.mainCharacter.pos[0], self.bordsCharacter[1][0])
        elif self.mainCharacter.pos[1] > self.bordsCharacter[1][1]:
            self.mainCharacter.pos = (self.mainCharacter.pos[0], self.bordsCharacter[1][1])

    def Draw(self):
        self.screen.blit(self.mainCharacter.image, self.mainCharacter.rect)
        self.managerEnemy.drawEnemy(self.screen)
        self.groupCharacterBomb.draw(self.screen)
    
    def collisionManage(self):
        for enemy in self.managerEnemy.groupSprite.sprites():
            for bomb in pygame.sprite.spritecollide(enemy, self.groupCharacterBomb, False):
                enemy.kill()
                bomb.kill()
                enemy.explosionSoundPlay()
                del enemy
                del bomb
                self.score += 1
        for bomb in pygame.sprite.spritecollide(self.mainCharacter, self.managerEnemy.bombGroup, False):
            bomb.kill()
            self.mainCharacter.explosionSoundPlay()
            del bomb
            del self.mainCharacter
            self.Gameover()

    def scoreMenu(self):
        textShow("Score : " + str(self.score), self.scoreFontSize, pygame.Color(255, 255, 255, 255), self.screen, self.scoreTextPosistion)

    def bombClear(self, group):
        for bomb in group.sprites():
            if bomb.rect.centerx < self.bordsBomb[0][0] or bomb.rect.centerx > self.bordsBomb[0][1]:
                group.remove(bomb)
            if bomb.rect.centery < self.bordsBomb[1][0] or bomb.rect.centery > self.bordsBomb[1][1]:
                group.remove(bomb)
            if bomb not in group.sprites():
                del bomb

    def update(self):
        self.screen.blit(self.background, (0, 0))
        self.bombClear(self.groupCharacterBomb)
        self.bombClear(self.managerEnemy.bombGroup)
        self.mainCharacter.update()
        self.groupCharacterBomb.update()
        self.managerEnemy.update()
        self.Draw()
        self.scoreMenu()
        self.collisionManage()
        self.clock.tick(50)
        pygame.display.update()
    
    def Gameover(self):
        self.startGameoverTimer = time.time()
        while time.time() - self.startGameoverTimer < self.timerGameover:
            self.screen.fill(pygame.Color(0, 0, 0, 255))
            textShow("Game Over !!!", 70, pygame.Color(255, 0, 0, 255), self.screen, (self.res[0] / 2, self.res[1] / 2))
            pygame.display.update()
        self.Quit()
    
    def Quit(self):
        pygame.display.quit()
        pygame.quit()
        del self
        quit()