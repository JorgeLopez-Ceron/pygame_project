import pygame
pygame.init()
import logic

#code to make screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Crack The Code')


status = 'main'

#code for the start and background image
background_image = pygame.image.load('background_image.jpg')


#loading button
start_button = logic.Button(
    screen_width // 2 - 50,
    screen_height // 2,
100,
50,
(255,0,0),
'START!',
    pygame.font.Font('GemunuLibre-VariableFont_wght.ttf', 40),
    (0,0,0)
)

#calling menu function
logic.menu_screen(screen,background_image,start_button)

