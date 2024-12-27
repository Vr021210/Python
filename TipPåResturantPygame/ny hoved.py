import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((960, 540))
pygame.display.set_caption('Tip på Restaurant')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font\Times New Roman.ttf', 50)

background_surface = pygame.image.load('graphics\\background.jpg')
Text_Tip_På_Resturant_surface = test_font.render('Tip På Resturant', True, 'Red')

snail_surface = pygame.image.load('graphics\snail1.png')
snail_x_pos = 400
snail_rect = snail_surface.get_rect(midbottom = (snail_x_pos, 310))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            pygame.quit()
            exit()  

    screen.blit(background_surface, (0, 0))
    screen.blit(Text_Tip_På_Resturant_surface, (330, 50))
    snail_x_pos -=0
    screen.blit(snail_surface, (snail_x_pos, 310))
    
    if snail_x_pos <= 0:
        snail_x_pos = 960

    pygame.display.update()
    clock.tick(60)
