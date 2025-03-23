import pygame

pygame.init()
shirina, vysota = 500, 500
screen = pygame.display.set_mode((shirina, vysota))
pygame.display.set_caption("Play Ball by Elya")

radius = 25
x, y = shirina // 2, vysota // 2
speed = 20

shart = True

while shart:
    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), radius)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shart = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x - radius - speed >= 0:
                x -= speed
            if event.key == pygame.K_RIGHT and x + radius + speed <= shirina:
                x += speed
            if event.key == pygame.K_UP and y - radius - speed >= 0:
                y -= speed
            if event.key == pygame.K_DOWN and y + radius + speed <= vysota:
                y += speed
                
    pygame.display.flip()
pygame.quit()