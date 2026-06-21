import pygame
import urllib.request
pygame.init()
pygame.display.set_caption("first game platformer")
win_surface = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
win_size = win_surface.get_size()

#fetching,loading and scailing and  the background
url = "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%2Fid%2FOIP.wGREfI0D3BMQRjAy374zGgHaE0%3Fpid%3DApi&f=1&ipt=139b75c5e5219669308854aa30049220b5a4ae832dd0bd5c2857f4f455904711&ipo=images"
urllib.request.urlretrieve(url, "hintergrund.png")
hintergrund = pygame.image.load("hintergrund.png")
hintergrund = pygame.transform.scale(hintergrund, win_size)



x = 50
y = 50
width = 40
height = 60
vel = 5


#main game loob
run = True
while run:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win_surface.blit(hintergrund, (0, 0))
    pygame.draw.rect(win_surface, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()