import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    
    radius = 15 # Толщина линии (начальный размер)
    x = 0 # # Позиция курсора X (не используется в коде)
    y = 0
    mode = 'blue' #  текущий цвет
    points = [] # список точек, через которые проходит линия.
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held: # Ctrl + W
                    return
                if event.key == pygame.K_F4 and alt_held: # Alt + F4
                    return
                if event.key == pygame.K_ESCAPE: # ESC
                    return
# Если нажали Ctrl + W, Alt + F4 или Esc – игра тоже закрывается.
                if event.key == pygame.K_r:
                    mode = 'red'
                if event.key == pygame.K_g:
                    mode = 'green'
                if event.key == pygame.K_b:
                    mode = 'blue'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Левая кнопка мыши – увеличивает толщину
                    radius = min(200, radius + 1) # увеличивает толщину (но не больше 200).
                elif event.button == 3: # Правая кнопка мыши – уменьшает толщину
                    radius = max(1, radius - 1) #  уменьшает толщину (но не меньше 1).
                    
            if event.type == pygame.MOUSEMOTION: # Если мышка двигается
                position = event.pos  # Берём координаты курсора
                points = points + [position]  # Добавляем в список точек
                points = points[-256:]  # Ограничиваем список до 256 точек
                
        screen.fill((0, 0, 0))
        
        i = 0
        while i < len(points) - 1:
            drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
            
        pygame.display.flip()
        
        clock.tick(60)
# Перебираем список точек и рисуем линии между соседними точками.   
    
def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'blue':
        color = (c1, c1, c2)
    elif color_mode == 'red':
        color = (c2, c1, c1)  # Оттенки красного
    elif color_mode == 'green':
        color = (c1, c2, c1)  # Оттенки зелёного
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1-progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width) 
main() 
    
    