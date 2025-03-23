import pygame
import sys # Для выхода из программы 
from pygame.locals import * # использовать функции и переменные в модуле pygame.locals без необходимости добавлять длинный префикс pygame.locals. K_LEFT, K_RIGHT
import random

pygame.init()  # инициализирует движок pygame. 

BLACK = pygame.Color(0, 0, 0)         # Black
WHITE = pygame.Color(255, 255, 255)   # White
GREY = pygame.Color(128, 128, 128)   # Grey
RED = pygame.Color(255, 0, 0) 

WIDTH, HEIGHT = 400, 600
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT)) #слева направо  # сверху вниз.
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

FPS = pygame.time.Clock()


class Enemy(pygame.sprite.Sprite): # спрайты Pygame. Это помогает работать с изображениями и движением.
    def __init__(self): # это конструктор, который создается при создании врага.
        super().__init__() # вызывает конструктор родительского класса (обязательная штука для работы со спрайтами).
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40), 0) # по горизонтали (X), от 40 до WIDTH - 40. #  0 по вертикали (Y) (
        
    def move(self):
        self.rect.move_ip(0, 10) # Двигаем врага вниз на 10 пикселей (0 по X, 10 по Y).
        if (self.rect.bottom > 600): # Если враг уходит за нижнюю границу
            self.rect.top = 0  # Появляется снова сверху
            self.rect.center = (random.randint(30, 370), 0)  # враг появится в случайном месте от 30 до 370 пикселей.
            
    def draw(self, surface):
        surface.blit(self.image, self.rect)  # Отображаем врага на экране

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
 
    def update(self):
        pressed_keys = pygame.key.get_pressed() # Проверяем нажатые клавиши
       #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)
       #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0,5)
         
        if self.rect.left > 0: # Если не у левой границы
              if pressed_keys[K_LEFT]: # Если нажата стрелка влево 
                  self.rect.move_ip(-5, 0) # Двигаем влево 
        if self.rect.right < WIDTH:        # Если не у правой границы
              if pressed_keys[K_RIGHT]:   # Если нажата стрелка вправо 
                  self.rect.move_ip(5, 0)
 
    def draw(self, surface):
        surface.blit(self.image, self.rect) 



P1 = Player()
E1 = Enemy()


#Game loop begins
while True:
    for event in pygame.event.get(): # "Event" Pygame происходит, когда пользователь выполняет определенное действие
        if event.type == pygame.QUIT: # Мы можем узнать, какие события произошли, вызвав функцию pygame.event.get() # Если нажали "Закрыть окно" 
            pygame.quit()   # Выходим из Pygame
            sys.exit() # Закрываем программу
    
    P1.update() # Обновляем позицию игрока
    E1.move() # Двигаем врага
     
    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)
    E1.draw(DISPLAYSURF)
    
    FPS.tick(60)
    pygame.display.update() # отвечает за обновление вашего игрового окна любыми изменениями

