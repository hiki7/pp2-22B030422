import pygame 
import datetime
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800, 550))
pygame.display.set_caption("Micky Clock")
clock = pygame.time.Clock()

back_surf = pygame.image.load('tsis7/1/graphics/clock.jpg').convert_alpha()
back_surf = pygame.transform.scale(back_surf, (800, 550))

left_h = pygame.image.load('tsis7/1/graphics/left.png').convert_alpha()
left_h_rect = left_h.get_rect(center = (380, 275))
right_h = pygame.image.load('tsis7/1/graphics/right.png').convert_alpha()
right_h_rect = right_h.get_rect(center = (420, 275))

current_time = datetime.datetime.now()
second = current_time.second
minute = current_time.minute

angle1 = 0 - (second * 6)
angle2 = 0 - (minute * 6) 

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(back_surf, (0, 0))
    right_h_copy = pygame.transform.rotate(right_h, angle1)
    left_h_copy = pygame.transform.rotate(left_h, angle2)

    left_h_copy_rect = left_h_copy.get_rect()
    left_h_copy_rect.center = left_h_rect.center

    right_h_copy_rect = right_h_copy.get_rect()
    right_h_copy_rect.center = right_h_rect.center



    screen.blit(right_h_copy, right_h_copy_rect)

    if((angle1-6) % 360) == 0:
        angle2 -= 6
        screen.blit(left_h_copy, left_h_copy_rect)
    else:
        screen.blit(left_h_copy, left_h_copy_rect)

    angle1 -= 6

    pygame.display.update()
    clock.tick(1)