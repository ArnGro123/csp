import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Test Map")
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)


map_texture = {
    0 = pygame.image.load("ocean image")
    1 = pygame.image.load("grass image")
}

map = [
[0,0,0,0],
[0,1,1,0],
[0,1,1,0],
[0,0,0,0]
]