import pygame
import random
import sys

pygame.init()
pygame.mixer.init()

shirina, vysoto = 700,700
screen = pygame.display.set_mode((shirina, vysoto))
pygame.display.set_caption("Snack Game by Elya")
clock = pygame.time.Clock()

font = pygame.font.SysFont('Arial', 40)

white = (256, 256, 256)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

#Snake Settings
snake_pos = [300, 200] # Начальная позиция головы змейки (x=300, y=200)
snake_body = [[100, 50], [90, 50], [80, 50]] # Тело змейки (список сегментов)
snake_direction = 'RIGHT' # Начальное направление движения змейки
change_to = snake_direction # Переменная для смены направления
speed = 15 # Скорость змейки (чем больше, тем быстрее)

#Food Settings
food_pos = [random.randrange(1, (shirina // 10)) * 10, random.randrange(1, (vysoto // 10)) * 10] # Генерируем случайную позицию еды
food_swapn = True

game_score = 0

shart = True
while shart:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shart = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != "DOWN":
                change_to = "UP"
            if event.key == pygame.K_DOWN and snake_direction != "UP":
                change_to = "DOWN"
            if event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                change_to = "RIGHT"
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                change_to = "LEFT"
                
    #Move Snake based on Direction
    snake_direction = change_to
    if snake_direction == "UP":
        snake_pos[1] -= 10
    if snake_direction == "DOWN":
        snake_pos[1] += 10
    if snake_direction == "RIGHT":
        snake_pos[0] += 10
    if snake_direction == "LEFT":
        snake_pos[0] -= 10
        
    #Insert New Position
    snake_body.insert(0, list(snake_pos))
    
    #Check if Food is Eaten
    if snake_pos == food_pos:
        food_swapn = False
        game_score += 1
    else:
        snake_body.pop()
        
    if not food_swapn:
        food_pos = [random.randrange(1, (shirina // 10)) * 10, random.randrange(1, (vysoto // 10)) * 10]
        food_swapn = True
        
    #Check for Collision with Walls
    if snake_pos[0] < 0 or snake_pos[0] >= shirina or snake_pos[1] < 0 or snake_pos[1] >= vysoto:
        shart = False
        
    #Check for Collision with Itself
    for block in snake_body[1:]:
        if snake_pos == block:
            shart = False
            
    #Update Screen
    screen.fill(black)
    for p in snake_body:
        pygame.draw.rect(screen, green, pygame.Rect(p[0], p[1], 10, 10))
    pygame.draw.rect(screen, red, pygame.Rect(food_pos[0], food_pos[1], 10, 10))
    
    game_score_text = font.render(f"Score: {game_score}",True,'white')
    screen.blit(game_score_text,(20,20))
    pygame.display.update()
 
    pygame.display.flip()
    clock.tick(speed) 
    
 
game_over_text = font.render("GAME OVER", True, 'white')
game_over_rectangle = game_over_text.get_rect()
game_over_rectangle.center = (shirina / 2, vysoto / 2)
screen.blit(game_over_text,game_over_rectangle)
pygame.display.update()
pygame.time.wait(4000)
pygame.mixer          




