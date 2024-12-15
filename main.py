import pygame
pygame.init()
import logic

#code to make screen
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Crack The Code')


#code for the background image
images = [
    pygame.image.load('Layer_0011_0.png').convert_alpha(),
    pygame.image.load('Layer_0010_1.png').convert_alpha(),
    pygame.image.load('Layer_0009_2.png').convert_alpha(),
    pygame.image.load('Layer_0008_3.png').convert_alpha(),
    pygame.image.load('Layer_0007_Lights.png').convert_alpha(),
    pygame.image.load('Layer_0006_4.png').convert_alpha(),
    pygame.image.load('Layer_0005_5.png').convert_alpha(),
    pygame.image.load('Layer_0004_Lights.png').convert_alpha(),
    pygame.image.load('Layer_0003_6.png').convert_alpha(),
    pygame.image.load('Layer_0002_7.png').convert_alpha(),
    pygame.image.load('Layer_0001_8.png').convert_alpha(),
    pygame.image.load('Layer_0000_9.png').convert_alpha()
]


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

#call game function to run game
logic.game(screen,images,start_button)
