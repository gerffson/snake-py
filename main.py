import pygame

pygame.init()

game_over = False
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

x1 = 300
y1 = 300
 
x1_direction = 0       
y1_direction = 0

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_direction = -10
                y1_direction = 0
            elif event.key == pygame.K_RIGHT:
                x1_direction = 10
                y1_direction = 0
            elif event.key == pygame.K_UP:
                y1_direction = -10
                x1_direction = 0
            elif event.key == pygame.K_DOWN:
                y1_direction = 10
                x1_direction = 0
 
    x1 += x1_direction
    y1 += y1_direction
    screen.fill(white)

    pygame.draw.rect(screen, black, [x1, y1, 10, 10])
    pygame.display.update() 
    clock.tick(30)

pygame.quit()
quit()