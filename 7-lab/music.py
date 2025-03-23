import pygame
import os

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Music Player by Elya")

playlist_folder = "music/"
album = "elya.png"
icon = pygame.image.load("icon.png")

pygame.display.set_icon(icon)

playlist = [f for f in os.listdir(playlist_folder) if f.endswith(".mp3")]
current_music = 0

photo = pygame.image.load(album)
photo = pygame.transform.scale(photo, (170, 170))

font = pygame.font.SysFont("AriComic Sans MSal", 30)
artist_font = pygame.font.SysFont("AriComic Sans MSal", 20)

photo_rect = pygame.Rect(55, 40, 200, 200)
text_rect = pygame.Rect(40, 50, 500, 250)
button_rect = pygame.Rect(40, 200, 500, 100)

play_button = pygame.Rect(375, 215, 50, 50)
next_button = pygame.Rect(450, 220, 40, 40)
prev_button = pygame.Rect(310, 220, 40, 40)

playing = False
rotation_angle = 0

def play_music():
    global playing
    pygame.mixer.music.load(os.path.join(playlist_folder, playlist[current_music]))
    pygame.mixer.music.play()
    playing = True
    
def stop_music():
    global playing
    pygame.mixer.music.stop()
    playing = False

def next_music():
    global current_music, rotation_angle
    current_music = (current_music + 1) % len(playlist)
    rotation_angle = 0
    play_music()
    
def prev_music():
    global current_music, rotation_angle
    current_music = (current_music - 1) % len(playlist)
    rotation_angle = 0
    play_music()


shart = False

while not shart:
    screen.fill((200, 230, 230))
    
    pygame.draw.rect(screen, (95, 158, 160), text_rect)
    pygame.draw.rect(screen, (50, 100, 100), button_rect)
    pygame.draw.rect(screen, (240, 255, 240), photo_rect)
    
    if playing:
        rotation_angle = (rotation_angle - 0.1) % 360
        rotated_cover = pygame.transform.rotozoom(photo, rotation_angle, 1)
        new_rect = rotated_cover.get_rect(center=photo_rect.center)
        screen.blit(rotated_cover, new_rect.topleft)
    else:
        screen.blit(photo, (photo_rect.x + 10, photo_rect.y + 10))
    
    track_name, _ = os.path.splitext(playlist[current_music])  

    if " - " in track_name:
        artist, title = track_name.split(" - ", 1)
    else:
        artist, title = "Неизвестный", track_name 

    name_music = font.render(title, True, (0, 0, 0))  
    screen.blit(name_music, (text_rect.x + 250, text_rect.y + 50)) 
    
    artist_name = artist_font.render(artist, True, (50, 50, 50))
    screen.blit(artist_name, (text_rect.x + 250, text_rect.y + 80)) 
    
    pygame.draw.rect(screen, (240, 255, 240), play_button)
    pygame.draw.rect(screen, (240, 255, 240), next_button)
    pygame.draw.rect(screen, (240, 255, 240), prev_button)
    
    screen.blit(font.render("*" if not playing else "||", True, (0, 0, 0)), (395, 235))
    screen.blit(font.render(">>", True, (0, 0, 0)), (460, 230))
    screen.blit(font.render("<<", True, (0, 0, 0)), (320, 230))
    
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shart = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.collidepoint(event.pos):
                if playing:
                    stop_music()
                else:
                    play_music()
            elif next_button.collidepoint(event.pos):
                next_music()
            elif prev_button.collidepoint(event.pos):
                prev_music()
            
pygame.quit()          
            
            