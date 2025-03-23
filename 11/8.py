import pygame
import math
import time

def create_background(width, height):         #create chess desk
    colors = [(255, 255, 255), (0, 0, 0)]  #white and grey
    background = pygame.Surface((width, height))  # Создаём поверхность (холст)
    tile_width = 50 # Размер одной плитки
    y = 0 #начинаем рисовать с верхней границы  (рядами сверху вниз).
    while y < height: # продолжаем, пока не дойдём до нижней границы (height).
        x = 0 #начинаем с левого края.
        while x < width: #идём справа налево по строке.
            row = y // tile_width # номер строки (по y).  Если y = 40, то row = 40 // 20 = 2
            col = x // tile_width # Деление на tile_width переводит пиксели в номер клетки.
            pygame.draw.rect(background, 
                             colors[(row + col) % 2], #Чередует белый и серый цвета.
                             pygame.Rect(x, y, tile_width, tile_width))
            x += tile_width # Сдвигаемся вправо # x увеличивается на 20 пикселей.
        y += tile_width #После завершения строки (while x < width) увеличивает y на 20.
    return background

def try_to_quit(event):
    pressed_keys = pygame.key.get_pressed() # Получаем информацию о всех клавишах, которые в данный момент нажаты.
    alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT] # Проверяем, нажата ли клавиша Alt
    x_bulton = event.type == pygame.QUIT #Проверяем, кликнул ли пользователь по кнопке "Закрыть" (❌) в окне игры.
    altF4 = alt_pressed and event.type == pygame.KEYDOWN and event.key == pygame.K_F4 # Проверяем, нажал ли игрок Alt + F4:
    escape = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE #  Проверяем, нажал ли игрок клавишу Escape (Esc).
    return x_bulton or altF4 or escape

#Функция возвращает True, если любое из условий выполнено:

# x_button → кликнули по "крестику".
# altF4 → нажали Alt + F4.
# escape → нажали Esc.

def run_demos(width, height, fps):
    pygame.init()
    screen = pygame.display.set_mode((width, height)) # Создаём окно
    pygame.display.set_caption("pygame by elya") # Заголовок окна
    background = create_background(width, height) # Фон
    clock = pygame.time.Clock() # Часы для контроля FPS
    demos = [   # Хранит список функций, каждая из которых рисует разные фигуры.
        do_rectangle_demo,
        do_circle_demo,
        do_horrible_outlines,
        do_nice_outlines,
        do_polygon_demo,
        do_line_demo
    ]
    the_word_happy_place = 0 # Счётчик времени
    while True:
        the_word_happy_place += 1
        for event in pygame.event.get():
            if try_to_quit(event):
                return # Закрываем программу
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                demos = demos[1:] # Убираем текущую демонстрацию и переходим к следующей
        
        screen.blit(background, (0, 0)) # Рисуем фон
        if len(demos) == 0:
            return # Если демки закончились — выйти
        demos[0](screen, the_word_happy_place) # Запускаем текущую демку
        pygame.display.flip() # Обновляем экран
        clock.tick(fps) # Ограничиваем FPS
        
def do_rectangle_demo(surface, counter):
    left = (counter // 3) % surface.get_width() # (движение влево-вправо).
    top = (counter // 3) % surface.get_height() # Это делает движение немного плавнее.
    #  % (Остаток от деления) → гарантирует, что left всегда остаётся в пределах экрана.
    # Когда left становится больше ширины экрана, он сбрасывается в 0, и движение начинается заново.
    width = 50
    height = 50
    color = (128, 0, 128)
    pygame.draw.rect(surface, color, pygame.Rect(left, top, width, height))

def do_circle_demo(surface, counter):
    x = surface. get_width() // 2 # круг будет находиться в центре экрана.
    y = surface. get_height() // 2 # y = 500 // 2 = 250
    max_radius = min(x, y) * 4 // 5  # выбираем наименьшее из двух значений (ширина или высота).
    # Умножаем на 4/5, чтобы радиус был не больше 80% экрана
    radius = abs(int(math.sin(counter * 3.14159 * 2/ 500) * max_radius)) + 1
    # Деление на 200 делает так, чтобы полный цикл занимал 200 кадров.
    # math.sin(...) создаёт пульсирующий эффект (от -1 до 1).
    # Умножение на max_radius делает так, чтобы круг менялся от 0 до 120 пикселей.
    # abs() делает отрицательные значения положительными (чтобы радиус всегда был больше 0).
    # +1 гарантирует, что круг никогда не будет невидимым (минимум 1 пиксель).
    color = (0, 140, 255)
    pygame.draw.circle(surface, color, (x, y), radius)

def do_horrible_outlines(surface, counter):
    color = (255, 0, 0)
    pygame.draw.rect(surface, color, pygame.Rect(10,10,100,100), 10)
    pygame.draw.circle(surface, color, (300, 60), 50, 10)
    
def do_nice_outlines(surface, counter):
    color = (0, 128, 0)  # Зелёный
    pygame.draw.rect(surface, color, pygame.Rect(10, 10, 100, 10))
    pygame.draw.rect(surface, color, pygame.Rect(10, 10, 10, 100))
    pygame.draw.rect(surface, color, pygame.Rect(100, 10, 10, 100))
    pygame.draw.rect(surface, color, pygame.Rect(10, 100, 100, 10))
    
def do_polygon_demo(surface, counter):
    color = (255, 255, 0)
    num_points = 8  # Количество "углов" у звезды
    point_list = []  # список, куда мы будем записывать точки.
    center_x = surface.get_width() // 2  # Координата X центра экрана
    center_y = surface.get_height() // 2 # Задаём центр экрана (center_x, center_y), чтобы рисовать от него.
    for i in range(num_points * 2):  # Мы удваиваем количество точек (num_points * 2), потому что:
        radius = 150
        if i % 2 == 0:   # Чётные точки → ближе к центру (короткие лучи).
            radius = radius // 2    # Нечётные точки → дальше от центра (длинные лучи)
        ang = i * 3.14159 / num_points + counter * 3.14159 / 60  # находим угол для каждой точки.
        x = center_x + int(math.cos(ang) * radius)  # sin(ang) * radius — переводим угол в координаты (x, y).
        y = center_y + int(math.sin(ang) * radius)
        point_list.append((x, y))  # Добавляем точки в point_list
    pygame.draw.polygon(surface, color, point_list)

def rotate_3d_points(points, angle_x, angle_y, angle_z):
        new_points = []
        for point in points:
                x = point[0]
                y = point[1]
                z = point[2]
                new_y = y * math.cos(angle_x) - z * math.sin(angle_x)
                new_z = y * math.sin(angle_x) + z * math.cos(angle_x)
                y = new_y
                # isn't math fun, kids? 
                z = new_z
                new_x = x * math.cos(angle_y) - z * math.sin(angle_y)
                new_z = x * math.sin(angle_y) + z * math.cos(angle_y)
                x = new_x
                z = new_z
                new_x = x * math.cos(angle_z) - y * math.sin(angle_z)
                new_y = x * math.sin(angle_z) + y * math.cos(angle_z)
                x = new_x
                y = new_y
                new_points.append([x, y, z])
        return new_points

def do_line_demo(surface, counter):
        color = (0, 0, 0) # black 
        cube_points = [
                [-1, -1, 1],
                [-1, 1, 1],
                [1, 1, 1],
                [1, -1, 1],
                [-1, -1, -1],
                [-1, 1, -1],
                [1, 1, -1],
                [1, -1, -1]]
                
        connections = [
                (0, 1),
                (1, 2),
                (2, 3),
                (3, 0),
                (4, 5),
                (5, 6),
                (6, 7),
                (7, 4),
                (0, 4),
                (1, 5),
                (2, 6),
                (3, 7)
                ]
                
        t = counter * 2 * 3.14159 / 60 # this angle is 1 rotation per second 
        
        # rotate about x axis every 2 seconds 
        # rotate about y axis every 4 seconds 
        # rotate about z axis every 6 seconds 
        points = rotate_3d_points(cube_points, t / 2, t / 4, t / 6)
        flattened_points = []
        for point in points:
                flattened_points.append(
                        (point[0] * (1 + 1.0 / (point[2] + 3)),
                         point[1] * (1 + 1.0 / (point[2] + 3))))
        
        for con in connections:
                p1 = flattened_points[con[0]]
                p2 = flattened_points[con[1]]
                x1 = p1[0] * 60 + 200
                y1 = p1[1] * 60 + 150
                x2 = p2[0] * 60 + 200
                y2 = p2[1] * 60 + 150
                
                # This is the only line that really matters 
                pygame.draw.line(surface, color, (x1, y1), (x2, y2), 4)
                
        


run_demos(400, 300, 60)