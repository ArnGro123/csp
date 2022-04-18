import pygame, sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Test Map")
font = pygame.font.SysFont("Calibri", 30)
clock = pygame.time.Clock()

o = pygame.image.load("ocean_tile.png")
l = pygame.image.load("land_tile.png")

scroll = [0,0]

def start_map():

    start_map = [
    [l,l,l,l],
    [l,o,o,l],
    [l,o,o,l],
    [l,l,l,l]
    ]

    map_x = 0
    map_y = 0

    for i in start_map:
        for a in i:
            if a == o:
                screen.blit(o,(map_x,map_y))
                map_x += 100
            else:
                screen.blit(l,(map_x,map_y))
                map_x += 100
            map_x = 0
            map_y += 100

def game_map():
    
    game_map = [
    [l,l,l,l],
    [o,o,o,o],
    [o,o,o,o],
    [o,o,o,o],
    [o,o,o,o],
    [o,o,o,o],
    [o,o,o,o],
    [o,o,o,o],
    [l,l,l,l]
    ]

    map_x = scroll[0]
    map_y = scroll[1]
    
    for i in game_map:
            for a in i:
                if a == o:
                    screen.blit(o,(map_x,map_y))
                    map_x += 100
                else:
                    screen.blit(l,(map_x,map_y))
                    map_x += 100
            map_x = 0
            map_y += 100


player = pygame.image.load("player_ship.png")
player.convert_alpha(screen)
player_rect = player.get_rect()

start_button = pygame.image.load("start_button.png")
start_button.convert_alpha(screen)
start_button_rect = start_button.get_rect()

z = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if start_button_rect.collidepoint(pos):
                z = 1

    if z == 0:

        start_map()
        
        screen.blit(start_button,(0,0))
        start_button_rect.topleft = (0,0)

        txt_surface = font.render("START",False,(0,0,0))
        screen.blit(txt_surface,(20,25))

    elif z == 1:

        game_map()

        screen.blit(player,(150,100))
        player_rect.topleft = (150,100)

        keys = pygame.key.get_pressed()

        if keys[pygame.K_DOWN] :
            print("down")
            scroll[1] -= 1
        
        if keys[pygame.K_UP]:
            print("up")
            scroll[1] += 1

    pygame.display.update()
    clock.tick(60)


