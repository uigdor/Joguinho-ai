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
ph = 6
randomcolor = (random.randint (0, 255), random.randint (0, 255), random.randint (0, 255))
pontos = 0


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
pixel5_alt = 40
pixel5_lar = 40
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

pixel8x = random.randint (250, 1400)
pixel8y = random.randint (80, 720)
pixel8_alt = 20
pixel8_lar = 20
pixel8body = pygame.Rect (pixel8x, pixel8y, pixel8_alt, pixel8_lar)

pixel9x = random.randint (250, 1400)
pixel9y = random.randint (80, 720)
pixel9_alt = 20
pixel9_lar = 20
pixel9body = pygame.Rect (pixel9x, pixel9y, pixel9_alt, pixel9_lar)

pixel10x = random.randint (250, 1400)
pixel10y = random.randint (80, 720)
pixel10_alt = 30
pixel10_lar = 30
pixel10body = pygame.Rect (pixel10x, pixel10y, pixel10_alt, pixel10_lar)


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
fonte1 = pygame.font.SysFont ("none", 60)
fonte2 = pygame.font.SysFont ("none", 50)
fonte3 = pygame.font.SysFont ("none", 40)
fonte4 = pygame.font.SysFont ("none", 35)
textosurface = fonte.render ("UNTITLED PIXELS!", True, (255, 255, 255))
textosurface1 = fonte1.render ("UNTITLED PIXELS!", True, (255, 255, 255))
textosurface2 = fonte2.render ("Space for play", True, (255, 255, 255))
textosurface3 = fonte3.render ("Game Paused. Click 'O' for play again", True, (255, 255, 255))
#textosurface4 = fonte4.render (f"pountuação: {pontos}", True, (255, 255, 255))


menux = 5
menuy = 5
menualt = 9999
menular = 9999
menubody = pygame.Rect (menux, menuy, menualt, menular)

relogio = pygame.time.Clock ()
menu = True
pause = False
janelaaberta = True

while janelaaberta:
    for evento in pygame.event.get ():
        if evento.type == pygame.QUIT:
            janelaaberta = False

    teclas = pygame.key.get_pressed ()
    if menu:
        if teclas [pygame.K_SPACE]:
            menu = False

    if pause:
        if teclas [pygame.K_d]:
                playerx += 0
        if teclas [pygame.K_a]:
                playerx -= 0

        if teclas [pygame.K_s]:
                playery += 0
        if teclas [pygame.K_w]:
                playery -= 0

        if teclas [pygame.K_r]:
                playerx += 0
                playery -= 0

        playerbody.x = playerx
        playerbody.y = playery

        if teclas [pygame.K_o]:
            pause = False

    else:
        if teclas [pygame.K_m]:
            menu = True
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

        if teclas [pygame.K_p]:
            pause = True

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
        pontos += 1

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
        pontos += 1

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
        pontos += 1

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
        pontos += 1

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
        pontos += 4

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
        pontos += 1

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
        pontos += 1

    if playerbody.colliderect (pixel8body):
        if teclas [pygame.K_d]:
            pixel8x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel8x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel8y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel8y += random.randint (80, 720)

        pixel8body.x = random.randint (250, 1400)
        pixel8body.y = random.randint (80, 720)
        pontos += 1

    if playerbody.colliderect (pixel9body):
        if teclas [pygame.K_d]:
            pixel9x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel9x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel9y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel9y += random.randint (80, 720)

        pixel9body.x = random.randint (250, 1400)
        pixel9body.y = random.randint (80, 720)
        pontos += 1

    if playerbody.colliderect (pixel10body):
        if teclas [pygame.K_d]:
            pixel10x -= random.randint (250, 1400)
        if teclas[pygame.K_a]:
            pixel10x += random.randint (250, 1400)
        
        if teclas [pygame.K_s]:
            pixel10y -= random.randint (80, 720)
        if teclas [pygame.K_w]:
            pixel10y += random.randint (80, 720)

        pixel10body.x = random.randint (250, 1400)
        pixel10body.y = random.randint (80, 720)
        pontos += 2


    if playerbody.colliderect (barreira1body):
        playery += 2

    if playerbody.colliderect (barreira2body):
        playery -= 2

    if playerbody.colliderect (barreira3body):
        playerx += 2

    if playerbody.colliderect (barreira4body):
        playerx -= 2

    textosurface4 = fonte4.render (f"pountuação: {pontos}", True, (255, 255, 255))

    tela.fill ((20, 20, 20))

    if menu:
        pygame.draw.rect (tela, (0, 0, 0), menubody)
        tela.blit (textosurface2, (630, 400))
        tela.blit (textosurface1, (562, 350))
        pontos = 0

    else:
        pygame.draw.rect (tela, (255, 255, 255), playerbody)

        pygame.draw.rect (tela, (80, 180, 110), pixel1body)

        pygame.draw.rect (tela, (255, 20, 10), pixel2body)

        pygame.draw.rect (tela, (10, 20, 255), pixel3body)

        pygame.draw.rect (tela, (255, 250, 40), pixel4body)

        pygame.draw.rect (tela, (255, 160, 20), pixel5body)

        pygame.draw.rect (tela, (10, 130, 10), pixel6body)

        pygame.draw.rect (tela, (250, 240, 100), pixel7body)

        pygame.draw.rect (tela, (20, 120, 220), pixel8body)

        pygame.draw.rect (tela, (70, 190, 40), pixel9body)

        pygame.draw.rect (tela, (255, 240 , 40), pixel10body)

        #pygame.draw.rect (tela, (255, 0, 0), barreira1body) #

        #pygame.draw.rect (tela, (255, 0, 0), barreira2body)

        #pygame.draw.rect (tela, (255, 0, 0), barreira3body)

        #pygame.draw.rect (tela, (255, 0, 0), barreira4body) #

        tela.blit (textosurface, (642, 20))

        tela.blit (textosurface4, (662, 856))

        if teclas [pygame.K_c]:
            playerbody = pygame.draw.rect (tela, (randomcolor), playerbody)

        if pause:
            tela.blit (textosurface3, (520, 400))
            playerbody = pygame.draw.rect (tela, (255, 255, 255), playerbody)


    pygame.display.flip ()
    pygame.display.update ()
    relogio.tick (80)

pygame.quit ()