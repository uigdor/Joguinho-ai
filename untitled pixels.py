import pygame
import random
pygame.init ()

tela = pygame.display.set_mode ((1500, 800), pygame. RESIZABLE)
pygame.display.set_caption ("Untitled Pixels!")

playerx = 720
playery = 380
player_alt = 50
player_lar = 50
playerbody = pygame.Rect (playerx, playery, player_alt, player_lar)
ph = 1

randomcolor = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))

pixel1x = random.randint (250, 1400)
pixel1y = random.randint (80, 720)
pixel1_alt = 20
pixel1_lar = 20
pixel1body = pygame.Rect (pixel1x, pixel1y, pixel1_alt, pixel1_lar)

pixel2x = random.randint (250, 1400)
pixel2y = random.randint (80, 720)
pixel2_alt = 20
pixel2_lar = 20
pixel2body = pygame.Rect (pixel2x, pixel2y, pixel2_alt, pixel2_lar)

pixel3x = random.randint (250, 1400)
pixel3y = random.randint (80, 720)
pixel3_alt = 20
pixel3_lar = 20
pixel3body = pygame.Rect (pixel3x, pixel3y, pixel3_alt, pixel3_lar)

pixel4x = random.randint (250, 1400)
pixel4y = random.randint (80, 720)
pixel4_alt = 20
pixel4_lar = 20
pixel4body = pygame.Rect (pixel4x, pixel4y, pixel4_alt, pixel4_lar)

pixel5x = random.randint (250, 1400)
pixel5y = random.randint (80, 720)
pixel5_alt = 20
pixel5_lar = 20
pixel5body = pygame.Rect (pixel5x, pixel5y, pixel5_alt, pixel5_lar)

pixel6x = random.randint (250, 1400)
pixel6y = random.randint (80, 720)
pixel6_alt = 20
pixel6_lar = 20
pixel6body = pygame.Rect (pixel6x, pixel6y, pixel6_alt, pixel6_lar)

pixel7x = random.randint (250, 1400)
pixel7y = random.randint (80, 720)
pixel7_alt = 20
pixel7_lar = 20
pixel7body = pygame.Rect (pixel7x, pixel7y, pixel7_alt, pixel7_lar)



barreira1x = 5
barreira1y = 1
barreira1_alt = 8000
barreira1_lar = 10
barreira1body = pygame.Rect (barreira1x, barreira1y, barreira1_alt, barreira1_lar)

barreira2x = 5
barreira2y = 880
barreira2_alt = 8000
barreira2_lar = 10
barreira2body = pygame.Rect (barreira2x, barreira2y, barreira2_alt, barreira2_lar)

barreira3x = 5
barreira3y = 5
barreira3_alt = 10
barreira3_lar = 8000
barreira3body = pygame.Rect (barreira3x, barreira3y, barreira3_alt, barreira3_lar)

barreira4x = 1525
barreira4y = 5
barreira4_alt = 10
barreira4_lar = 8000
barreira4body = pygame.Rect (barreira4x, barreira4y, barreira4_alt, barreira4_lar)

fonte = pygame.font.SysFont ("none", 32)
fonte2 = pygame.font.SysFont ("none", 25)
textosurface = fonte.render ("UNTITLED PIXELS!", True, (255, 255, 255))
textosurface2 = fonte2.render ("Space for play", True, (255, 255, 255))

menu = True
janelaaberta = True
while janelaaberta:
    for evento in pygame.event.get ():
        if evento.type == pygame.QUIT:
            janelaaberta = False

    teclas = pygame.key.get_pressed ()
    if menu:
        if teclas [pygame.K_SPACE]:
            menu = False

    else:
        if teclas [pygame.K_d]:
            playerx += ph
        if teclas [pygame.K_a]:
            playerx -= ph

        if teclas [pygame.K_s]:
            playery += ph
        if teclas [pygame.K_w]:
            playery -= ph

        if teclas [pygame.K_r]:
            playerx = 720
            playery = 380

    playerbody.x = playerx
    playerbody.y = playery

    if playerbody.colliderect (pixel1body):
        if teclas [pygame.K_d]:
            pixel1x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel1x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel1y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel1y += random.randint (80, 720)

        pixel1body.x = random.randint (250, 1400)
        pixel1body.y = random.randint (80, 720)

        

    if playerbody.colliderect (pixel2body):
        if teclas [pygame.K_d]:
            pixel2x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel2x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel2y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel2y += random.randint (80, 720)

        pixel2body.x = random.randint (250, 1400)
        pixel2body.y = random.randint (80, 720)

    if playerbody.colliderect (pixel3body):
        if teclas [pygame.K_d]:
            pixel3x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel3x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel3y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel3y += random.randint (80, 720)

        pixel3body.x = random.randint (250, 1400)
        pixel3body.y = random.randint (80, 720)

    if playerbody.colliderect (pixel4body):
        if teclas [pygame.K_d]:
            pixel4x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel4x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel4y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel4y += random.randint (80, 720)

        pixel4body.x = random.randint (250, 1400)
        pixel4body.y = random.randint (80, 720)

    if playerbody.colliderect (pixel5body):
        if teclas [pygame.K_d]:
            pixel5x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel5x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel5y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel5y += random.randint (80, 720)

        pixel5body.x = random.randint (250, 1400)
        pixel5body.y = random.randint (80, 720)


    if playerbody.colliderect (pixel6body):
        if teclas [pygame.K_d]:
            pixel6x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel6x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel6y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel6y += random.randint (80, 720)

        pixel6body.x = random.randint (250, 1400)
        pixel6body.y = random.randint (80, 720)

    if playerbody.colliderect (pixel7body):
        if teclas [pygame.K_d]:
            pixel7x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel7x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel7y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel7y += random.randint (80, 720)

        pixel7body.x = random.randint (250, 1400)
        pixel7body.y = random.randint (80, 720)

    if playerbody.colliderect (barreira1body):
        playery += 2

    if playerbody.colliderect (barreira2body):
        playery -= 2

    if playerbody.colliderect (barreira3body):
        playerx += 2

    if playerbody.colliderect (barreira4body):
        playerx -= 2


    tela.fill ((15, 15, 15))
    tela.blit (textosurface, (635, 20))
    tela.blit (textosurface2, (680, 40))

    pygame.draw.rect (tela, (255, 255, 255), playerbody)
    if teclas [pygame.K_c]:
        playerbody = pygame.draw.rect (tela, (randomcolor), playerbody)

    pygame.draw.rect (tela, (80, 180, 110), pixel1body)

    pygame.draw.rect (tela, (255, 20, 10), pixel2body)

    pygame.draw.rect (tela, (10, 20, 255), pixel3body)

    pygame.draw.rect (tela, (255, 250, 40), pixel4body)

    pygame.draw.rect (tela, (255, 160, 20), pixel5body)

    pygame.draw.rect (tela, (10, 130, 10), pixel6body)

    pygame.draw.rect (tela, (130, 20, 130), pixel7body)

    #pygame.draw.rect (tela, (255, 0, 0), barreira1body)

    #pygame.draw.rect (tela, (255, 0, 0), barreira2body)

    #pygame.draw.rect (tela, (255, 0, 0), barreira3body)

    #pygame.draw.rect (tela, (255, 0, 0), barreira4body)
    pygame.display.flip ()

pygame.quit ()