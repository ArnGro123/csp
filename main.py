#TO-DO :  enemy spawn, healthbar, end screen

import pygame, sys, math, random as rand

pygame.init()
screen = pygame.display.set_mode((500,600))
pygame.display.set_caption("PyRate")
clock = pygame.time.Clock()

#initializing
l = pygame.image.load("land_tile.png").convert_alpha(screen)
l = pygame.transform.smoothscale(l,(100,100))
o = pygame.image.load("ocean_tile.png").convert_alpha(screen)
o = pygame.transform.smoothscale(o,(100,100))

large_font = pygame.font.SysFont("Calibri",100)
small_font = pygame.font.SysFont("Calibri", 30)

start_button = pygame.image.load("start_button.png").convert_alpha(screen)
start_rect = start_button.get_rect()

restart_button = pygame.image.load("restart_button.png").convert_alpha(screen)
restart_button = pygame.transform.smoothscale(restart_button,(300,100))
restart_rect = restart_button.get_rect()

scroll = [0,500]
screen_speed = 1
h_size = 200
score = 0

game_map = [
        [o,o,o,o,o],
        [o,o,o,o,o],
        [o,o,o,o,o],
        [o,o,o,o,o],
        [o,o,o,o,o],
        [l,l,l,l,l],
        ]

def start_screen():
    start_map = [
        [l,l,l,l,l],
        [l,o,o,o,l],
        [l,o,o,o,l],
        [l,o,o,o,l],
        [l,o,o,o,l],
        [l,l,l,l,l],
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

    title_surface = large_font.render("PyRate",False,(0,0,0))
    screen.blit(title_surface,(113,193))

    screen.blit(start_button,(176,320))
    start_rect.topleft = (176,320)
    start_surface = small_font.render("START",False,(0,0,0))
    screen.blit(start_surface,(210,342))

def game_screen():
    global screen_speed, score
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
    
    scroll[1] += screen_speed
    screen_speed += 0.001
    o_list = [o,o,o,o,o]
    game_map.insert(0,o_list)

    score_surface = small_font.render("SCORE : "+str(score),False,(255,255,255))
    screen.blit(score_surface,(315,14))

def healthbar():
    global h_size, z

    pygame.draw.rect(screen,"red",pygame.Rect(10,10,h_size,26.75))
    pygame.draw.rect(screen,"white",pygame.Rect(10,10,200,29),4)

    if player.rect.colliderect(enemy_1.enemy_rect) or player.rect.colliderect(enemy_2.enemy_rect) or player.rect.colliderect(enemy_3.enemy_rect) or player.rect.colliderect(enemy_4.enemy_rect):
        h_size -= 1

    if h_size == 0:
        z = 2

def end_screen():
    global z

    screen.fill("white")
    end_surface = large_font.render("GAME OVER",False,(0,0,0))
    screen.blit(end_surface,(0,150))

    end_score_surface = small_font.render("SCORE : "+str(score),False,(0,0,0))
    screen.blit(end_score_surface,(180,320))

    screen.blit(restart_button,(100,400))
    restart_rect.topleft = (100,400)
        

class Player(pygame.sprite.Sprite):

    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("player_ship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.x = 217
        self.y = 300

    def draw(self,screen):
        screen.blit(self.image, (self.x,self.y))
        self.rect.topleft = (self.x,self.y)
        
    def movement(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.y > 0:
            self.y -= 1
            self.rect.y -= 1
        
        if keys[pygame.K_DOWN] and self.y < 490:
            self.y += 1.5
            self.rect.y += 1.5

        if keys[pygame.K_RIGHT] and self.x<433:
            self.x += 1
            self.rect.x += 1
        
        if keys[pygame.K_LEFT] and self.x>0:
            self.x -= 1
            self.rect.x -= 1


class Enemy(pygame.sprite.Sprite):
    
    def __init__(self):

        super().__init__()

        self.image = pygame.image.load("enemy_ship.png").convert_alpha(screen)
        self.rotated_e = pygame.transform.rotate(self.image,180)
        self.enemy_rect = self.rotated_e.get_rect()
        self.rand_x = rand.randrange(10,450,50)
        self.y = 0
        self.enemy_speed = rand.randrange(2,4)

    def draw(self,screen):
        screen.blit(self.rotated_e,(self.rand_x,self.y))
        self.enemy_rect.topleft = (self.rand_x,self.y)
        self.y += self.enemy_speed
        self.enemy_speed += 0.001

        if self.y > 600:
            self.y = -20
            self.rand_x = rand.randrange(10,450,50)


z = 0
t = 0
player = Player()
enemy_1 = Enemy()
enemy_2 = Enemy()
enemy_3 = Enemy()
enemy_4 = Enemy()
e_l = [enemy_1,enemy_2,enemy_3,enemy_4]
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
for i in e_l:
    all_sprites.add(i)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if start_rect.collidepoint(pos):
                z = 1
            if restart_rect.collidepoint(pos):
                z = 1
                h_size = 200
                screen_speed = 1
                score = 0
                player.x = 217
                player.y = 300
                for i in e_l:
                    i.y = -20
                    i.enemy_speed = rand.randrange(2,4)
    
    all_sprites.update()
    
    if z == 0:
        start_screen()

    elif z == 1:
        game_screen()
        healthbar()

        player.draw(screen)
        player.movement()

        if t < 500:
            enemy_1.draw(screen)
            enemy_2.draw(screen)
        elif 500 < t < 2000:
            enemy_1.draw(screen)
            enemy_2.draw(screen)
            enemy_3.draw(screen)
        else:
            enemy_1.draw(screen)
            enemy_2.draw(screen)
            enemy_3.draw(screen)
            enemy_4.draw(screen)

        score += 1
        t += 1

    else:
        end_screen()
    
    pygame.display.update()
    clock.tick(60)

