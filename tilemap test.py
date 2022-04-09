import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Test Map")
clock = pygame.time.Clock()



o = pygame.image.load("ocean_tile.png")
l = pygame.image.load("land_tile.png")

def tile_map():
    map = [
    [l,o,o,o],
    [o,l,l,o],
    [o,l,l,o],
    [o,o,o,o]
    ]

    xcor = 0
    ycor = 0

    for i in map:
            for a in i:
                if a == o:
                    screen.blit(o,(xcor,ycor))
                    xcor+=100
                else:
                    screen.blit(l,(xcor,ycor))
                    xcor+=100
            xcor = 0
            ycor += 100

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tile_map()
            
    pygame.display.update()
    clock.tick(60)


