import pygame
pygame.init()
screen = pygame.display.set_mode((400,400),pygame.RESIZABLE)
pygame.display.set_caption('My first image/sprite!')
bird_image = pygame.image.load('Bird.jpg')
bird_image = bird_image.convert()
player_image = pygame.transform.scale(bird_image,(200,200))
player_rect = player_image.get_rect(center=(400,300))
running = True
while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    screen.blit(player_image,player_rect)
    pygame.display.flip()
pygame.quit()