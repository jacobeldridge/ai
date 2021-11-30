
import pygame
from pygame.constants import SRCALPHA
import constants
from constants import ZEROX, ZEROY
import math



vec = pygame.math.Vector2
class Static(pygame.sprite.Sprite):
    def __init__(self, shape, static_w = None, static_h = None, circlex=None, circley=None, radius=None):
        pygame.sprite.Sprite.__init__(self)
        if shape == "rect":
            self.image = pygame.Surface((static_w, static_h))
            self.image.fill(constants.WHITE)
            self.rect = self.image.get_rect()
            self.rect.center = (constants.WIDTH / 2, constants.HEIGHT / 2)
        if shape == "circle":
            self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
            pygame.draw.circle(self.image, constants.GREEN, (radius, radius), radius)
            self.position = vec(circlex, circley)
            self.rect = self.image.get_rect(center=self.position)
        else:

            return None

        
class Lines(pygame.sprite.Sprite):
    def __init__(self, color, radius, startposx, startposy, trajectory_angle):
        #create obj
        self.placesivebeen = []
        pygame.sprite.Sprite.__init__(self)
        self.listofstatic = list()
        self.color = color
        self.radius = radius
        self.angle = math.radians(trajectory_angle)
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.position = vec(startposx, startposy)
        self.placesivebeen.append(self.position)
        self.rect = self.image.get_rect(center=self.position)
        
        #create static to be left

    def move(self):
        
        # newstatic = Static(shape="circle", circlex=self.position[0], circley=self.position[1], radius=self.radius)
        # self.listofstatic.append(newstatic)
        self.position += (math.cos(self.angle)/constants.K, math.sin(self.angle)/constants.K)
        
        self.rect.center = self.position
        self.placesivebeen.append(self.position)


            





