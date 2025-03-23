import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Создаем холст для рисования
canvas = pygame.Surface((800, 600))
canvas.fill((255, 255, 255))  # Белый фон

# Основные переменные
brush_size = 5  # Размер кисти
eraser_size = 10  # Размер ластика
mode = 'draw'  # 'draw', 'rect', 'circle', 'eraser'
color = (0, 0, 255)  # Синий по умолчанию
start_pos = None  # Начальная точка для фигур
drawing = False  # Флаг рисования
points = []  # Точки для свободного рисования

# Шрифт для кнопок
font = pygame.font.Font(None, 24)

def draw_ui():
    """Рисует UI (панель инструментов)"""
    pygame.draw.rect(screen, (200, 200, 200), (0, 0, 800, 50))  # Панель инструментов
    
    # Кнопки выбора цвета
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, 30, 30))  # Красный
    pygame.draw.rect(screen, (0, 255, 0), (50, 10, 30, 30))  # Зеленый
    pygame.draw.rect(screen, (0, 0, 255), (90, 10, 30, 30))  # Синий
    pygame.draw.rect(screen, (0, 0, 0), (130, 10, 30, 30))  # Черный
    pygame.draw.rect(screen, (255, 255, 255), (170, 10, 30, 30))  # Белый (ластик)
    
    # Кнопки инструментов
    pygame.draw.rect(screen, (180, 180, 180), (220, 10, 80, 30))  # Карандаш
    pygame.draw.rect(screen, (180, 180, 180), (310, 10, 80, 30))  # Прямоугольник
    pygame.draw.rect(screen, (180, 180, 180), (400, 10, 80, 30))  # Круг
    pygame.draw.rect(screen, (180, 180, 180), (490, 10, 80, 30))  # Ластик
    pygame.draw.rect(screen, (255, 0, 0), (580, 10, 100, 30))  # Очистка

    # Кнопки изменения размера кисти и ластика
    pygame.draw.rect(screen, (100, 100, 100), (690, 10, 30, 30))  # Уменьшить
    pygame.draw.rect(screen, (100, 100, 100), (730, 10, 30, 30))  # Увеличить

    # Текст на кнопках
    screen.blit(font.render("Draw", True, (0, 0, 0)), (240, 15))
    screen.blit(font.render("Rect", True, (0, 0, 0)), (330, 15))
    screen.blit(font.render("Circle", True, (0, 0, 0)), (415, 15))
    screen.blit(font.render("Eraser", True, (0, 0, 0)), (510, 15))
    screen.blit(font.render("Clear", True, (255, 255, 255)), (610, 15))
    screen.blit(font.render("-", True, (255, 255, 255)), (700, 15))  # Уменьшение размера
    screen.blit(font.render("+", True, (255, 255, 255)), (740, 15))  # Увеличение размера

while True:
    screen.blit(canvas, (0, 0))  # Отображаем сохраненный рисунок
    draw_ui()

    mouse_pos = pygame.mouse.get_pos()
    if drawing and start_pos and mode in ['rect', 'circle']:
        temp_surface = canvas.copy()  # Создаем копию холста для предпросмотра
        if mode == 'rect':
            rect = pygame.Rect(*start_pos, mouse_pos[0] - start_pos[0], mouse_pos[1] - start_pos[1])
            pygame.draw.rect(temp_surface, color, rect, 2)
        elif mode == 'circle':
            center = start_pos
            radius = int(((mouse_pos[0] - center[0]) ** 2 + (mouse_pos[1] - center[1]) ** 2) ** 0.5)
            pygame.draw.circle(temp_surface, color, center, radius, 2)
        screen.blit(temp_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        # Обработка кликов по кнопкам
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if y < 50:
                # Выбор цвета
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
                
                # Выбор инструмента
                elif 220 <= x <= 300:
                    mode = 'draw'
                elif 310 <= x <= 390:
                    mode = 'rect'
                elif 400 <= x <= 480:
                    mode = 'circle'
                elif 490 <= x <= 570:
                    mode = 'eraser'
                elif 580 <= x <= 680:
                    canvas.fill((255, 255, 255))  # Очистка экрана
                
                # Изменение размера кисти и ластика
                elif 690 <= x <= 720:
                    brush_size = max(1, brush_size - 1)
                    eraser_size = max(1, eraser_size - 1)
                elif 730 <= x <= 760:
                    brush_size = min(50, brush_size + 1)
                    eraser_size = min(50, eraser_size + 1)

            else:
                if mode in ['rect', 'circle']:
                    start_pos = event.pos
                    drawing = True
                else:
                    drawing = True
                    points = [event.pos]

        if event.type == pygame.MOUSEBUTTONUP:
            if mode in ['rect', 'circle'] and start_pos:
                end_pos = event.pos
                if mode == 'rect':
                    rect = pygame.Rect(*start_pos, end_pos[0] - start_pos[0], end_pos[1] - start_pos[1])
                    pygame.draw.rect(canvas, color, rect, 2)
                elif mode == 'circle':
                    center = start_pos
                    radius = int(((end_pos[0] - center[0]) ** 2 + (end_pos[1] - center[1]) ** 2) ** 0.5)
                    pygame.draw.circle(canvas, color, center, radius, 2)
                start_pos = None
            drawing = False

        if event.type == pygame.MOUSEMOTION and drawing:
            if mode == 'draw':
                points.append(event.pos)
                pygame.draw.lines(canvas, color, False, points, brush_size)
            elif mode == 'eraser':
                pygame.draw.circle(canvas, (255, 255, 255), event.pos, eraser_size)

    pygame.display.flip()
    clock.tick(60)
