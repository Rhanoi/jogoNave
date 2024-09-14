# Example file showing a basic pygame "game loop"
import pygame
import random

# pygame setup
pygame.init()

x = 1280
y = 720

screen = pygame.display.set_mode((x, y))
clock = pygame.time.Clock()

bg = pygame.image.load('images/bg.png').convert_alpha()
bg = pygame.transform.scale(bg, (x, y))

nave = pygame.image.load('images/nave.png').convert_alpha()
nave = pygame.transform.scale(nave, (50, 50))

alien = pygame.image.load('images/ufo.png').convert_alpha()
alien = pygame.transform.scale(alien, (50, 50))

missil = pygame.image.load('images/bala.png').convert_alpha()
missil = pygame.transform.scale(missil, (25, 25))

pos_alien_x = 500
pos_alien_y = 360

pos_player_x = 200
pos_player_y = 300

vel_missil_x = 0
pos_missil_x = 200
pos_missil_y = 310


pontos = 4

triggered = False


rodando = True

font = pygame.font.SysFont('fonte/PixelGameFont.ttf', 50)


nave_rect = nave.get_rect()
alien_rect = alien.get_rect()
missil_rect = missil.get_rect()


#Funções
def respawn():
    x = 1350
    y = random.randint(1,640)
    return [x,y]

def respawn_missil():
    triggered = False
    respawn_missil_x = pos_player_x
    respawn_missil_y = pos_player_y
    vel_missil_x = 0
    return[respawn_missil_x, respawn_missil_y, triggered, vel_missil_x]

def colisions():
    global pontos
    
    if nave_rect.colliderect(alien_rect) or alien_rect.x < 100:
        pontos -=1
        return True
    elif missil_rect.colliderect(alien_rect):
        pontos +=1
        return True
    else:
        return False
    
    
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
    
    
    rel_x = x % bg.get_rect().width
    screen.blit(bg, (rel_x - bg.get_rect().width,0)) # cria um background
    if rel_x < 1280:
        screen.blit(bg, (rel_x, 0))
        
    
    #teclas
    tecla = pygame.key.get_pressed()
    if tecla[pygame.K_UP] and pos_player_y > 1:
        pos_player_y -= 10
        if not triggered:
           pos_missil_y -= 10
        
    if tecla[pygame.K_DOWN] and pos_player_y < 665:
        pos_player_y += 10
        
        if not triggered:
           pos_missil_y += 10
        
        
    if tecla[pygame.K_SPACE]:
        triggered = True
        vel_missil_x = 20
    
    if pontos < 0:
        rodando = False
    #regras respaw
    if pos_alien_x == 50 or colisions():
        pos_alien_x = respawn()[0]
        pos_alien_y = respawn()[1]
    
    if pos_missil_x == 1300:
        pos_missil_x, pos_missil_y, triggered, vel_missil_x = respawn_missil()
    
    
    #posição rect
    nave_rect.x = pos_player_x
    nave_rect.y = pos_player_y
    
    missil_rect.x = pos_missil_x
    missil_rect.y = pos_missil_y
    
    alien_rect.x = pos_alien_x
    alien_rect.y = pos_alien_y
    
    
    #movimentação
    x-=10 
    pos_alien_x -= 20
    pos_missil_x += vel_missil_x
    
    pygame.draw.rect(screen, (255, 0, 0), nave_rect, -1)
    pygame.draw.rect(screen, (255, 0, 0), missil_rect, -1)
    pygame.draw.rect(screen, (255, 0, 0), alien_rect, -1)
    
    score = font.render(f' Pontos: {int(pontos)}', True, (255,255,255))
    screen.blit(score, (50,50))
    
    #cria imagens
    screen.blit(alien, (pos_alien_x, pos_alien_y))
    screen.blit(missil, (pos_missil_x, pos_missil_y))
    screen.blit(nave, (pos_player_x, pos_player_y))
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(24)  # limits FPS to 24

pygame.quit()