import pygame
import sys # Для выхода из программы
from pygame.locals import *  # использовать функции и переменные в модуле pygame.locals без необходимости добавлять длинный префикс pygame.locals. K_LEFT, K_RIGHT
import random, time

pygame.init() # инициализирует движок pygame

black = pygame.Color(0, 0, 0)        
white = pygame.Color(255, 255, 255)  
grey = pygame.Color(128, 128, 128) 
red = pygame.Color(255, 0, 0)
blue = pygame.Color(0, 0, 255) 

shirina, vysoto = 680, 700
speed = 5
score = 0
coins_collected = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

background = pygame.image.load("back.png")

screen = pygame.display.set_mode((shirina, vysoto))
screen.fill((white))
pygame.display.set_caption("Racer Game by Elya")

clock = pygame.time.Clock()

paused = False
game_over_screen = False

restart_button = pygame.Rect(200, 400, 120, 50)
exit_button = pygame.Rect(400, 400, 120, 50)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(5, shirina - 5), 0)
        
    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > vysoto:
            score += 1
            self.rect.top = 0
            lanes = [68, 210, 340, 470, 640]
            self.rect.center = (random.choice(lanes), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (100, 130))
        self.rect = self.image.get_rect()
        self.lanes = [68, 210, 340, 475, 630]
        self.current_lane = 3
        self.rect.center = (self.lanes[self.current_lane], 600)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if pressed_keys[K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -7)
        if pressed_keys[K_DOWN] and self.rect.bottom < vysoto:
            self.rect.move_ip(0,7)
            
        if pressed_keys[K_LEFT] and self.current_lane > 0:
            self.current_lane -= 1
            self.rect.centerx = self.lanes[self.current_lane]
            pygame.time.delay(150)
        if pressed_keys[K_RIGHT] and self.current_lane < len(self.lanes) - 1:
            self.current_lane += 1
            self.rect.centerx = self.lanes[self.current_lane]
            pygame.time.delay(150)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.spawn()
    
    def spawn(self):
        self.rect.center = (random.choice([68, 210, 340, 470, 640]), random.randint(100, 500))
    
    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > vysoto:
            self.spawn()


def restart_game():
    global speed, score, coins_collected, EE, PP, enemies, coins, all_sprites, game_over_screen
    speed = 5
    score = 0
    coins_collected = 0
    game_over_screen = False
    
    EE = Enemy()
    PP = Player()  
    CC = Coin()
    
    enemies = pygame.sprite.Group()
    enemies.add(EE)
    
    coins = pygame.sprite.Group()
    coins.add(CC)
    
    all_sprites = pygame.sprite.Group()
    all_sprites.add(PP)
    all_sprites.add(EE)  
    all_sprites.add(CC)              
           
def game_over_screen_display():
    screen.fill(red)
    text = font.render("Game Over", True, black)
    screen.blit(text, (shirina // 2 - 150, 250))

    pygame.draw.rect(screen, blue, restart_button)
    pygame.draw.rect(screen, black, exit_button)

    restart_text = font_small.render("RESET", True, white)
    exit_text = font_small.render("EXIT", True, white)

    screen.blit(restart_text, (restart_button.x + 30, restart_button.y + 10))
    screen.blit(exit_text, (exit_button.x + 40, exit_button.y + 10))

    pygame.display.update()          
                           
restart_game()            
            
action = pygame.USEREVENT + 1
pygame.time.set_timer(action, 1000)

while True:
    for event in pygame.event.get():
        if event.type == action:
            speed += 0.4
            
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if game_over_screen:
            if event.type == pygame.KEYDOWN:
                if event.key == K_r:
                    restart_game()
                if event.key == K_e:
                    pygame.quit()
                    sys.exit()
            continue

        if event.type == pygame.MOUSEBUTTONDOWN:
            if restart_button.collidepoint(event.pos):
                restart_game()
            if exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                restart_game()
            if event.key == K_p:
                paused = not paused
                    
    if game_over_screen:
        game_over_screen_display()
        continue
    
    screen.blit(background, (0,0))
    scores = font_small.render(f"Score: {score}  Coins: {coins_collected}", True, black)
    screen.blit(scores, (10, 10))
    
    for object in all_sprites:
        screen.blit(object.image, object.rect)
        object.move()  
        
    if pygame.sprite.spritecollideany(PP, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        game_over_screen = True
        
    if pygame.sprite.spritecollideany(PP, coins):
        coins_collected += 1
        for coin in coins:
            coin.spawn()
    
    pygame.display.update()
    clock.tick(60)
