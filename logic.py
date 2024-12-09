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

def draw_text_box(surface, x, y, box_length, box_width, box_color):
    pygame.draw.rect(surface, box_color, (x, y, box_length,box_width))

def bg(surface,backgrounds):
    #draw them into screen
    for image in backgrounds:
        surface.blit(image, (0,0))

def game(surface,images,button):
    status = 'main_menu'

    while True:
        if status == 'main_menu':
            status = menu_screen(surface,images,button)
        elif status == 'transition_screen':
            status = transition_screen(surface,images)
        elif status == 'first_choice':
            status = first_choice(surface,images)
        elif status == 'done':
            print('done')

        pygame.display.update()



def menu_screen(surface,images,button):
    run = True
    button_clicked = False

#code for title
    font = pygame.font.Font('BungeeTint-Regular.ttf', 50)
    title = font.render('Crack The Code', True, (255,255,255))

    # menu game loop
    while run:
        bg(surface,images)

        if not button_clicked:
            surface.blit(title, (surface.get_width() // 2 - title.get_width() // 2, 50))
            if button.draw(surface):
                button_clicked = True

        if button_clicked:
            #put this onto own screen so that background can reset easier
            #return 'info_screen'
            info_text_pt1 = text_font.render('Find the letters to create the code' ,True,(255,225,225))
            surface.blit(info_text_pt1, (250 - info_text_pt1.get_width() // 2, 100))
            info_text_p2 = text_font.render('to return to your world!',True , (255,225,225))
            surface.blit(info_text_p2, (250 - info_text_p2.get_width() // 2, 150))
            info_text_press_s = text_font.render('Press space to continue', True , (255,225,225))
            surface.blit(info_text_press_s, (250 - info_text_press_s.get_width() // 2, 250))

            #check if space is clicked in second screen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif button_clicked and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'transition_screen'
                    return status

        pygame.display.update()
    pygame.quit()

def info_screen(screen,images):
    pass

def transition_screen(surface,images):
    run = True

    while run:

        bg(surface,images)
        test = text_font.render('test text', True, (255,255,255))
        surface.blit(test, (250 - test.get_width() // 2, 100))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'first_choice'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def first_choice(surface,images):
    run = True
    button_yes = False
    button_no = False

    while run:
        bg(surface, images)
        draw_text_box(surface,100,100,300,250,(0,0,0))
        test = text_font.render('first choice ', True, (255, 255, 255))
        surface.blit(test, (250 - test.get_width() // 2, 100))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'done'
                    return status

        pygame.display.update()
    pygame.quit()