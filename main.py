import pygame

#code to make screen
pygame.init()
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Crack The Code')

#code to make buttons
start_image = pygame.image.load('start_button.png').convert_alpha()

background_image = pygame.image.load('background_image.jpg')


class Button:
    def __init__(self, x, y, image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)

    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

start_button = Button(175,225, start_image, 0.1)
background = Button(0,0, background_image, 1.0)

#loop to make game run
run = True
while run:
    screen.fill((0,0,0))
    #screen.blit(background_image,(0,0))
    background.draw()
    start_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()

pygame.quit()

