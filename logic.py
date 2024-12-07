#add here any classes from the main

import pygame

text_font = pygame.font.Font('GemunuLibre-VariableFont_wght.ttf', 40)

class Button:
    def __init__(self, x, y, width, height, color, text, font, text_color):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.clicked = False

    def draw(self,surface):
        #draw button
        pygame.draw.rect(surface, self.color, self.rect)

        #draw text on buttons
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

        #check for click
        action = False
        #grabs mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

def bg(surface,image):
    pass


def menu_screen(surface,image,button):
    run = True
    button_clicked = False

#code for title
    font = pygame.font.Font('BungeeTint-Regular.ttf', 50)
    title = font.render('Crack The Code', True, (255,255,255))

    # menu game loop
    while run:
        surface.blit(image, (0, 0))

        if not button_clicked:
            surface.blit(title, (surface.get_width() // 2 - title.get_width() // 2, 50))
            if button.draw(surface):
                button_clicked = True

        if button_clicked:
            #here we can call function to change screen and text
            info_text_pt1 = text_font.render('Find the letters to create the code' ,True,(255,225,225))
            surface.blit(info_text_pt1, (250 - info_text_pt1.get_width() // 2, 100))
            info_text_p2 = text_font.render('to return to your world!',True , (255,225,225))
            surface.blit(info_text_p2, (250 - info_text_p2.get_width() // 2, 150))
            info_text_press_s = text_font.render('Press space to continue', True , (255,225,225))
            surface.blit(info_text_press_s, (250 - info_text_press_s.get_width() // 2, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
