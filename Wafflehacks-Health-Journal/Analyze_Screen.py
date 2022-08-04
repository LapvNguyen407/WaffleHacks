import os
import pygame
from jentry import Jentry
from pathlib import Path
from datetime import datetime
from datetime import timedelta

from journal import Journal

pygame.init()

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("main menu screen")
cozyfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf',  30)

WHITE = (255,255,255)
FPS = 60

#testJentry = Jentry(mood, social, energy, freetime, exercise, diet, sleep, menstruation, journal)

# testJentry = Jentry("06/18/22",2, 1, 3, 1,3,2,3,False,"This Jentry is for testing")
# test_journal_jentries = ["06/18/22|10|1|1|2|0|3|2|False|more strings to test".split("|"),
# "06/17/22|8|1|1|2|0|3|2|False|test string for app".split("|"),
# "06/16/22|6|2|2|2|0|3|2|False|Might test string 1".split("|"),
# "06/15/22|4|1|3|1|0|3|3|True|Might test string 3".split("|"),
# "06/14/22|2|3|3|2|1|3|2|True|Might test string 4".split("|"),
# "06/13/22|0|3|2|3|2|3|1|True|Might test string 5".split("|"),
# "06/12/22|3|2|1|2|3|2|2|True|Might test string 6".split("|"),
# "06/11/22|2|1|3|2|3|2|1|True|Might test string 7".split("|"),
# "06/10/22|1|0|2|1|2|3|1|False|Might test string 8".split("|"),
# "06/09/22|1|1|1|2|0|3|2|False|Might delete this ap".split("|")]

# test_journal = Journal(test_journal_jentries)


background_image = pygame.image.load("resource\\background.png") #load an image as a surface

img_axis = pygame.image.load("resource\\axis_week.png").convert_alpha() #load an image, convert alpha preserves transparency
axis_xy = (113,79)

graph_data_point = pygame.image.load("resource\\graph_data_point.png").convert_alpha()
graph_blue_bar = pygame.image.load("resource\\graph_bar_blue.png").convert_alpha()
graph_green_bar = pygame.image.load("resource\\graph_bar_green.png").convert_alpha()
graph_red_bar = pygame.image.load("resource\\graph_bar_red.png").convert_alpha()

text_one = pygame.image.load("resource\\text_one.png").convert_alpha()
text_ten = pygame.image.load("resource\\text_ten.png").convert_alpha()

icon_period_s = pygame.image.load("resource\\icon_period_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_period_u = pygame.image.load("resource\\icon_period_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_period_xy = (1250,0)
icon_period_rect = icon_period_u.get_rect(topleft = icon_period_xy)

icon_back_arrow = pygame.image.load("resource\\icon_back_arrow.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_back_arrow_xy = (1394,0)
icon_back_arrow_rect = icon_back_arrow.get_rect(topleft = icon_back_arrow_xy)

icon_social_s = pygame.image.load("resource\\icon_social_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_social_u = pygame.image.load("resource\\icon_social_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_social_xy = (1250,144)
icon_social_rect = icon_social_u.get_rect(topleft = icon_social_xy)

icon_exercise_s = pygame.image.load("resource\\icon_exercise_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_exercise_u = pygame.image.load("resource\\icon_exercise_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_exercise_xy = (1394,144)
icon_exercise_rect = icon_exercise_u.get_rect(topleft = icon_exercise_xy)

icon_time_s = pygame.image.load("resource\\icon_time_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_time_u = pygame.image.load("resource\\icon_time_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_time_xy = (1250,288)
icon_time_rect = icon_time_u.get_rect(topleft = icon_time_xy)

icon_diet_s = pygame.image.load("resource\\icon_diet_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_diet_u = pygame.image.load("resource\\icon_diet_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_diet_xy = (1394,288)
icon_diet_rect = icon_diet_u.get_rect(topleft = icon_diet_xy)

icon_energy_s = pygame.image.load("resource\\icon_energy_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_energy_u = pygame.image.load("resource\\icon_energy_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_energy_xy = (1250,432)
icon_energy_rect = icon_energy_u.get_rect(topleft = icon_energy_xy)

icon_sleep_s = pygame.image.load("resource\\icon_sleep_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_sleep_u = pygame.image.load("resource\\icon_sleep_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_sleep_xy = (1394,432)
icon_sleep_rect = icon_sleep_u.get_rect(topleft = icon_sleep_xy)

icon_move_backward = pygame.image.load("resource\\icon_move_backward.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_move_backward_xy = (1250,576)
icon_move_backward_rect = icon_back_arrow.get_rect(topleft = icon_move_backward_xy)

icon_move_forward = pygame.image.load("resource\\icon_move_forward.png").convert_alpha() #load an image, convert alpha preserves transparency
icon_move_forward_xy = (1394,576)
icon_move_forward_rect = icon_back_arrow.get_rect(topleft = icon_move_forward_xy)

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

def display_navigation(stat_selected, timespan, period_selected):
    draw_image(icon_back_arrow, icon_back_arrow_xy)

    if(stat_selected == "Social"):
        draw_image(icon_social_s, icon_social_xy)
    else:
        draw_image(icon_social_u, icon_social_xy)

    if(stat_selected == "Exercise"):
        draw_image(icon_exercise_s, icon_exercise_xy)
    else:
        draw_image(icon_exercise_u, icon_exercise_xy)
    if(stat_selected == "Freetime"):
        draw_image(icon_time_s, icon_time_xy)
    else:
        draw_image(icon_time_u, icon_time_xy)
    if(stat_selected == "Diet"):
        draw_image(icon_diet_s, icon_diet_xy)
    else:
        draw_image(icon_diet_u, icon_diet_xy)
    if(stat_selected == "Energy"):
        draw_image(icon_energy_s, icon_energy_xy)
    else:
        draw_image(icon_energy_u, icon_energy_xy)
    if(stat_selected == "Sleep"):
        draw_image(icon_sleep_s, icon_sleep_xy)
    else:
        draw_image(icon_sleep_u, icon_sleep_xy)
    draw_image(icon_move_backward, icon_move_backward_xy)
    draw_image(icon_move_forward, icon_move_forward_xy)

def graph_line(current_week):
    #37/40 
    x = []
    y = []
    i=0
    for day in current_week:
        x.append((179)+(152*i))
        y.append((684)-(day.get_value("Mood")*62))
        i+=1
    plot_line(x,y)
    plot_points(x,y)
    plot_dates(current_week)

def plot_line(x,y):
    for i in range(len(x)):
        if(i+1 < len(x)):
            if(y[i+1] != 684):
                pygame.draw.line(WIN, pygame.Color("#ffcc00ff"), (x[i]+16,y[i]+20), ((x[i+1]+16,y[i+1]+20)), 6)

def plot_points(x,y):
    for i in range(len(x)):
        if(y[i] != 684):
            draw_image(graph_data_point, (x[i],y[i]))


def plot_dates(current_week):
    x = 120
    y = 750
    for day in current_week:
        label = cozyfont.render(day.get_value("Date")[:5], True, pygame.Color("#4b4d26ff"))
        WIN.blit(label, (x,y))
        x += 155
    
    


def graph_stat(stat_selected, current_week):
    i=0
    for day in current_week:
        bars = day.get_value(stat_selected)
        if(bars != 0):
            xy = (123, 499)
            draw_bar_graph(bars,(xy[0] + (152*i) ,xy[1]))
        i += 1

def draw_bar_graph(bars, xy):
    if(bars == 1):
        graph_bar = graph_red_bar
    elif(bars == 2):
        graph_bar = graph_green_bar
    elif(bars == 3):
        graph_bar=graph_blue_bar
    for i in range(bars):
        draw_image(graph_bar, (xy[0], xy[1]- (i*207)))

def populate_week(journal):
    #datetime.now().strftime("%x")
    week = []
    today = datetime.today()
    for i in range(7):
        print(journal.get_jentry(today.strftime("%x")))
        if(journal.has_jentry(today.strftime("%x"))):
            print("got past first if")
            if(journal.get_sum(journal.get_jentry(today.strftime("%x"))) < 100 ):
                week.append(journal.get_jentry(today.strftime("%x")))
            else:
                week.append(Jentry(today.strftime("%x"),0,0,0,0,0,0,0,False,"No entry for today"))
        today = today - timedelta(days = 1)
    week.reverse()
    return week

def display_analyze_screen(journal):
    clock = pygame.time.Clock()
    run = True
    stat_selected = ""
    timespan = "Week"
    period_selected = False
    current_week = populate_week(journal)



    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate
            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
                #print(event.pos)
                if(icon_period_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    period_selected = not period_selected
                if(icon_back_arrow_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    return "back"
                if(icon_social_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    if(stat_selected == "Social"):
                        stat_selected = ""
                    else:
                        stat_selected = "Social"
                if(icon_exercise_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    if(stat_selected == "Exercise"):
                        stat_selected = ""
                    else:
                        stat_selected = "Exercise"
                if(icon_time_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    if(stat_selected == "Freetime"):
                        stat_selected = ""
                    else:
                        stat_selected = "Freetime"
                if(icon_diet_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    if(stat_selected == "Diet"):
                        stat_selected = ""
                    else:
                        stat_selected = "Diet"
                if(icon_energy_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    if(stat_selected == "Energy"):
                        stat_selected = ""
                    else:
                        stat_selected = "Energy"
                if(icon_sleep_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    if(stat_selected == "Sleep"):
                        stat_selected = ""
                    else:
                        stat_selected = "Sleep"
                # if(icon_month_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                #     timespan = "Month"
                # if(icon_week_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                #     timespan = "Week"
                


        draw_image(background_image, (0,0))
        ######### DISPLAY GRAPH ############
        
        if(stat_selected != ""):
            graph_stat(stat_selected, current_week)
        draw_image(img_axis, axis_xy)
        graph_line(current_week)
        draw_image(text_one, (40, 670))
        draw_image(text_ten, (10, 79))

        

        ######### DISPLAY NAVIGATION #########
        display_navigation(stat_selected, timespan, period_selected)


        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

if __name__ == "__main__":
    display_analyze_screen(test_journal)