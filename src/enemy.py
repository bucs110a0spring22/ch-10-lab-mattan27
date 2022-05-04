import pygame
import random
#model
class Enemy(pygame.sprite.Sprite, pygame.inflate.Rect):
    def __init__(self, name, x, y, img_file):
      '''
      Sets variables for different images and coordinates
      '''
        #initialize all the Sprite functionality
        pygame.sprite.Sprite.__init__(self)

        #The following two attributes must be called image and rect
        #pygame assumes you have intitialized these values
        #and uses them to update the screen

        #create surface object image
        self.image = pygame.image.load(img_file).convert_alpha()
        #get the rectangle for positioning
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #set other attributes
        self.name = name + str(id(self))
        self.speed = 2

    def update(self):
      """
      Updates the enemies to move one unit randomly throughout the window and chaning the speed
      """
      changeCor = random.randrange(-1,2)
      self.rect.x += changeCor
      self.rect.y += changeCor

      changeSpeed = random.randrange(-2,2)
      self.speed += changeSpeed
      self.speed += changeSpeed