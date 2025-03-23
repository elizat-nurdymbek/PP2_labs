import pygame 
import random
pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music Random")
clock = pygame.time.Clock()

musics = ['die_with_smile.mp3', 'let_her_go.mp3', 'sure_thing.mp3']
current_song = None

song_end = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(song_end)
done = False

def next_song():
    global musics
    musics = musics[1:] + [musics[0]]
    pygame.mixer.music.load(musics[0])
    pygame.mixer.music.play()
    
next_song()

''''
def next_song():
    global current_song, musics
    next_song = random.choice(musics)
    while next_song == current_song:
        next_song = random.choice(musics)
    current_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()  
    
next_song()
 '''   
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                next_song()
            
    
    screen.fill((255, 255, 255))        
    pygame.display.flip()
    clock.tick(60)
    
pygame.quit()