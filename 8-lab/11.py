import pygame
import sys
import random
import time

pygame.init()

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
gold = (255, 215, 0)

# Экран
width, height = 680, 700
speed = 5
score = 0
coins_collected = 0
game_over_screen = False

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
button_font = pygame.font.SysFont("Verdana", 25)
game_over_text = font.render("Game Over", True, black)

background = pygame.image.load("back.png")

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer Game")

clock = pygame.time.Clock()

# Полосы движения
lanes = [68, 210, 340, 470, 640]

# Кнопки
restart_button = pygame.Rect(220, 400, 100, 50)
exit_button = pygame.Rect(370, 400, 100, 50)


# --- Классы ---
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("enemy.png")
        self.image = pygame.transform.scale(self.image, (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.choice(lanes), 0)

    def move(self):
        global score
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            score += 1
            self.rect.top = 0
            self.rect.center = (random.choice(lanes), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("player.png")
        self.image = pygame.transform.scale(self.image, (100, 130))
        self.rect = self.image.get_rect()
        self.current_lane = 3
        self.rect.center = (lanes[self.current_lane], 600)

    def move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.move_ip(0, -7)
        if keys[pygame.K_DOWN] and self.rect.bottom < height:
            self.rect.move_ip(0, 7)
            
        if keys[pygame.K_LEFT] and self.current_lane > 0:
            self.current_lane -= 1
            self.rect.centerx = lanes[self.current_lane]
            pygame.time.delay(150)
        if keys[pygame.K_RIGHT] and self.current_lane < len(lanes) - 1:
            self.current_lane += 1
            self.rect.centerx = lanes[self.current_lane]
            pygame.time.delay(150)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.spawn()  # Начальная позиция в средней полосе

    def spawn(self):
        self.rect.center = (random.choice([68, 210, 340, 470, 640]), random.randint(100, 500))

    def move(self):
        self.rect.move_ip(0, speed)
        if self.rect.top > height:
            self.spawn()


# --- Функции ---
def restart_game():
    global speed, score, coins_collected, game_over_screen, EE, PP, coin, enemies, coins, all_sprites
    speed = 5
    score = 0
    coins_collected = 0
    game_over_screen = False

    EE = Enemy()
    PP = Player()
    coin = Coin()

    enemies = pygame.sprite.Group()
    enemies.add(EE)

    coins = pygame.sprite.Group()
    coins.add(coin)

    all_sprites = pygame.sprite.Group()
    all_sprites.add(PP)
    all_sprites.add(EE)
    all_sprites.add(coin)


def show_game_over():
    global game_over_screen
    game_over_screen = True

    screen.fill(red)
    screen.blit(game_over_text, (185, 250))

    pygame.draw.rect(screen, blue, restart_button)
    pygame.draw.rect(screen, black, exit_button)

    restart_text = button_font.render("Restart", True, white)
    exit_text = button_font.render("Exit", True, white)

    screen.blit(restart_text, (restart_button.x + 10, restart_button.y + 10))
    screen.blit(exit_text, (exit_button.x + 20, exit_button.y + 10))

    pygame.display.update()


# --- Главный цикл ---
restart_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart_game()
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and game_over_screen:
            if restart_button.collidepoint(event.pos):
                restart_game()
            if exit_button.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    if game_over_screen:
        continue

    screen.blit(background, (0, 0))

    scores = font_small.render(f"Score: {score} | Coins: {coins_collected}", True, black)
    screen.blit(scores, (10, 10))

    for obj in all_sprites:
        screen.blit(obj.image, obj.rect)
        obj.move()

    if pygame.sprite.spritecollideany(PP, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)
        show_game_over()

    pygame.display.update()
    clock.tick(60)
