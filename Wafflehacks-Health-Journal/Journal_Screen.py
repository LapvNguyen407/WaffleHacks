import os
import pygame

from pathlib import Path
from jentry import Jentry

pygame.init()

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("journal screen")
cozyfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf',  36)

WHITE = (255,255,255)
FPS = 60

background_image = pygame.image.load("resource\\background.png") #load an image as a surface
text_bg = pygame.image.load("resource\\journal_background.png").convert_alpha() #load an image, convert alpha preserves transparency

# {MIND_BUTTON}
mind_button_image = pygame.image.load("resource\\tab_mind_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
mind_button_xy = (40,30)
mind_button = mind_button_image.get_rect(topleft = mind_button_xy)

# {BODY_BUTTON}
body_button_image = pygame.image.load("resource\\tab_body_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
body_button_xy = (540,30)
body_button = body_button_image.get_rect(topleft = body_button_xy)

# {JOURNAL_BUTTON}
journal_button_image = pygame.image.load("resource\\tab_journal_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
journal_button_xy = (1040,30)
journal_button = journal_button_image.get_rect(topleft = journal_button_xy)

button_back = pygame.image.load("resource\\icon_back_arrow.png").convert_alpha() #load an image, convert alpha preserves transparency
button_back_xy = (8,714)
button_back_rect = button_back.get_rect(topleft = button_back_xy)

button_submit = pygame.image.load("resource\\button_submit.png").convert_alpha() #load an image, convert alpha preserves transparency
button_submit_xy = (500,730)
button_submit_rect = button_submit.get_rect(topleft = button_submit_xy)




def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))


def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)


def draw_rect(color, rectangle):
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(WIN, color, rectangle, 70 , 15)
    pygame.draw.rect(WIN, color, rectangle, 2 , 3)
    

def draw_line():
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.line(WIN, (0,0,0), (0,0), (600,100), 6)

def render_text(message, xy, line_length):
    lines = [""]
    index = 0
    running_total = 0
    for word in message.split():
        if(running_total + len(word) < line_length):
            lines[index] += word + " "
            running_total += len(word)+1
        else:
            index += 1
            lines.append("")
            lines[index] += word + " "
            running_total = len(word)+1
    x = xy[0]
    y = xy[1]
    for each in lines:
        words = cozyfont.render(each, True, (255,255,255))
        WIN.blit(words, (x,y))
        y += 40


def display_journal_screen(todays_jentry):
    clock = pygame.time.Clock()
    run = True
    
    journal_text = todays_jentry.get_value("Journal")
    # if(show_journal_button):
    #     button_journal = pygame.image.load("resource\\button_journal.png").convert_alpha() #load an image, convert alpha preserves transparency   
    # else:
    #     button_journal = pygame.image.load("resource\\button_journal_grey.png").convert_alpha() #load an image, convert alpha preserves transparency
    
    # button_journal_xy = (600,630)
    # button_journal_rect = button_back.get_rect(topleft = button_journal_xy)

    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running

            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked
                if(mind_button.collidepoint(event.pos)):
                    return ("mind")

                if(body_button.collidepoint(event.pos)):
                    return ("body")

                if(button_back_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    return ("back")

                if(button_submit_rect.collidepoint(event.pos)):
                    todays_jentry.set_value("Journal", journal_text)
                    return ("submit")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                        journal_text = journal_text[:-1]
                        todays_jentry.set_value("Journal", journal_text)
                else:
                    journal_text += event.unicode
                    todays_jentry.set_value("Journal", journal_text)


       
        draw_bg(WHITE) 
        draw_image(background_image, (0,0))
        draw_image(mind_button_image, mind_button_xy)
        draw_image(body_button_image, body_button_xy)
        draw_image(journal_button_image, journal_button_xy)
        draw_image(button_back, button_back_xy)
        
        text_bg_xy = (110,225)
        draw_image(text_bg, text_bg_xy)
        render_text(journal_text, (145, 240), 55)

        draw_image(button_submit, button_submit_rect)
        
        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

if __name__ == "__main__":
    display_journal_screen(Jentry("06/18/22",2, 1, 3, 1,3,2,3,False,"This Jentry is for testing"))