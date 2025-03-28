import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create a canvas for drawing
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))

# Settings
brush_size = 5  # Размер кисти
eraser_size = 10  # Размер ластика
mode = 'draw'  # 'draw', 'rect', 'circle', 'eraser'
color = (0, 0, 255)  # Синий по умолчанию
start_pos = None  # Начальная точка для фигур
drawing = False  # Флаг рисования
points = []  # Точки для свободного рисования

# Font
font = pygame.font.Font(None, 24) # # Шрифт для кнопок

def draw_ui():
    """Draws the UI (toolbar)(панель инструментов)"""
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 800, 90))  # Панель инструментов
    
    # # Color selection buttons
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 30, 30))  # Красный
    pygame.draw.rect(screen, (0, 255, 0), (50, 10, 30, 30))  # Зеленый
    pygame.draw.rect(screen, (0, 0, 255), (90, 10, 30, 30))  # Синий
    pygame.draw.rect(screen, (0, 0, 0), (130, 10, 30, 30))  # Черный
    pygame.draw.rect(screen, (255, 255, 255), (170, 10, 30, 30))  # Белый (ластик)
    
    # Tool selection buttons
    pygame.draw.rect(screen, (180, 180, 180), (220, 10, 80, 30))  # Карандаш
    pygame.draw.rect(screen, (180, 180, 180), (220, 50, 80, 30))  # Квадрат
    pygame.draw.rect(screen, (180, 180, 180), (310, 10, 80, 30))  # Прямоугольник
    pygame.draw.rect(screen, (180, 180, 180), (310, 50, 80, 30))  # Прямоугольный треугольник
    pygame.draw.rect(screen, (180, 180, 180), (400, 10, 80, 30))  # Круг
    pygame.draw.rect(screen, (180, 180, 180), (400, 50, 80, 30))  # Равносторонний треугольник
    pygame.draw.rect(screen, (180, 180, 180), (490, 10, 80, 30))  # Ластик
    pygame.draw.rect(screen, (180, 180, 180), (490, 50, 80, 30))  # Ромб
    pygame.draw.rect(screen, (255, 0, 0), (580, 10, 100, 30))  # Очистка

    # Brush and eraser size adjustment buttons
    pygame.draw.rect(screen, (100, 100, 100), (690, 10, 30, 30))  # Уменьшить
    pygame.draw.rect(screen, (100, 100, 100), (730, 10, 30, 30))  # Увеличить

    # Button labels
    screen.blit(font.render("Draw", True, (0, 0, 0)), (240, 15))
    screen.blit(font.render("Square", True, (0, 0, 0)), (230, 55))
    screen.blit(font.render("Rect", True, (0, 0, 0)), (330, 15))
    screen.blit(font.render("R-Tri", True, (0, 0, 0)), (330, 55))
    screen.blit(font.render("Circle", True, (0, 0, 0)), (415, 15))
    screen.blit(font.render("E-Tri", True, (0, 0, 0)), (420, 55))
    screen.blit(font.render("Eraser", True, (0, 0, 0)), (500, 15))
    screen.blit(font.render("Rhombus", True, (0, 0, 0)), (495, 55))
    screen.blit(font.render("Clear", True, (255, 255, 255)), (610, 15))
    screen.blit(font.render("-", True, (255, 255, 255)), (700, 15))  # Уменьшение размера
    screen.blit(font.render("+", True, (255, 255, 255)), (740, 15))  # Увеличение размера

while True:
    screen.blit(canvas, (0, 0))  # Display the saved drawing on the screen
    draw_ui() # Draw the user interface

    mouse_pos = pygame.mouse.get_pos()
    if drawing and start_pos and mode in ['rect', 'circle', 'square', 'r-tri', 'e-tri', 'rhombus']:
        temp_surface = canvas.copy()  # Create a copy of the canvas for shape preview
        if mode == 'rect': # Rectangle (preview)
            rect = pygame.Rect(*start_pos, mouse_pos[0] - start_pos[0], mouse_pos[1] - start_pos[1])
            pygame.draw.rect(temp_surface, color, rect, 2)
        elif mode == 'circle':  # Circle (preview)
            center = start_pos
            radius = int(((mouse_pos[0] - center[0]) ** 2 + (mouse_pos[1] - center[1]) ** 2) ** 0.5)
            pygame.draw.circle(temp_surface, color, center, radius, 2)
        elif mode == 'square':  # Square (preview)
            side = min(abs(mouse_pos[0] - start_pos[0]), abs(mouse_pos[1] - start_pos[1]))
            square_rect = pygame.Rect(start_pos[0], start_pos[1], side, side)
            pygame.draw.rect(temp_surface, color, square_rect, 2)
        elif mode == 'r-tri':  # Right triangle (preview)
            pygame.draw.polygon(temp_surface, color, [start_pos, (mouse_pos[0], start_pos[1]), (start_pos[0], mouse_pos[1])], 2)
        elif mode == 'e-tri':  # Equilateral triangle (preview)
            height = abs(mouse_pos[1] - start_pos[1])
            base = height * (3 ** 0.5) / 2
            pygame.draw.polygon(temp_surface, color, [start_pos, (start_pos[0] + base, start_pos[1]), ((start_pos[0] + start_pos[0] + base) // 2, start_pos[1] - height)], 2)
        elif mode == 'rhombus':  # Rhombus (preview)
            width = abs(mouse_pos[0] - start_pos[0])
            height = abs(mouse_pos[1] - start_pos[1])
            pygame.draw.polygon(temp_surface, color, [
                (start_pos[0], start_pos[1] - height // 2),
                (start_pos[0] + width // 2, start_pos[1]),
                (start_pos[0], start_pos[1] + height // 2),
                (start_pos[0] - width // 2, start_pos[1])
            ], 2)    
            
        screen.blit(temp_surface, (0, 0))  # Display the canvas with preview

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Handle button clicks
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < 50:
                # Color selection
                if 10 <= x <= 40:
                    color = (255, 0, 0)  # Красный
                elif 50 <= x <= 80:
                    color = (0, 255, 0)  # Зеленый
                elif 90 <= x <= 120:
                    color = (0, 0, 255)  # Синий
                elif 130 <= x <= 160:
                    color = (0, 0, 0)  # Черный
                elif 170 <= x <= 200:
                    color = (255, 255, 255)  # Белый (ластик)
                
                 # Tool selection
                elif 220 <= x <= 300:
                    mode = 'draw'
                elif 310 <= x <= 390:
                    mode = 'rect'
                elif 400 <= x <= 480:
                    mode = 'circle'
                elif 490 <= x <= 570:
                    mode = 'eraser'
                elif 580 <= x <= 680:
                    canvas.fill((255, 255, 255))# Очистка экрана
                    points.clear()
                    
            if 50 < y < 100: # Additional shape selection
                if 220 <= x <= 300:
                    mode = 'square'
                elif 310 <= x <= 390:
                    mode = 'r-tri'
                elif 400 <= x <= 480:
                    mode = 'e-tri'
                elif 490 <= x <= 570:
                    mode = 'rhombus'
                
                
                
                # Adjust brush and eraser size
                elif 690 <= x <= 720:
                    brush_size = max(1, brush_size - 1)
                    eraser_size = max(1, eraser_size - 1)
                elif 730 <= x <= 760:
                    brush_size = min(50, brush_size + 1)
                    eraser_size = min(50, eraser_size + 1)

            else:
                points.clear()
                start_pos = event.pos
                drawing = True

        # Draw shapes on mouse release
        if event.type == pygame.MOUSEBUTTONUP:
            if mode in ['rect', 'circle', 'square', 'r-tri', 'e-tri', 'rhombus'] and start_pos:
                end_pos = event.pos
                if mode == 'rect':
                    rect = pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    pygame.draw.rect(canvas, color, rect, 2)
                elif mode == 'circle':
                    center = start_pos
                    radius = int(((end_pos[0] - center[0]) ** 2 + (end_pos[1] - center[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, color, center, radius, 2)
                elif mode == 'square':
                    side = min(abs(end_pos[0] - start_pos[0]), abs(end_pos[1] - start_pos[1]))
                    pygame.draw.rect(canvas, color, (start_pos[0], start_pos[1], side, side), 2)
                elif mode == 'r-tri':  # Прямоугольный треугольник
                    pygame.draw.polygon(canvas, color, [start_pos, (end_pos[0], start_pos[1]), (start_pos[0], end_pos[1])], 2)
                elif mode == 'e-tri':  # Равносторонний треугольник
                    height = abs(end_pos[1] - start_pos[1])
                    base = height * 2 / (3 ** 0.5)
                    pygame.draw.polygon(canvas, color, [start_pos, (start_pos[0] + base, start_pos[1]), ((start_pos[0] + start_pos[0] + base) // 2, start_pos[1] - height)], 2)
                elif mode == 'rhombus':  # Ромб
                    width = abs(end_pos[0] - start_pos[0])
                    height = abs(end_pos[1] - start_pos[1])
                    pygame.draw.polygon(canvas, color, [
                        (start_pos[0], start_pos[1] - height // 2),
                        (start_pos[0] + width // 2, start_pos[1]),
                        (start_pos[0], start_pos[1] + height // 2),
                        (start_pos[0] - width // 2, start_pos[1])
                    ], 2)
                start_pos = None
            drawing = False


        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 'draw': # Drawing mode
                points.append(event.pos)  # Save mouse position
                if len(points) >= 2: # If two points, draw a line
                    pygame.draw.lines(canvas, color, False, points, brush_size)
                else:
                    points.append(event.pos) # Add point again

            elif mode == 'eraser': # Eraser mode
                pygame.draw.circle(canvas, (255, 255, 255), event.pos, eraser_size) # Erase with white color
    
    # Refresh screen and set speed
    pygame.display.flip()
    clock.tick(60)
