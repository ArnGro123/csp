import pygame, sys

pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Test Map")
clock = pygame.time.Clock()

o = pygame.image.load("ocean_tile.png")
l = pygame.image.load("land_tile.png")

p_x = 200
p_y = 0

scroll = [0,0]

map = [
[l,l,l,l,l],
[o,o,o,o],
[o,o,o,o],
[o,o,o,o],
[o,o,o,o],
[o,o,o,o],
[o,o,o,o],
[o,o,o,o],
[l,l,l,l]
]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    player = pygame.image.load("player_ship.png")
    player.convert_alpha(screen)
    player_rect = player.get_rect()

    screen.blit(player, (p_x,p_y))

    keys = pygame.key.get_pressed()

    for i in map:
            for a in i:
                if a == o:
                    screen.blit(o,(scroll[0],scroll[1]))
                    scroll[0]+=100
                else:
                    screen.blit(l,(scroll[0],scroll[1]))
                    scroll[0]+=100
            scroll[0] = 0
            scroll[1] += 100

    if keys[pygame.K_DOWN] :#and p_y < 400:
        print("down")
        p_y += 1
        scroll[1] -= 1
        print(scroll[1])
    
    if keys[pygame.K_UP] and p_y > 0:
        print("up")
        p_y -= 1
        scroll[1] += 1

    pygame.display.update()
    clock.tick(60)


