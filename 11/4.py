import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("IMAGES: ")

surface = pygame.Surface((100, 100))
surface.fill((255, 0, 0))

running = True
angle = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
            
    screen.fill((255, 255, 255))
    rotatee = pygame.transform.rotate(surface, angle)
    screen.blit(rotatee, (100, 100))
    angle += 1
            
    pygame.display.flip()