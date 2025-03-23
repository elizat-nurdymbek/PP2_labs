import pygame
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music")
done = False
song_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(song_end)
pygame.mixer.music.load("sure_thing.mp3")

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                pygame.mixer.music.play()
            if event.key == pygame.K_2:
                pygame.mixer.music.play(-1)
            if event.key == pygame.K_3:
                pygame.mixer.music.pause()
            if event.key == pygame.K_4:
                pygame.mixer.music.unpause()
            if event.key == pygame.K_5:
                pygame.mixer.music.stop()
        
        if event.type == song_end:
            print("theee enddd!!!")
        
    screen.fill((255, 255, 255))       
    pygame.display.flip()