#30  -  50
#50p
import pygame, sys
pygame.init()

TILESIZE = 50
MAPX = 22
MAPY = 11

DISPLAYSURF = pygame.display.set_mode((MAPX*TILESIZE, MAPY*TILESIZE))


BLACK = (0,0,0)
WHITE = (255, 255, 255)

WALL = "#"
GROUND = " "


colours ={
        WALL : BLACK,
        GROUND : WHITE
         }


map1 =   """######################
            #                    #
            #        #           #
            #        #           #
            #        #           #
            ####### ##############
            #                    #
            #                    #
            #                    #
            #                    #
            ######################"""





def init(map_nr):
    if map_nr == 1:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for row in range(MAPX):
                print("jouab")
                for column in range(MAPY):
                    print("jouab2")
                    pygame.draw.rect(DISPLAYSURF, colours[map1[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
        
            pygame.display.update()
init(1)
