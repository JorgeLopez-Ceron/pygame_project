import pygame
from button import Button

text_font = pygame.font.Font('GemunuLibre-VariableFont_wght.ttf', 40)

def draw_text_box(surface: pygame.Surface,x: int, y:int, box_length: int, box_width: int, box_color: tuple[int,int,int]) -> None:
    """
    This function creates a text box with the args provided

    Args:
        surface: the screen the box is going on
        x: x coord of the text box
        y: y coord of the text box
        box_length: how long you want the box to be
        box_width: how wide you want the box to be
        box_color: what color the box will be

    Returns:
        no returns
    """
    pygame.draw.rect(surface, box_color, (x, y, box_length,box_width))

def draw_text(surface:pygame.Surface, text:str, font:pygame.font.Font, text_color:tuple[int,int,int], x:int, y:int) -> None:
    """
    This function creates text with the args provided

    Args:
        surface: the screen the box is going on
        text: string of text you want displayed
        font: specific font for text
        text_color: what color you want the text to be
        x: x coord of where the text will be placed
        y: y coord of where the text will be placed

    Returns:
        no returns
    """
    print_text = font.render(text,True,text_color)
    length = print_text.get_width()
    surface.blit(print_text,(x - length // 2, y))

def bg(surface:pygame.Surface, backgrounds:list[pygame.Surface]) -> None:
    """
    This function gets the list of images and creates the background

    Args:
        surface: the screen the bg will go on
        backgrounds: list of images used for bg

    Returns:
        no returns
    """
    for image in backgrounds:
        surface.blit(image, (0,0))

def loading_frames(sprite_sheet:pygame.Surface, frame_width: int, frame_height:int, frames_in_row:int) -> list[pygame.Surface]:
    """
    This function creates frames for sprite animation from args provided and returns a list of frames

    Args:
        sprite_sheet: the sprite sheet of the character you want to animate
        frame_width: the width of each frame in the sprite sheet
        frame_height: the height of each frame in the sprite sheet
        frames_in_row: how many frames are in total in the sprite sheet

    Returns:
        list[pygame.Surface]: a list of frames that have been modified to each have their own squares to animate
    """
    frames = []
    for i in range(frames_in_row):
        frame = sprite_sheet.subsurface(pygame.Rect(i * frame_width, 0,frame_width, frame_height))
        frames.append(frame)
    return frames

def game(surface:pygame.Surface, images:list[pygame.Surface],button:Button) -> None:
    """
    This function runs the game and switches screens when needed

    Args:
        surface: the screen that the game will be on
        images: the list of bg images for the game
        button: the starter button for the menu

    Returns:
        no returns
    """
    status = 'main_menu'
    extra_troll_riddle = False

    while True:
        surface.fill((0,0,0))
        if status == 'main_menu':
            status = menu_screen(surface,images,button)
        elif status == 'transition_screen':
            status = transition_screen(surface,images)
        elif status == 'first_choice':
            status = first_choice(surface,images)
        elif status == 'bear':
            status = bear_encounter(surface,images)
        elif status == 'bear_death':
            status = bear_death(surface, images)
        elif status == 'continue_to_bridge':
            status = continue_to_troll(surface,images)
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
        elif status == 'riddle_ending_for_riddle1':
            status = riddle_ending_for_riddle1(surface, images)
        elif status == 'riddle_ending_for_riddle2':
            status = riddle_ending_for_riddle2(surface, images)
        elif status == 'continue':
            if extra_troll_riddle:
               status = troll_riddle(surface, images)

               if status == 'keeper_encounter':
                    status = keeper_encounter(surface, images)
               elif status == 'riddle_ending_for_troll_riddle':
                   status = riddle_ending_for_troll_riddle(surface, images)
                   extra_troll_riddle = False

            else:
                status = keeper_encounter(surface,images)

        elif status == 'win_screen':
            status = win_screen(surface, images)


        pygame.display.update()



def menu_screen(surface:pygame.Surface, images:list[pygame.Surface], button:Button) ->str:
    """
    This function provides the code for the menu screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game
        button: the starter button for the menu

    Returns:
        str: returns status of next screen
    """
    run = True
    button_clicked = False

    #code for title
    font = pygame.font.Font('BungeeTint-Regular.ttf', 50)
    title = font.render('Crack The Code', True, (255,255,255))

    # menu game loop
    while run:
        surface.fill((0,0,0))
        bg(surface,images)

        if not button_clicked:
            surface.blit(title, (surface.get_width() // 2 - title.get_width() // 2, 50))
            if button.draw(surface):
                button_clicked = True

        if button_clicked:
            #show info screen/text
            draw_text_box(surface, 25, 50, 450, 350, (112, 128, 144))
            draw_text(surface,'Find the letters to create the code' ,text_font,(255,225,225),250, 50)
            draw_text(surface,'to return to your world!', text_font,(255,255,255),250,100)
            draw_text(surface,'+1 headphones', text_font,(255,255,255),250,200)
            draw_text(surface,'+1 laptop', text_font,(255,255,255),250,250)
            draw_text(surface,'Press space to continue!',text_font,(255,255,255),250,350)


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


def transition_screen(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the transition screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True
    frame_width = 64
    frame_height = 64
    frames_in_row = 11
    frame_index = 0
    clock = pygame.time.Clock()

    while run:
        surface.fill((0, 0, 0))
        bg(surface, images)

        #drawing text
        draw_text_box(surface,50,50,400,350,(112,128,144))
        draw_text(surface,'You run along confused yet',text_font,(255,255,255),250,50)
        draw_text(surface,'determined to find the',text_font,(255,255,255),250,100)
        draw_text(surface,'code and you suddenly hear',text_font,(255,255,255),250,150)
        draw_text(surface,'something close by',text_font,(255,255,255),250,200)
        draw_text(surface,'Press space!',text_font,(255,255,255),250,350)

        sprite_sheet_dino = pygame.image.load('DinoSprites - doux.png').convert_alpha()
        frames = loading_frames(sprite_sheet_dino, frame_width, frame_height, frames_in_row)
        surface.blit(frames[frame_index], (220, 275))

        # cycle through frames
        frame_index += 1
        if frame_index >= len(frames):
            frame_index = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'first_choice'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(5)
    pygame.quit()

def first_choice(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the first_choice screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True
    while run:

        surface.fill((0,0,0))
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
            status = 'bear'
            return status
        elif no_button.draw(surface):
            status = 'continue_to_bridge'
            return status


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()
    pygame.quit()

def bear_encounter(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
        This function provides the code for the panda bear screen

        Args:
            surface: the screen that the menu will be on
            images: the list of bg images for the game

        Returns:
            str: returns status of next screen
        """
    run = True
    frame_width = 64
    frame_height = 64
    frames_in_row = 12
    frame_index = 0
    clock = pygame.time.Clock()

    while run:
        surface.fill((0, 0, 0))
        bg(surface,images)

        #load in pandas
        panda_waving_sprite_sheet = pygame.image.load('PandaWave.png').convert_alpha()
        panda_eating_sprite_sheet = pygame.image.load('PandaEating.png').convert_alpha()

        draw_text(surface,'WILD PANDAS!',text_font,(255,255,255),250,25)
        draw_text(surface,'What will you do?!',text_font,(255,255,255),250,75)

        hit_button = Button(100, 200, 100, 50, (112, 128, 144), 'HIT', text_font,(255, 255, 255))
        run_button = Button(300, 200, 100, 50, (112, 128, 144), 'RUN', text_font,(255, 255, 255))

        #actually drawing pandas in
        frames = loading_frames(panda_waving_sprite_sheet,frame_width,frame_height,frames_in_row)
        frames_for_panda_two = loading_frames(panda_eating_sprite_sheet,frame_width,frame_height,frames_in_row)
        surface.blit(frames[frame_index],(200,400))
        surface.blit(frames_for_panda_two[frame_index],(300,400))

        #cycle through frames
        frame_index += 1
        if frame_index >= len(frames):
            frame_index = 0


        if hit_button.draw(surface):
            status = 'bear_death'
            return status
        elif run_button.draw(surface):
            status = 'continue_to_bridge'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(5)
    pygame.quit()


def bear_death(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the panda bear death screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        # background
        surface.fill((0,0,0))
        bg(surface, images)

        #text and box for game over
        draw_text_box(surface, 100, 50, 300, 100, (112, 128, 144))
        draw_text(surface, 'Game Over!', text_font, (255, 255, 255), 250, 75)

        #code for death text
        draw_text(surface,'You punched the panda but it did',text_font,(255,255,255),250,150)
        draw_text(surface,'no damage and instead the panda',text_font,(255,255,255),250,200)
        draw_text(surface,'just ate your laptop ultimately',text_font,(255,255,255),250,250)
        draw_text(surface,'trapping you in here forever...',text_font,(255,255,255),250,300)
        draw_text(surface,'-1 laptop',text_font,(255,255,255),250,350)

        #code for menu button
        menu_button = Button((surface.get_width() // 2 - 50),400,100,50,(112,128,144),'Menu',text_font,(255,255,255))

        if menu_button.draw(surface):
            status = 'main_menu'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def continue_to_troll(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the continuing to troll screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:

        #background
        surface.fill((0,0,0))
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

def troll_encounter_v1(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the first version of the troll screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True
    frame_width = 64
    frame_height = 64
    frames_in_row = 4
    frame_index = 0
    clock = pygame.time.Clock()

    while run:
        surface.fill((0,0,0))
        bg(surface, images)

        # drawing text
        draw_text_box(surface, 100, 50, 300, 50, (112, 128, 144))
        draw_text(surface, 'TROLL', text_font, (255, 255, 255), 250, 50)

        draw_text_box(surface, 75, 150, 350, 250, (112, 128, 144))
        draw_text(surface,'Thank you friend I shall',text_font,(255,255,255),250,150)
        draw_text(surface,'take these as payment.',text_font,(255,255,255),250,200)
        draw_text(surface,'Now follow, me show you',text_font,(255,255,255),250,250)
        draw_text(surface,'the way to an old pall',text_font,(255,255,255),250,300)
        draw_text(surface,'Press space!',text_font,(255,255,255),250,350)

        #load and draw troll
        troll = pygame.image.load('IDLE_000.png').convert_alpha()
        surface.blit(troll,(200,400))

        #load in dino
        sprite_sheet_dino = pygame.image.load('DinoSprites - doux.png').convert_alpha()
        frames = loading_frames(sprite_sheet_dino, frame_width, frame_height, frames_in_row)
        surface.blit(frames[frame_index], (100, 400))

        # cycle through frames
        frame_index += 1
        if frame_index >= len(frames):
            frame_index = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'ruins_info'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(5)
    pygame.quit()

def troll_encounter_v2(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the second version of the troll screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True
    frame_width = 64
    frame_height = 64
    frames_in_row = 4
    frame_index = 0
    clock = pygame.time.Clock()

    while run:
        surface.fill((0, 0, 0))
        bg(surface, images)

        # drawing text
        draw_text_box(surface, 100, 50, 300, 50, (112, 128, 144))
        draw_text(surface, 'TROLL', text_font, (255, 255, 255), 250, 50)

        draw_text_box(surface, 75, 150, 350, 200, (112, 128, 144))
        draw_text(surface, 'GRRR ME MAKE YOU', text_font, (255, 255, 255), 250, 150)
        draw_text(surface, 'REGRET THISS!!', text_font, (255, 255, 255), 250, 200)
        draw_text(surface, 'Hurry get away!', text_font, (255, 255, 255), 250, 250)
        draw_text(surface, 'Press space!', text_font, (255, 255, 255), 250, 300)

        #draw troll
        troll = pygame.image.load('ATTAK_002.png').convert_alpha()
        surface.blit(troll, (100, 380))

        #draw dino
        sprite_sheet_dino = pygame.image.load('DinoSprites - doux.png').convert_alpha()
        frames = loading_frames(sprite_sheet_dino, frame_width, frame_height, frames_in_row)
        surface.blit(frames[frame_index], (300, 400))

        # cycle through frames
        frame_index += 1
        if frame_index >= len(frames):
            frame_index = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'ruins_info'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(5)
    pygame.quit()

def ruins_info(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the ruins info screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        surface.fill((0,0,0))
        bg(surface,images)

        #drawing text
        draw_text_box(surface,40,50,420,400,(112,128,144))
        draw_text(surface,'You travel to the ruins where',text_font,(255,255,255),250,50)
        draw_text(surface,'you find the keeper who is',text_font,(255,255,255),250,100)
        draw_text(surface,'friends with the troll and is',text_font,(255,255,255),250,150)
        draw_text(surface,'willing to help on one condition',text_font,(255,255,255),250,200)
        draw_text(surface,'OBJ: solve riddles!',text_font,(255,255,255),250,250)
        draw_text(surface,'Press 1,2,or 3 on keyboard to',text_font,(255,255,255),250,300)
        draw_text(surface,'answer the riddles!',text_font,(255,255,255),250,350)
        draw_text(surface,'Press space to continue!',text_font,(255,255,255),250,400)


        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'riddle_one'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def riddle_one(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the first riddle screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        surface.fill((0,0,0))
        bg(surface,images)

        #question code
        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface,'I call myself to solve a task,',text_font,(255,255,255),250,50)
        draw_text(surface,'but without my base case,',text_font,(255,255,255),250,100)
        draw_text(surface,'my effort wont last...',text_font,(255,255,255),250,150)
        draw_text(surface,'What am I?',text_font,(255,255,255),250,200)

        #answer code
        draw_text(surface,'1',text_font,(255,255,255),10,310)
        draw_text_box(surface,10,350,200,40,(112,128,144))
        draw_text(surface,'infinite loop',text_font,(255,255,255),100,350)

        draw_text(surface,'2',text_font,(255,255,255),250,310)
        draw_text_box(surface,250,350,250,40,(112,128,144))
        draw_text(surface,'recursive function',text_font,(255,255,255),375,350)

        draw_text(surface,'3',text_font,(255,255,255),175,430)
        draw_text_box(surface,175,400,150,40,(112,128,144))
        draw_text(surface,'callback',text_font,(255,255,255),250,400)

        #check which number is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    status = 'riddle_ending_for_riddle1'
                    return status
                elif event.key == pygame.K_2:
                    status = 'riddle_two'
                    return status
                elif event.key == pygame.K_3:
                    status = 'riddle_ending_for_riddle1'
                    return status


        pygame.display.update()
    pygame.quit()

def riddle_two(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the second riddle screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        surface.fill((0,0,0))
        bg(surface,images)

        #draw question code
        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface,'Im a home for your code,',text_font,(255,255,255),250,50)
        draw_text(surface,'both public and private,',text_font,(255,255,255),250,100)
        draw_text(surface,'where branches grow, and',text_font,(255,255,255),250,150)
        draw_text(surface,'pull requests unite it,',text_font,(255,255,255),250,200)
        draw_text(surface,'What am I?',text_font,(255,255,255),250,250)

        #answers
        draw_text(surface, '1', text_font, (255, 255, 255), 50, 310)
        draw_text_box(surface, 50, 350, 150, 40, (112, 128, 144))
        draw_text(surface, 'Bitbucket', text_font, (255, 255, 255), 125, 350)

        draw_text(surface,'2',text_font,(255,255,255),300,310)
        draw_text_box(surface, 300, 350, 150, 40, (112, 128, 144))
        draw_text(surface, 'Git', text_font, (255, 255, 255), 375, 350)

        draw_text(surface,'3',text_font,(255,255,255),175,430)
        draw_text_box(surface, 175, 400, 150, 40, (112, 128, 144))
        draw_text(surface, 'Github', text_font, (255, 255, 255), 250, 400)

        #check which one selected
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    status = 'riddle_ending_for_riddle2'
                    return status
                elif event.key == pygame.K_2:
                    status = 'riddle_ending_for_riddle2'
                    return status
                elif event.key == pygame.K_3:
                    status = 'continue'
                    return status

        pygame.display.update()
    pygame.quit()

def troll_riddle(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the troll riddle screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        surface.fill((0,0,0))
        bg(surface, images)

        #draw troll riddle question
        draw_text_box(surface, 50, 50, 400, 250, (112, 128, 144))
        draw_text(surface, 'Troll riddle', text_font, (255, 255, 255), 250, 0)
        draw_text(surface,'I am always running, but I',text_font,(255,255,255),250,50)
        draw_text(surface,'never move. I have a head',text_font,(255,255,255),250,100)
        draw_text(surface,'but no body. I can crash,',text_font,(255,255,255),250,150)
        draw_text(surface,'but I never bleed.',text_font,(255,255,255),250,200)
        draw_text(surface,'What am I..?',text_font,(255,255,255),250,250)

        #draw answers
        draw_text(surface, '1', text_font, (255, 255, 255), 50, 310)
        draw_text_box(surface, 50, 350, 150, 40, (112, 128, 144))
        draw_text(surface, 'A loop', text_font, (255, 255, 255), 125, 350)

        draw_text(surface,'2',text_font,(255,255,255),300,310)
        draw_text_box(surface, 300, 350, 150, 40, (112, 128, 144))
        draw_text(surface, 'A program', text_font, (255, 255, 255), 375, 350)

        draw_text(surface,'3',text_font,(255,255,255),175,430)
        draw_text_box(surface, 175, 400, 150, 40, (112, 128, 144))
        draw_text(surface, 'A stack', text_font, (255, 255, 255), 250, 400)

        #check which answers is chosen
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    status = 'riddle_ending_for_troll_riddle'
                    return status
                elif event.key == pygame.K_2:
                    status = 'keeper_encounter'
                    return status
                elif event.key == pygame.K_3:
                    status = 'riddle_ending_for_troll_riddle'
                    return status

        pygame.display.update()
    pygame.quit()

def riddle_ending_for_riddle1(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the ending screen if you get riddle 1 wrong

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        # background
        surface.fill((0,0,0))
        bg(surface, images)

        # text and box for game over
        draw_text_box(surface, 100, 50, 300, 100, (112, 128, 144))
        draw_text(surface, 'Game Over!', text_font, (255, 255, 255), 250, 75)

        # code for death text
        draw_text(surface, 'Hmm maybe pay more', text_font, (255, 255, 255), 250, 200)
        draw_text(surface, 'attention in class..', text_font, (255, 255, 255), 250, 250)

        # code for menu button
        go_back_button = Button((surface.get_width() // 2 - 80), 350, 150, 50, (112, 128, 144), 'Go back :)', text_font,
                             (255, 255, 255))

        if go_back_button.draw(surface):
            status = 'riddle_one'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def riddle_ending_for_riddle2(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the ending screen if you get riddle 2 wrong

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        # background
        surface.fill((0,0,0))
        bg(surface, images)

        # text and box for game over
        draw_text_box(surface, 100, 50, 300, 100, (112, 128, 144))
        draw_text(surface, 'Game Over!', text_font, (255, 255, 255), 250, 75)

        # code for death text
        draw_text(surface, 'Really? Second times the', text_font, (255, 255, 255), 250, 200)
        draw_text(surface, 'charm I guess? ._.', text_font, (255, 255, 255), 250, 250)

        # code for menu button
        go_back_button = Button((surface.get_width() // 2 - 80), 350, 150, 50, (112, 128, 144), 'Go back :)', text_font,
                             (255, 255, 255))

        if go_back_button.draw(surface):
            status = 'riddle_two'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def riddle_ending_for_troll_riddle(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the ending screen if you get the troll riddle wrong

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        # background
        surface.fill((0,0,0))
        bg(surface, images)

        # text and box for game over
        draw_text_box(surface, 100, 50, 300, 100, (112, 128, 144))
        draw_text(surface, 'Game Over!', text_font, (255, 255, 255), 250, 75)

        # code for death text
        draw_text(surface, 'Thats what you get for not giving', text_font, (255, 255, 255), 250, 150)
        draw_text(surface, 'me your headphones hehe :p', text_font, (255, 255, 255), 250, 200)
        draw_text(surface, 'now go back to start!', text_font, (255, 255, 255), 250, 250)
        draw_text(surface,'mwahahaha',text_font,(255,255,255),250,300)

        # code for menu button
        go_back_button = Button((surface.get_width() // 2 - 80), 350, 150, 50, (112, 128, 144), 'Go back :)', text_font,
                             (255, 255, 255))

        if go_back_button.draw(surface):
            status = 'main_menu'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()

def keeper_encounter(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the keeper encounter screen

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True
    frame_width = 64
    frame_height = 64
    frames_in_row = 4
    frame_index = 0
    clock = pygame.time.Clock()

    while run:
        surface.fill((0, 0, 0))
        bg(surface, images)

        # load in ghost
        sprite_sheet = pygame.image.load('Mr.Ghost_Idle.png').convert_alpha()

        #draw textbox and text
        draw_text_box(surface, 100, 50, 300, 50, (112, 128, 144))
        draw_text(surface, 'Ruins keeper', text_font, (255, 255, 255), 250, 50)

        draw_text_box(surface,75,150,350,200,(112,128,144))
        draw_text(surface,'Good job on passing the',text_font,(255,255,255),250,150)
        draw_text(surface,'riddles! As promised here',text_font,(255,255,255),250,200)
        draw_text(surface,'is the code: XIT',text_font,(255,255,255),250,250)
        draw_text(surface,'Press space to use code!',text_font,(255,255,255),250,300)

        #draw in ghost
        frames_for_ghost = loading_frames(sprite_sheet, frame_width, frame_height, frames_in_row)
        surface.blit(frames_for_ghost[frame_index], (200, 400))

        #code to animate ghost
        frame_index += 1
        if frame_index >= len(frames_for_ghost):
            frame_index = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    status = 'win_screen'
                    return status

            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
        clock.tick(5)
    pygame.quit()

def win_screen(surface:pygame.Surface, images:list[pygame.Surface]) -> str:
    """
    This function provides the code for the win screen at the end

    Args:
        surface: the screen that the menu will be on
        images: the list of bg images for the game

    Returns:
        str: returns status of next screen
    """
    run = True

    while run:
        surface.fill((0,0,0))
        bg(surface,images)

        #draw in celebration text and textbox
        draw_text_box(surface, 100, 50, 300, 100, (112, 128, 144))
        draw_text(surface,'Congrats!',text_font,(255,255,255),250,50)
        draw_text(surface,'You Win!!!',text_font,(255,255,255),250,100)
        draw_text(surface,'You obtained the code and made',text_font,(255,255,255),250,200)
        draw_text(surface,'it back to your world!',text_font,(255,255,255),250,250)
        draw_text(surface,'The End!',text_font,(255,255,255),250,300)

        #draw in menu button
        menu_button = Button((surface.get_width() // 2 - 50), 400, 100, 50, (112, 128, 144), 'Menu', text_font,(255, 255, 255))

        if menu_button.draw(surface):
            status = 'main_menu'
            return status

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()
    pygame.quit()