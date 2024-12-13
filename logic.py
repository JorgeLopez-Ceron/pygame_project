#add here any classes from the main
import pygame
from button import Button

text_font = pygame.font.Font('GemunuLibre-VariableFont_wght.ttf', 40)


def draw_text_box(surface, x, y, box_length, box_width, box_color):
    pygame.draw.rect(surface, box_color, (x, y, box_length,box_width))

def draw_text(surface,text,font,text_color,x,y):
    print_text = font.render(text,True,text_color)
    length = print_text.get_width()
    surface.blit(print_text,(x - length // 2, y))

def bg(surface,backgrounds):
    #draw them into screen
    for image in backgrounds:
        surface.blit(image, (0,0))


#fix screen change from riddle one
def game(surface,images,button):
    status = 'main_menu'
    #extra_bear_riddle = False
    extra_troll_riddle = False

    while True:
        if status == 'main_menu':
            status = menu_screen(surface,images,button)
        elif status == 'transition_screen':
            status = transition_screen(surface,images)
        elif status == 'first_choice':
            status = first_choice(surface,images)
        elif status == 'bear_encounter':
            status = bear_encounter(surface,images)
        elif status == 'bear_death':
            status = bear_death(surface, images)
        elif status == 'continue_to_bridge':
            status = continue_to_bridge(surface,images)
        elif status == 'troll_encounter_v1':
            status = troll_encounter_v1(surface,images)
        elif status == 'troll_encounter_v2':
            extra_troll_riddle = True
            status = troll_encounter_v2(surface,images)
        elif status == 'ruins_info':
            status = ruins_info(surface, images)
        elif status == 'riddle_one':
            status = riddle_one(surface,images)
        elif status == 'riddle_two':
            status = riddle_two(surface,images)
        elif status == 'riddle_ending':
            status = riddle_ending(surface, images)
        elif status == 'continue':
            if extra_troll_riddle:
               status = troll_riddle(surface, images)
               if status == 'keeper_encounter':
                    status = keeper_encounter(surface, images)
            else:
                status = keeper_encounter(surface,images)

        elif status == 'win_screen':
            status = win_screen(surface, images)


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
            #show info screen/text
            draw_text(surface,'Find the letters to create the code' ,text_font,(255,225,225),250, 100)
            draw_text(surface,'to return to your world!', text_font,(255,255,255),250,150)
            draw_text(surface,'Press space to continue',text_font,(255,255,255),250,250)


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


def transition_screen(surface,images):
    run = True

    while run:
        bg(surface,images)

        #drawing text
        draw_text(surface,'transition screen',text_font,(255,255,255),250,100)
        draw_text(surface,'Press space!',text_font,(255,255,255),250,250)


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
    while run:
        bg(surface, images)

        #draws text box and adds the text on top
        draw_text_box(surface,100,50,300,250,(112,128,144))
        draw_text(surface,'You hear a noise in',text_font,(255,255,255),250,50)
        draw_text(surface,'a bush nearby...',text_font,(255,255,255),250,100)
        draw_text(surface,'What will you do?',text_font,(255,255,255),250,200)

        #code to create buttons
        yes_button = Button(50,350,150,50,(112,128,144),'why not..?',text_font,(255,255,255))
        no_button = Button(300,350,150,50,(112,128,144),'yeahh no..',text_font,(255,255,255))

        if yes_button.draw(surface):
            status = 'bear_encounter'
            return status
        elif no_button.draw(surface):
            status = 'continue_to_bridge'
            return status


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()
    pygame.quit()

def bear_encounter(surface,images):
   run = True

   while run:
       bg(surface,images)

       draw_text_box(surface,100,50,300, 100,(112,128,144))
       draw_text(surface,'bear encounter screen',text_font,(255,255,255),250,75)

       hit_button = Button((surface.get_width() // 2 - 50), 400, 100, 50, (112, 128, 144), 'HIT', text_font,(255, 255, 255))
       run_button = Button((surface.get_width() // 2 + 50), 400, 100, 50, (112, 128, 144), 'RUN', text_font,(255, 255, 255))

       if hit_button:
           status = 'bear_death'
           return status
       elif run_button:
           status = 'continue_to_bridge'
           return status

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               run = False

       pygame.display.update()
   pygame.quit()


def bear_death(surface,images):
    run = True

    while run:
        # background
        bg(surface, images)

        #text and box for game over
        draw_text_box(surface, 100, 50, 300, 100, (112, 128, 144))
        draw_text(surface, 'Game Over!', text_font, (255, 255, 255), 250, 75)

        #code for death text
        draw_text(surface,'Maybe next time try not to',text_font,(255,255,255),250,200)
        draw_text(surface,'look in the bushes...',text_font,(255,255,255),250,250)

        #code for menu button
        menu_button = Button((surface.get_width() // 2 - 50),350,100,50,(112,128,144),'Menu',text_font,(255,255,255))

        if menu_button.draw(surface):
            status = 'main_menu'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def continue_to_bridge(surface,images):
    run = True

    while run:

        #background
        bg(surface,images)

        #text box and text
        draw_text_box(surface,50,50,400,300,(112,128,144))
        #draw_text_box(surface,100,50,300,250,(112,128,144))
        draw_text(surface,'You continue to a bridge',text_font,(255,255,255),250,100)
        draw_text(surface,'and are stopped by a troll',text_font,(255,255,255),250,150)
        draw_text(surface,'who wants your',text_font,(255,255,255),250,200)
        draw_text(surface,'headphones!',text_font,(255,255,255),250,250)

        #create buttons
        sure_button = Button(50,400,150,50,(112,128,144),'...Sure?',text_font,(255,255,255))
        no_button = Button(300,400,150,50,(112,128,144),'NO!',text_font,(255,255,255))

        #if the buttons are clicked
        if sure_button.draw(surface):
            status = 'troll_encounter_v1'
            return status
        elif no_button.draw(surface):
            status = 'troll_encounter_v2'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def troll_encounter_v1(surface,images):
    run = True

    while run:
        bg(surface, images)

        # drawing text
        draw_text(surface, 'troll encounter v1 screen', text_font, (255, 255, 255), 250, 100)
        draw_text(surface, 'Press space!', text_font, (255, 255, 255), 250, 250)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'ruins_info'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def troll_encounter_v2(surface,images):
    run = True

    while run:
        bg(surface, images)

        # drawing text
        draw_text(surface, 'troll encounter v2', text_font, (255, 255, 255), 250, 100)
        draw_text(surface, 'Press space!', text_font, (255, 255, 255), 250, 250)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'ruins_info'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

#maybe add a troll death?

def ruins_info(surface,images):
    run = True

    while run:
        bg(surface,images)

        draw_text_box(surface,50,50,400,400,(112,128,144))
        draw_text(surface,'You travel to the ruins where',text_font,(255,255,255),250,50)
        draw_text(surface,'you find the keeper who is',text_font,(255,255,255),250,100)
        draw_text(surface,'friends with the bear and troll',text_font,(255,255,255),250,150)
        draw_text(surface,'and is willing to help on one',text_font,(255,255,255),250,200)
        draw_text(surface,'condition...',text_font,(255,255,255),250,250)
        draw_text(surface,'OBJ: solve riddles!',text_font,(255,255,255),250,350)
        draw_text(surface,'Press space!',text_font,(255,255,255),250,400)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'riddle_one'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def riddle_one(surface,images):
    run = True

    while run:
        bg(surface,images)

        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface,'I call myself to solve a task,',text_font,(255,255,255),250,50)
        draw_text(surface,'but without my base case,',text_font,(255,255,255),250,100)
        draw_text(surface,'my effort wont last...',text_font,(255,255,255),250,150)
        draw_text(surface,'What am I?',text_font,(255,255,255),250,200)

        infinite_loop_button = Button(10, 350, 200, 40, (112, 128, 144), 'Infinite loop', text_font, (255, 255, 255))
        recursive_button = Button(245, 350, 250, 40, (112, 128, 144), 'recursive function', text_font, (255, 255, 255))
        call_back_button = Button(150, 400, 200, 40, (112, 128, 144), 'callback', text_font, (255, 255, 255))


        if infinite_loop_button.draw(surface):
            status = 'riddle_ending'
            return status

        if recursive_button.draw(surface):
            status = 'riddle_two'
            return status

        if call_back_button.draw(surface):
            status = 'riddle_ending'
            return status



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def riddle_two(surface,images):
    run = True

    while run:
        bg(surface,images)

        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface,'Im a home for your code,',text_font,(255,255,255),250,50)
        draw_text(surface,'both public and private,',text_font,(255,255,255),250,100)
        draw_text(surface,'where branches grow, and',text_font,(255,255,255),250,150)
        draw_text(surface,'pull requests unite it,',text_font,(255,255,255),250,200)
        draw_text(surface,'What am I?',text_font,(255,255,255),250,250)

        bitbucket_button = Button(10, 350, 200, 40, (112, 128, 144), 'Bitbucket', text_font, (255, 255, 255))
        git_button = Button(245, 350, 250, 40, (112, 128, 144), 'Git', text_font, (255, 255, 255))
        github_button = Button(150, 400, 200, 40, (112, 128, 144), 'Github', text_font, (255, 255, 255))

        if bitbucket_button.draw(surface):
            status = 'riddle_ending'
            return status
        elif git_button.draw(surface):
            status = 'riddle_ending'
            return status
        elif github_button.draw(surface):
            status = 'keeper_encounter'
            return status


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def bear_riddle(surface,images):
    run = True

    while run:
        bg(surface, images)

        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface,'bear riddle',text_font,(255,255,255),250,50)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'main_menu'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def troll_riddle(surface,images):
    run = True

    while run:
        bg(surface, images)

        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface, 'troll riddle', text_font, (255, 255, 255), 250, 50)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'keeper_screen'
                    return status

            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()
    pygame.quit()

def riddle_ending(surface,images):
    run = True

    while run:
        # background
        bg(surface, images)

        # text and box for game over
        draw_text_box(surface, 100, 50, 300, 100, (112, 128, 144))
        draw_text(surface, 'Game Over!', text_font, (255, 255, 255), 250, 75)

        # code for death text
        draw_text(surface, 'Hmm maybe pay more', text_font, (255, 255, 255), 250, 200)
        draw_text(surface, 'attention in class..', text_font, (255, 255, 255), 250, 250)

        # code for menu button
        menu_button = Button((surface.get_width() // 2 - 50), 350, 100, 50, (112, 128, 144), 'Menu', text_font,
                             (255, 255, 255))

        if menu_button.draw(surface):
            status = 'main_menu'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()


def keeper_encounter(surface,images):
    run = True

    while run:
        bg(surface,images)

        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface, 'keeper screen', text_font, (255, 255, 255), 250, 50)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'win_screen'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def win_screen(surface,images):
    run = True

    while run:
        bg(surface,images)

        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface,'Win screen',text_font,(255,255,255),250,50)





        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'main_menu'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()