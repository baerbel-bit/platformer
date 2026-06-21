import pygame
import numpy

pygame.init()
pygame.display.set_caption("first game platformer")
win_surface = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
win_size = win_surface.get_size()

hintergrund = pygame.Surface(win_size)
hintergrund.fill((0, 255, 0))


# variablen for player size
x = 50
y = 50
width = 40
height = 60
vel = 5
vel1 = 10
# body to jump on rectancle

x1 = 100
y1 = 100
width1 = 100
height1 = 100

#main game loob
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.VIDEORESIZE:
            win_size = event.size
            win_surface = pygame.display.set_mode(win_size, pygame.RESIZABLE)
            hintergrund = pygame.Surface(win_size)
            hintergrund.fill((0, 255, 0))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_v:
                y -= vel1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
        x -= vel
    if keys[pygame.K_d]:
        x += vel
    if keys[pygame.K_w]:
        y -= vel
    if keys[pygame.K_s]:
        y += vel



    win_surface.blit(hintergrund, (0, 0))
    pygame.draw.rect(win_surface, (255, 0, 0), (x, y, width, height))
    pygame.draw.rect(win_surface, (255, 0, 0), (x1, y1, width1, height1))
    pygame.display.update()

pygame.quit()