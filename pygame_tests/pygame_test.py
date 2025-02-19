# Example file showing a basic pygame "game loop"
import pygame
import time
import random

# pygame setup
pygame.init()

green = (0, 255, 0)
blue = (0, 0, 128)

screen = pygame.display.set_mode((2560, 1440))
#screen = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()
pygame.display.set_caption('========== Game ==========')
running = True
main_colors = ["red", "cyan", "blue", "green", "yellow", "magenta", "black", "white", "gray", "orange"]
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # fill the screen with a color to wipe away anything from last frame
    
    screen.fill(random.choice(main_colors))
    pygame.draw.rect(screen, random.choice(main_colors), pygame.Rect(random.randint(1,2560), random.randint(1,1440), 60, 60))
    pygame.display.flip()
    screen.fill(random.choice(main_colors))
    pygame.draw.rect(screen, random.choice(main_colors), pygame.Rect(random.randint(1,2560), random.randint(1,1440), 60, 60))
    pygame.display.flip()
    screen.fill(random.choice(main_colors))
    pygame.draw.rect(screen, random.choice(main_colors), pygame.Rect(random.randint(1,2560), random.randint(1,1440), 60, 60))
    pygame.display.flip()
    screen.fill(random.choice(main_colors))
    pygame.draw.rect(screen, random.choice(main_colors), pygame.Rect(random.randint(1,2560), random.randint(1,1440), 60, 60))
    pygame.display.flip()
    
    font = pygame.font.Font('freesansbold.ttf', 1000)
    text = font.render('GeeksForGeeks', True, green, blue)

    screen.fill("white")
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60
pygame.quit()