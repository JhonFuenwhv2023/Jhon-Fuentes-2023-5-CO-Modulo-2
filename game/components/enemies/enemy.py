import pygame, random

from pygame.sprite import Sprite
from game.utils.constants import ENEMY_1, ENEMY_2,  SCREEN_HEIGHT, SCREEN_WIDTH



class Enemy(Sprite):
    ENEMY_WIDTH = 40
    ENEMY_HEIGHT = 60
    X_POS_LIST  = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 1000]
    Y_POS = 20
    SPEED_ENEMY_1_X = 5
    SPEED_ENEMY_1_Y = 4
    MOV_X = { 0: 'left', 1: 'right' }
    SPEED_ENEMY_2_X = random.randint(5, 8)
    SPEED_ENEMY_2_Y = random.randint(6, 10)
    

    def __init__(self):
        # Variable to randomly assign turns between enemies.
        self.enemy_turn = random.choice(["enemy_1", "enemy_2"])

        '''I use a conditional statement to check which enemy the attributes belong to.'''

        # Attributes for enemy 1.
        if self.enemy_turn == "enemy_1":
            self.image=self._get_enemy_image(ENEMY_1)
            self.speed_x = self.SPEED_ENEMY_1_X
            self.speed_y = self.SPEED_ENEMY_1_Y

        # Attributes for enemy 2.
        else:
            self.image=self._get_enemy_image(ENEMY_2)
            self.speed_x = self.SPEED_ENEMY_2_X
            self.speed_y = self.SPEED_ENEMY_2_Y

        # Common attributes.
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS_LIST[random.randint(0, 11)]
        self.rect.y = self.Y_POS
        self.movement_x = self.MOV_X[random.randint(0, 1)]
        self.move_x_for = random.randint(30, 100)
        self.index = 0

        '''This method receives the image as a parameter
           and then resizes it to the required dimensions.'''
        
    def _get_enemy_image(self,image_file):
        image=pygame.transform.scale(image_file,
                                                (self.ENEMY_WIDTH,self.ENEMY_HEIGHT))
        return image

    def update(self, ships):
        self.rect.y += self.speed_y

        if self.movement_x == 'left':
            self.rect.x -= self.speed_x
            self.change_movement_x()
        else:
            self.rect.x += self.speed_x
            self.change_movement_x()
        
        if self.rect.y >= SCREEN_HEIGHT:
            ships.remove(self)

    def draw(self,screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def change_movement_x(self):
        self.index += 1
        if (self.index >= self.move_x_for and self.movement_x == 'right') or (self.rect.x >= SCREEN_WIDTH - self.ENEMY_WIDTH):
            self.movement_x = 'left'
            self.index = 0
        elif (self.index >= self.move_x_for and self.movement_x == 'left') or (self.rect.x <= 10):
            self.movement_x = 'right'
            self.index = 0

