##Importing PyGames Version 2.3.0
import sys
import pygame
import button
##initializes each of the modules
pygame.init()
print(pygame.ver)

##Attempt at a menu lmao.

size = width, height = 1920, 1080
black = 0, 0, 0
bg = pygame.image.load("bg.jpg")
bg = pygame.transform.scale(bg,(1920, 1080))
screen = pygame.display.set_mode(size)

##Buttons image something
start_image = pygame.image.load('grey_button14.png').convert_alpha()
options_image =  pygame.image.load('grey_button14.png').convert_alpha()
exit_image =  pygame.image.load('grey_button14.png').convert_alpha()

##create button instances
start_button = button.Button(960, 450, start_image, 3.0)
options_button = button.Button(960, 625, options_image, 2)
exit_button = button.Button(960, 775, exit_image, 2)



font1 = pygame.font.SysFont('kenvector_future.ttf', 500)
font2 = pygame.font.SysFont('kenvector_future.ttf', 200)
start_text = font1.render('Start', True, black)
options_text = font2.render('Options', True, black)
exit_text = font2.render('Exit', True, black)

class FONT():
    def __init__(self, x, y):
        

runing = True
while runing:
    screen.blit(bg,(0,0))


    if start_button.draw(screen) == True:
        print("Start")
    if options_button.draw(screen) == True:
        print("Option")
    if exit_button.draw(screen) == True:
        runing = False
        #print("Exit")
    
    screen.blit(start_text, (0, 0))
    screen.blit(options_text, (0, 0))
    screen.blit(exit_text, (0, 0))



    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()      
    pygame.display.update()
pygame.quit()





