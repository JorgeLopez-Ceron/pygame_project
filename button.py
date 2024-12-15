#file that contains the button class
import pygame

class Button:
    def __init__(self, x:int, y:int, width:int, height:int, color:tuple[int,int,int], text:str, font:pygame.font.Font, text_color:tuple[int,int,int]) -> None:
        """
        This class creates a button using args

        Args:
            x: the x coord of the button
            y: the y coord of the button
            width: how wide you want the button
            height: the height you want the button
            color: what color you want the button to be
            text: what you want written on the button
            font: what font you want to use to render the text
            text_color: what color you want the text to be

        """
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.font = font
        self.text_color = text_color
        self.clicked = False

    def draw(self,surface:pygame.Surface) -> bool:
        """
        Draws the button on the screen and checks to see if it's been clicked

        Args:
            surface: the screen you want the button to be on

        Returns:
            bool: True if the button is clicked else False
        """
        #draw button
        pygame.draw.rect(surface, self.color, self.rect)

        #draw text on buttons
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)
        surface.blit(text_surface, text_rect)

        action = False
        #grabs mouse position
        pos = pygame.mouse.get_pos()

        #check for click
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action

