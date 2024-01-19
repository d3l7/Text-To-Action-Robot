import pygame, sys

scween = pygame.display.set_mode((200, 200))

pygame.init()

sound = pygame.mixer.Sound('dink.wav')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            sound.play()