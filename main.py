import pygame, sys

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Test Map")
font = pygame.font.SysFont("Calibri", 30)
clock = pygame.time.Clock()

player = pygame.image.load("player_ship.png")
player.convert_alpha(screen)
player_rect = player.get_rect()

enemy = pygame.image.load("enemy_ship.png")
enemy.convert_alpha(screen)
enemy_rect = enemy.get_rect()

start_button = pygame.image.load("start_button.png")
start_button.convert_alpha(screen)
start_button_rect = start_button.get_rect()

o = pygame.image.load("ocean_tile.png")
o = pygame.transform.smoothscale(o,(100,100))
l = pygame.image.load("land_tile.png")
l = pygame.transform.smoothscale(l,(100,100))

game_map = [
    [o,o,o,o,o,o],
    [o,o,o,o,o,o],
    [l,l,l,l,l,l],
    ]

scroll = [0,400]
p_x = 250
p_y = 250

def start_screen():

    start_map = [
    [l,l,l,l,l,l],
    [l,o,o,o,o,l],
    [l,o,o,o,o,l],
    [l,o,o,o,o,l],
    [l,o,o,o,o,l],
    [l,l,l,l,l,l],
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


def game_screen():

    game_map.reverse()

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
            map_y -= 100

def healthbar():
    
    pygame.draw.rect(screen,"red",pygame.Rect(10,10,200,30))
    pygame.draw.rect(screen,"white",pygame.Rect(10,10,200,34),4)

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

        start_screen()

        screen.blit(start_button,(225,320))
        start_button_rect.topleft = (225,320)

        txt_surface = font.render("START",False,(0,0,0))
        screen.blit(txt_surface,(260,340))

    elif z == 1:

        game_screen()

        game_map.insert(0,[o,o,o,o,o,o])

        healthbar()

        screen.blit(player,(p_x,p_y))
        player_rect.topleft = (p_x,p_y)

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            scroll[1] += 2
            game_map.insert(0,[o,o,o,o,o,o])

        if keys[pygame.K_RIGHT] and p_x<600:
            p_x += 1
        
        if keys[pygame.K_LEFT] and p_x>0:
            p_x -= 1


    pygame.display.update()
    clock.tick(60)

