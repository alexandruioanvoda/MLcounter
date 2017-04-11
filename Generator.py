import pygame
from random import randint

#initializing the screen on which the images are created
pygame.init()
screen = pygame.display.set_mode((300,300))

#function for checking intersection
def isIntersecting(x,y):
    for coordinate in coordinates:
        if x-15 < coordinate[0]+15 and x+15 > coordinate[0]-15:
            if y-15 < coordinate[1]+15 and y+15 > coordinate[1]-15:
                return True
    return False

image_count = int(input("How many images do you want?"))

while image_count > 0:
    screen.fill((255,255,255))

    #initialize the random number of circs
    no = randint(2,10)
    #list of coordinates for each circs
    coordinates=[[0,0]]

    for i in range(no):
        #make sure coordinates don't intersect with any circ before
        x=randint(30, 270)
        y=randint(30, 270)
        while (isIntersecting(x,y)):
            x=randint(30, 270)
            y=randint(30, 270)

        pygame.draw.circle(screen, (0,0,255), (x, y), 15, 0)
        coordinates.append([x,y])
        pygame.display.update()

    print()
    print(no)

    print(coordinates[1][1])
    input()

    image_count-=1
