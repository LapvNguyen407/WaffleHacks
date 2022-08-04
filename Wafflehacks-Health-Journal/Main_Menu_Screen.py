import os
import pygame

from pathlib import Path

pygame.init()

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("main menu screen")
cozyfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf', 36)
app_title = pygame.font.Font('resource\CooperFiveOpti-Black.otf', 110)

WHITE = (255,255,255)
FPS = 60

background_image = pygame.image.load("resource\\background.png") #load an image as a surface

text_bg = pygame.image.load("resource\\text_background.png").convert_alpha() #load an image, convert alpha preserves transparency


button_analyze = pygame.image.load("resource\\button_analyze.png").convert_alpha() #load an image, convert alpha preserves transparency
button_analyze_xy = (130,630)
button_analyze_rect = button_analyze.get_rect(topleft = button_analyze_xy)

button_quit = pygame.image.load("resource\\button_back.png").convert_alpha() #load an image, convert alpha preserves transparency
button_quit_xy = (1070,630)
button_quit_rect = button_analyze.get_rect(topleft = button_quit_xy)



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

def display_main_menu_screen(random_quote, show_journal_button):
    clock = pygame.time.Clock()
    run = True
    if(show_journal_button):
        button_journal = pygame.image.load("resource\\button_journal.png").convert_alpha() #load an image, convert alpha preserves transparency   
    else:
        button_journal = pygame.image.load("resource\\button_journal_grey.png").convert_alpha() #load an image, convert alpha preserves transparency
    
    button_journal_xy = (600,630)
    button_journal_rect = button_analyze.get_rect(topleft = button_journal_xy)

    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate
            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
                if(button_analyze_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    return ("analyze")
            if event.type == pygame.MOUSEBUTTONDOWN and show_journal_button: #If the user clicked 
                if(button_journal_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    return ("journal")
            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
                if(button_quit_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    return "quit"

       
        draw_bg(WHITE) 
        draw_image(background_image, (0,0))
        draw_image(button_analyze, button_analyze_xy)
        
        draw_image(button_journal, button_journal_xy)
        
        draw_image(button_quit, button_quit_xy)
        text_bg_xy = (110,350)
        draw_image(text_bg, text_bg_xy)
        render_text(random_quote, (125, 360), 57)

        title_text = app_title.render("HEALTH HACKER", True, (pygame.Color("#cbb397ff")))
        WIN.blit(title_text, (165, 90))
        
        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

if __name__ == "__main__":
    display_main_menu_screen("Placeholder random quote for testing purposes asdfasdf. Placeholder random quote for testing purposes asdf. Placeholder random quote for testing purposes asdfasdfasdf. Placeholder random quote for testing purposes. ", False)