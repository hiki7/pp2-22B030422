import pygame
from sys import exit


def play_music():
    global current_song, paused
    if not paused:
        pygame.mixer.music.load(current_song)
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song, music_index, paused
    
    music_index += 1
    if music_index > len(music_col) - 1:
        music_index = 0
        current_song = music_col[music_index]
        play_music()
    else:
        current_song = music_col[music_index]
        play_music()
  

def prev_music():
    global current_song, music_index, paused
    music_index -= 1
    if music_index < 0:
        music_index = 0
        current_song = music_col[music_index]
        play_music()
    else:
        current_song = music_col[music_index]
        play_music()
   

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Music player")
clock = pygame.time.Clock()


play_surf = pygame.image.load('tsis7/2/graphics/play-button.png').convert_alpha()
play_surf = pygame.transform.rotozoom(play_surf, 0, 0.1)
play_rect = play_surf.get_rect(midbottom = (350, 350))

pause_surf = pygame.image.load('tsis7/2/graphics/pause.png').convert_alpha()
pause_surf = pygame.transform.rotozoom(pause_surf, 0, 0.1)
pause_rect = pause_surf.get_rect(midbottom = (420, 350))

prev_surf = pygame.image.load('tsis7/2/graphics/previous.png').convert_alpha()
prev_surf = pygame.transform.rotozoom(prev_surf, 0, 0.1)
prev_rect = prev_surf.get_rect(midbottom = (280, 350))

next_surf = pygame.image.load('tsis7/2/graphics/next-button.png').convert_alpha()
next_surf = pygame.transform.rotozoom(next_surf, 0, 0.1)
next_rect = next_surf.get_rect(midbottom = (500, 350))

music_1 = 'tsis7/2/audio/first.mp3'
music_2 = 'tsis7/2/audio/second.mp3'

music_col = [music_1, music_2]
music_index = 0
current_song = music_col[music_index]
paused = False

image = pygame.image.load('tsis7/2/graphics/lofi.jpg')
image = pygame.transform.scale(image, (500, 280))
image_rect = image.get_rect(center = (400, 140))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and play_rect.collidepoint(event.pos):
            play_music()
        
        if event.type == pygame.MOUSEBUTTONDOWN and pause_rect.collidepoint(event.pos):
            pause_music()
        
        if event.type == pygame.MOUSEBUTTONDOWN and next_rect.collidepoint(event.pos):
            next_music()

        if event.type == pygame.MOUSEBUTTONDOWN and prev_rect.collidepoint(event.pos):
            prev_music()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                prev_music()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                play_music()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_y:
                pause_music()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                next_music()

    screen.fill('#7f6e54')
    screen.blit(image, image_rect)
    pygame.draw.line(screen, 'Black', (0, 280), (800, 280), width=3)
    screen.blit(play_surf, play_rect)
    screen.blit(pause_surf, pause_rect)
    screen.blit(prev_surf, prev_rect)
    screen.blit(next_surf, next_rect)
    
    

    clock.tick(30)
    pygame.display.update()

