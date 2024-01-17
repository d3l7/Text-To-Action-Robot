import pygame, time, sys

pygame.init()

scween = pygame.display.set_mode((50,50))

clock = pygame.time.Clock()

sfx = pygame.mixer.Sound('dink.wav')
play = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    scween.fill((0, 0, 0))

    pygame.display.flip()
    
    if play:
        sfx.play(1)
        play = False
        time.sleep(2)
    else:
        play = True
    

    clock.tick(30)


    
