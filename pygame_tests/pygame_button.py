# Jackson Hauley PYGAME TEST

import pygame 
clock = pygame.time.Clock()
import sys 
import random
  
pygame.init() # initializing the constructor 
 
# Names the window
pygame.display.set_caption('Random Title')

# Opens the window with the resolution
res = (720,720) 
screen = pygame.display.set_mode(res) 
  
# Colors
white = (255,255,255) 
color_light = (170,170,170)
color_dark = (100,100,100) 

alphabet = [chr(i) for i in range(97, 123)]

width = screen.get_width() 
height = screen.get_height() 
  
# Fonts
smallfont = pygame.font.SysFont('Arial',35) 

# Rendering a text written in the font
quit_button_text = smallfont.render('Quit' , True , white) 

# COMPLETELY EDITABLE quit location variable
quit_location = {
"width" : 140,
"height" : 40,
"StartPos": {"x" : 360 ,"y" : 360} # Top left coords
}


while True: # Main Loop (break after quit)

    screen.fill((40,40,40)) # R G B (fills screen)

    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates


    # QUIT BUTTON ================================
    if quit_location['StartPos']['x'] <= mouse[0] <= quit_location['StartPos']['x'] + quit_location['width'] and quit_location['StartPos']['y'] <= mouse[1] <= quit_location['StartPos']['y']+quit_location['height']: 
        pygame.draw.rect(screen,color_light,[quit_location['StartPos']['x'],quit_location['StartPos']['y'],quit_location['width'],quit_location['height']]) # If mouse is hovering
    else: 
        pygame.draw.rect(screen,color_dark,[quit_location['StartPos']['x'],quit_location['StartPos']['y'],quit_location['width'],quit_location['height']]) # If mouse is not touching
    screen.blit(quit_button_text , (quit_location['StartPos']['x']+quit_location['width']/4,quit_location['StartPos']['y'])) # Putting text on the button



    quit = 0

    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            quit = 1
            break
              
        #checks if a mouse is clicked 
        if ev.type == pygame.MOUSEBUTTONDOWN:
            # This is where you find out where the button was clicking with the coordinates
            #if the mouse is clicked on the 
            # button the game is terminated 
            if quit_location['StartPos']['x'] <= mouse[0] <= quit_location['StartPos']['x']+quit_location['width'] and quit_location['StartPos']['y'] <= mouse[1] <= quit_location['StartPos']['y']+quit_location['height']: 
                pygame.quit() 
                quit = 1
                break
    
    if quit == 1:
        break    

    # updates the frames of the game (always use)
    clock.tick(60) # Capping at 60fps so my PC doesnt die
    pygame.display.update() 

        