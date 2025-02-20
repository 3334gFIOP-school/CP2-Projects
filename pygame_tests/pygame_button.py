# Jackson Hauley PYGAME TEST

import pygame 
clock = pygame.time.Clock()
import sys 
import random
import time
  
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
bigfont = pygame.font.SysFont('Arial',70) 

# Rendering a text written in the font
quit_button_text = smallfont.render('Quit' , True , white) 
reaction_button_text = smallfont.render('Reaction' , True , white) 

# COMPLETELY EDITABLE button location variables

quit_location = {
"width" : 140,
"height" : 40,
"StartPos": {"x" : 400 ,"y" : 360} # Top left coords
}

reaction_game_location = {
"width" : 140,
"height" : 40,
"StartPos": {"x" :  180,"y" : 360} # Top left coords
}

def quit_check():
    if ev.type == pygame.QUIT: 
            pygame.quit() 
            quit = 1


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
    screen.blit(quit_button_text,(quit_location['StartPos']['x']+0,quit_location['StartPos']['y'])) # Putting text on the button

    # REACTION GAME BUTTON ================================
    if reaction_game_location['StartPos']['x'] <= mouse[0] <= reaction_game_location['StartPos']['x'] + reaction_game_location['width'] and reaction_game_location['StartPos']['y'] <= mouse[1] <= reaction_game_location['StartPos']['y']+reaction_game_location['height']: 
        pygame.draw.rect(screen,color_light,[reaction_game_location['StartPos']['x'],reaction_game_location['StartPos']['y'],reaction_game_location['width'],reaction_game_location['height']]) # If mouse is hovering
    else: 
        pygame.draw.rect(screen,color_dark,[reaction_game_location['StartPos']['x'],reaction_game_location['StartPos']['y'],reaction_game_location['width'],reaction_game_location['height']]) # If mouse is not touching
    screen.blit(reaction_button_text,(reaction_game_location['StartPos']['x']+0,reaction_game_location['StartPos']['y'])) # Putting text on the button



    quit = 0

    for ev in pygame.event.get(): 
          
        if ev.type == pygame.QUIT: 
            pygame.quit() 
            quit = 1
            break
              
        if ev.type == pygame.MOUSEBUTTONDOWN: # Mouse Click Checking
            # This is where you find out where the button was clicking with the coordinates

            if quit_location['StartPos']['x'] <= mouse[0] <= quit_location['StartPos']['x']+quit_location['width'] and quit_location['StartPos']['y'] <= mouse[1] <= quit_location['StartPos']['y']+quit_location['height']: 
                pygame.quit() 
                quit = 1
                break

            if reaction_game_location['StartPos']['x'] <= mouse[0] <= reaction_game_location['StartPos']['x']+reaction_game_location['width'] and reaction_game_location['StartPos']['y'] <= mouse[1] <= reaction_game_location['StartPos']['y']+reaction_game_location['height']: 
                screen.blit(bigfont.render('Reaction Game' , True , white),(100,100))
                while True:

                    
                    pygame.display.update() # updates the frames of the game (always use)
                    clock.tick(60) # Capping at 60fps so my PC doesnt die
                    quit_check()
                    if quit == 1:
                        break   

    
    if quit == 1:
        break    

    clock.tick(60) # Capping at 60fps so my PC doesnt die
    pygame.display.update() # updates the frames of the game (always use)

        