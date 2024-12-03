#add here any classes from the main

import pygame

class Button:
    def __init__(self, x, y, image,scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False

    def draw(self,surface):
        action = False
        #grabs mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

def menu_screen(surface,image,button):
    run = True
    button_clicked = False
    button_done = False

#code for title
    font = pygame.font.Font('PaytoneOne-Regular.ttf', 50)
    title = font.render('Crack The Code', True, (255,255,255))


    while run:
        surface.blit(image, (0, 0))

        if not button_clicked:
            surface.blit(title, (surface.get_width() // 2 - title.get_width() // 2, 50))
            if button.draw(surface):
                button_clicked = True
                print('button has been clicked')

        if button_clicked and not button_done:
            #here we can call function to change screen
            print('showing background')
            button_done = True

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
