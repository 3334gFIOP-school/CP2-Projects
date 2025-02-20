import pygame # type: ignore
import sys 
import random
  
pygame.init() # initializing the constructor 
 
  
# screen resolution 
res = (720,720) 
  
# Names the window
pygame.display.set_caption('Random Title')

# opens up a window 
screen = pygame.display.set_mode(res) 
  
# white color 
white = (255,255,255) 
  
# light shade of the button 
color_light = (170,170,170)

  
# dark shade of the button 
color_dark = (100,100,100) 
alphabet = [chr(i) for i in range(97, 123)]
# stores the width of the 
# screen into a variable 
width = screen.get_width() 
  
# stores the height of the 
# screen into a variable 
height = screen.get_height() 
  
# defining a font 
smallfont = pygame.font.SysFont('Arial',35) 

  
# rendering a text written in 
# this font 

text = smallfont.render('Quit' , True , white) 

while True: 
    # fills the screen with a color 
    screen.fill((40,40,40)) # R G B 

    # stores the (x,y) coordinates into 
    # the variable as a tuple 
    mouse = pygame.mouse.get_pos() # Stores mouse coordinates


    # QUIT BUTTON ================================
    if width/4 <= mouse[0] <= width/4+140 and height/4 <= mouse[1] <= height/4+40: 
        pygame.draw.rect(screen,color_light,[width/4,height/4,140,40]) 
          
    else: 
        pygame.draw.rect(screen,color_dark,[width/4,height/4,140,40]) 

    # superimposing the text onto quit button
    screen.blit(text , (width/4+38,height/4)) 

    # END QUIT BUTTON ===================================

    # updates the frames of the game 
    pygame.display.update() 

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
            if width/4 <= mouse[0] <= width/4+140 and height/4 <= mouse[1] <= height/4+40: 
                pygame.quit() 
                quit = 1
                break
    
    if quit == 1:
        break

    pygame.display.set_caption(random.choice(alphabet))    