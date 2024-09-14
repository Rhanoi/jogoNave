# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

bg = pygame.image.load('images/bg.png').convert_alpha()
bg = pygame.transform.scale(bg, (1280, 720))

rodando = True

while rodando:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            rodando = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    # RENDER YOUR GAME HERE
    screen.blit(bg, (0,0))
    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()