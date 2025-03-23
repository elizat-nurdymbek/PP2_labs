import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Changee: ")

colors = {
    pygame.K_r: (255, 0, 0),    # Красный при нажатии "R"
    pygame.K_g: (0, 255, 0),    # Зелёный при нажатии "G"
    pygame.K_b: (0, 0, 255),    # Синий при нажатии "B"
    pygame.K_y: (255, 255, 0)   # Жёлтый при нажатии "Y"
}

current_color = (0, 0, 0)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        if event.type == pygame.KEYDOWN:
            if event.key in colors:
                current_color = colors[event.key]
                
    screen.fill(current_color)
    
    pygame.display.flip()