# from ai.datacreate.objects import CenterLines
from pygame.draw import line
from objects import Lines
from objects import CenterLines
import pygame
import random
from objects import Static
import constants
from constants import ZEROX, ZEROY
import random
import math
import time

loopangle = 45
splitcheck = 0
colors = [constants.RED, constants.GREEN, constants.BLUE, constants.GOLD]
screen = pygame.display.set_mode((constants.WIDTH, constants.HEIGHT))
branches = [[],[],[],[]]
midlines = []
## initialize pygame and create window
pygame.init()
pygame.mixer.init()  ## For sound
vec = pygame.math.Vector2

pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()     ## For syncing the FPS


## group all the sprites together for ease of update
vector_sprites = pygame.sprite.Group()
static_sprites = pygame.sprite.Group()
branchessprites = [pygame.sprite.Group(),pygame.sprite.Group(),pygame.sprite.Group(),pygame.sprite.Group()]
starter = Static(shape="rect",static_w=20,static_h=20)

for i in range(4):
    
    branches[i-1].append(Lines(color=colors[i-1], radius=4, startposx=ZEROX, startposy=ZEROY, trajectory_angle=loopangle))
    loopangle += 90
    vector_sprites.add(branches[i-1][0])

## Game loop
running = True
# def collidecheck(branchnum):
    
#     minusgroup = branchessprites[:branchnum] + branchessprites[branchnum+1:]
#     collision = []
#     print("Minusgroup:{}".format(minusgroup))

#     collide = pygame.sprite.groupcollide(branches[branchnum], branchessprites[branchnum], dokilla=False, dokillb=False, collided = None)
#     print("collide:{}".format(len(collide)))
    



def startup():
    
    static_sprites.add(starter)
    static_sprites.draw(screen)
    


startup()
while running:
    
    #1 Process input/events
    clock.tick(constants.FPS)     ## will make the loop run at the same speed all the time
    for event in pygame.event.get():        # gets all the events which have occured till now and keeps tab of them.
        ## listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False
    


    

    vector_sprites.draw(screen)
    for lists in branches:
        whichbranch = branches.index(lists)
        for lines in lists:
            for x in lines.position:
                if x > 800:
                    running = False
                else:
                    pass
            # for statics in lines.listofstatic:
            #     branchessprites[whichbranch].add(statics)
            #     print(branchessprites[whichbranch])


            
            
            lines.move()
            newmidline = CenterLines(screen, lines.position, lines.lastposition)
            if newmidline.slope not in midlines:
                midlines.append(newmidline.slope)
            print(midlines)
            print(newmidline.slope)
            # static_sprites.add(lines.listofstatic[-1])
            # collidecheck(whichbranch)


         
    if splitcheck == 25:
        
        randomindex = random.randint(0,3)
        randomindex2 = random.randint(0,len(branches[randomindex])-1)
        splitcheck = 0
        newlist = []
        
        
        
        index = branches[randomindex].index(branches[randomindex][randomindex2])
        newangle1 = math.degrees(branches[randomindex][randomindex2].angle)-35
        newangle2 = math.degrees(branches[randomindex][randomindex2].angle)+35
        
        newlist.append(Lines(color=colors[randomindex], radius=4, startposx=branches[randomindex][randomindex2].position[0], startposy=branches[randomindex][randomindex2].position[1], trajectory_angle=newangle1))
        newlist.append(Lines(color=colors[randomindex], radius=4, startposx=branches[randomindex][randomindex2].position[0], startposy=branches[randomindex][randomindex2].position[1], trajectory_angle=newangle2))
        

        # branch_split_coords[randomindex].append(branches[randomindex][randomindex2].position)
        
        # pygame.draw.line(screen, constants.GOLD, branch_split_coords[randomindex][-1], branch_split_coords[randomindex][-2])
        for item in newlist:
            item.lastposition = branches[randomindex][randomindex2].position
            pygame.draw.line(screen, constants.GOLD, item.position, item.lastposition)
        
        branches[randomindex][randomindex2:randomindex2+1] = newlist
        vector_sprites.add(branches[randomindex][::1])


        

        
 
    ## Done after drawing everything to the screen
    pygame.display.update()
    pygame.display.flip()   
    splitcheck += 1    
    

pygame.quit()