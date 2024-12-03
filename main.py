import pygame
import logic

#code to make screen
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Crack The Code')


status = 'main'

#code for the start and background image
start_image = pygame.image.load('start_button.png').convert_alpha()
background_image = pygame.image.load('background_image.jpg')


#loading button
start_button = logic.Button(175,225, start_image, 0.1)

#pygame.quit()
logic.menu_screen(screen,background_image,start_button)

