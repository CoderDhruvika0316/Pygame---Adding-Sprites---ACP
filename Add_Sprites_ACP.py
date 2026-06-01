import pygame 
import random
pygame.init()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Adding Sprites to My Screen')    

clock = pygame.time.Clock()

player = pygame.Rect(100, 100, 50, 50)
enemy = pygame.Rect(random.randint(0, width - 50), random.randint(0, height - 50), 50, 50)
move_speed = 5

running = False

while not running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = True 
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= move_speed
    
    if keys[pygame.K_RIGHT]:
        player.x += move_speed

    if keys[pygame.K_UP]:
        player.y -= move_speed

    if keys[pygame.K_DOWN]:
        player.y += move_speed

    player.x = max(0, min(width - player.width, player.x))
    player.y = max(0, min(height - player.height, player.y))

    screen.fill("light pink")

    pygame.draw.rect(screen, (140, 3, 252), player)
    pygame.draw.rect(screen, (146, 247, 173), enemy)

    pygame.display.flip()
    clock.tick(90)

pygame.quit()