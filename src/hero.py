import pygame
import random
#model
class Hero(pygame.sprite.Sprite):
    def __init__(self, name, x, y, img_file):
    '''
    Defines different variables for the hero.
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
        self.name = name
        self.speed = 3
        self.health = 3

    #methods to make moving our hero easier
    def move_up(self):
      """
      sets variable for the hero to move upwards.
      """
        self.rect.y -= self.speed
    def move_down(self):
      """
      sets variable for hero to move downwards
      """
        self.rect.y += self.speed
    def move_left(self):
      """
      sets variable for hero to move to the left
      """
        self.rect.x -= self.speed
    def move_right(self):
      """
      sets variable to move hero to the right
      """
        self.rect.x += self.speed

    def fight(self, opponent):
      """
      Sets result of what happens when the hero and enemy collide. Prints statement as to whether or not the hero succeeds or fails in an attack.
      """
        if(random.randrange(3)):
            self.health -= 1
            print("attack failed. Remaining Health: ", self.health)
            return False
        else:
            print("successful attack")
        return True
