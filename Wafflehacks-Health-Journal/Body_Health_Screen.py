import pygame
from pygame import display, image
from Main_Menu_Screen import render_text
from jentry import Jentry

pygame.init()

SCREEN_HEIGHT = 864
SCREEN_WIDTH = 1536
WIN = display.set_mode((0,0), pygame.FULLSCREEN)
display.set_caption("mental health screen")
labelfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf', 95)
cozyfont = pygame.font.Font('resource\CooperFiveOpti-Black.otf', 42)

WHITE = (255,255,255)
FPS = 60

background_image = pygame.image.load("resource\\background.png")
hover_bg = pygame.image.load("resource\\hover_background.png").convert_alpha()

# {MIND_BUTTON}
mind_button_image = pygame.image.load("resource\\tab_mind_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
mind_button_xy = (40,30)
mind_button = mind_button_image.get_rect(topleft = mind_button_xy)

# {BODY_BUTTON}
body_button_image = pygame.image.load("resource\\tab_body_selected.png").convert_alpha() #load an image, convert alpha preserves transparency
body_button_xy = (540,30)
body_button = body_button_image.get_rect(topleft = body_button_xy)

# {JOURNAL_BUTTON}
journal_button_image = pygame.image.load("resource\\tab_journal_unselected.png").convert_alpha() #load an image, convert alpha preserves transparency
journal_button_xy = (1040,30)
journal_button = journal_button_image.get_rect(topleft = journal_button_xy)

# {ROW IDENTIFIERS}
exercise_image = pygame.image.load("resource\\icon_exercise_unselected.png").convert_alpha()
exercise_logo_xy = (40,240)
exercise_logo_button = exercise_image.get_rect(topleft = exercise_logo_xy)
diet_image = pygame.image.load("resource\\icon_diet_unselected.png").convert_alpha()
diet_logo_xy = (40,440)
diet_logo_button = diet_image.get_rect(topleft = diet_logo_xy)
sleep_image = pygame.image.load("resource\\icon_sleep_unselected.png").convert_alpha()
sleep_logo_xy = (40,640)
sleep_logo_button = sleep_image.get_rect(topleft = sleep_logo_xy)

########################################################
#               Number buttons here                    #
########################################################

exercise_buttons = []
exercise_xy = []
diet_buttons = []
diet_xy = []
sleep_buttons = []
sleep_xy = []

button_images_up = []
button_images_down = []

# {BUTTON UP GRAPHICS}
button_images_up.append(image.load("resource\\button_0_unselected.png").convert_alpha())
button_images_up.append(image.load("resource\\button_1_unselected.png").convert_alpha())
button_images_up.append(image.load("resource\\button_2_unselected.png").convert_alpha())
button_images_up.append(image.load("resource\\button_3_unselected.png").convert_alpha())

button_images_down.append(image.load("resource\\button_0_selected.png").convert_alpha())
button_images_down.append(image.load("resource\\button_1_selected.png").convert_alpha())
button_images_down.append(image.load("resource\\button_2_selected.png").convert_alpha())
button_images_down.append(image.load("resource\\button_3_selected.png").convert_alpha())

# {exercise BUTTONS [x] = 810, 990, 1170, 1350 --> [y] = 236 }
exercise_xy.append((810,236))
exercise_buttons.append(button_images_up[0].get_rect(topleft = exercise_xy[0]))
exercise_xy.append((990,236))
exercise_buttons.append(button_images_up[1].get_rect(topleft = exercise_xy[1]))
exercise_xy.append((1170,236))
exercise_buttons.append(button_images_up[2].get_rect(topleft = exercise_xy[2]))
exercise_xy.append((1350,236))
exercise_buttons.append(button_images_up[3].get_rect(topleft = exercise_xy[3]))

# {ENERGY BUTTONS [x] = 810, 990, 1170, 1350 --> [y] = 436 }
diet_xy.append((810,436))
diet_buttons.append(button_images_up[0].get_rect(topleft = diet_xy[0]))
diet_xy.append((990,436))
diet_buttons.append(button_images_up[1].get_rect(topleft = diet_xy[1]))
diet_xy.append((1170,436))
diet_buttons.append(button_images_up[2].get_rect(topleft = diet_xy[2]))
diet_xy.append((1350,436))
diet_buttons.append(button_images_up[3].get_rect(topleft = diet_xy[3]))

# {TIME BUTTONS [x] = 810, 990, 1170, 1350 --> [y] = 636 }
sleep_xy.append((810,636))
sleep_buttons.append(button_images_up[0].get_rect(topleft = sleep_xy[0]))
sleep_xy.append((990,636))
sleep_buttons.append(button_images_up[1].get_rect(topleft = sleep_xy[1]))
sleep_xy.append((1170,636))
sleep_buttons.append(button_images_up[2].get_rect(topleft = sleep_xy[2]))
sleep_xy.append((1350,636))
sleep_buttons.append(button_images_up[3].get_rect(topleft = sleep_xy[3]))

# {BACK_BUTTON}
# back_button_image = pygame.image.load("resource\\icon_back_arrow.png").convert_alpha()
# back_button_xy = (1389,18)
# back_button = back_button_image.get_rect(topleft = back_button_xy)


def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))

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

def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)
        

def display_body_screen(today_jentry):
    clock = pygame.time.Clock()
    run = True
    exercise_selection = False
    diet_selection = False
    sleep_selection = False
    exercise_value = 0

    if(today_jentry.get_value("Exercise") != 404):
        exercise_selection = True
        exercise_value = today_jentry.get_value("Exercise")

    if(today_jentry.get_value("Diet") != 404):
        diet_selection = True
        diet_value = today_jentry.get_value("Diet")

    if(today_jentry.get_value("Sleep") != 404):
        sleep_selection = True
        sleep_value = today_jentry.get_value("Sleep")

    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frame
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running

            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate

            if event.type == pygame.MOUSEBUTTONDOWN:
                if(mind_button.collidepoint(event.pos)):
                    return ("mind")

                if(journal_button.collidepoint(event.pos)):
                    return ("journal")
                
                for i in range(4):
                    if(exercise_buttons[i].collidepoint(event.pos)):
                        exercise_selection = True
                        exercise_value = i
                        today_jentry.set_value("Exercise", i)

                for i in range(4):
                    if(diet_buttons[i].collidepoint(event.pos)):
                        diet_selection = True
                        diet_value = i
                        today_jentry.set_value("Diet", i)

                for i in range(4):
                    if(sleep_buttons[i].collidepoint(event.pos)):
                        sleep_selection = True
                        sleep_value = i
                        today_jentry.set_value("Sleep", i)



        draw_image(background_image, (0,0))
        draw_image(mind_button_image, mind_button_xy)
        draw_image(body_button_image, body_button_xy)
        draw_image(journal_button_image, journal_button_xy)

        # draw exercise
        for i in range(4):
            draw_image(button_images_up[i], exercise_xy[i])

        #draw diet
        for i in range(4):
            draw_image(button_images_up[i], diet_xy[i])
        
        #draw sleep
        for i in range(4):
            draw_image(button_images_up[i], sleep_xy[i])

        #draw exercise button pressed
        if (exercise_selection):
            draw_image(button_images_down[exercise_value], exercise_xy[exercise_value])

        #draw diet button pressed
        if (diet_selection):
            draw_image(button_images_down[diet_value], diet_xy[diet_value])

        #draw sleep button pressed
        if (sleep_selection):
            draw_image(button_images_down[sleep_value], sleep_xy[sleep_value])

        draw_image(exercise_image, exercise_logo_xy)
        draw_image(diet_image, diet_logo_xy)
        draw_image(sleep_image, sleep_logo_xy)
        #draw_image(back_button_image, back_button_xy)
        
        exercise_label_text = labelfont.render("Exercise:", True, (pygame.Color("#cbb397ff")))
        WIN.blit(exercise_label_text, (224, 241))
        
        diet_label_text = labelfont.render("Diet:", True, (pygame.Color("#cbb397ff")))
        WIN.blit(diet_label_text, (224, 441))
        
        freesleep_label_text = labelfont.render("Sleep:", True, (pygame.Color("#cbb397ff")))
        WIN.blit(freesleep_label_text, (224, 641))

        for i in range(10):
            if(exercise_logo_button.collidepoint(pygame.mouse.get_pos())):
                mouse_xy = pygame.mouse.get_pos()
                mouse_xy = ((mouse_xy[0] + 40), (mouse_xy[1] + 10))

                WIN.blit(pygame.transform.scale(hover_bg, (600, 125)), pygame.mouse.get_pos())
                words = cozyfont.render(render_text("How much exercise have you had today?", mouse_xy, 20), True, (255,255,255))
                WIN.blit(words, mouse_xy)

            if(diet_logo_button.collidepoint(pygame.mouse.get_pos())):
                mouse_xy = pygame.mouse.get_pos()
                mouse_xy = ((mouse_xy[0] + 40), (mouse_xy[1] + 10))

                WIN.blit(pygame.transform.scale(hover_bg, (620, 125)), pygame.mouse.get_pos())
                words = cozyfont.render(render_text("How healthy did you eat today?", mouse_xy, 20), True, (255,255,255))
                WIN.blit(words, mouse_xy)

            if(sleep_logo_button.collidepoint(pygame.mouse.get_pos())):
                mouse_xy = pygame.mouse.get_pos()
                mouse_xy = ((mouse_xy[0] + 40), (mouse_xy[1] + 10))

                WIN.blit(pygame.transform.scale(hover_bg, (620, 125)), pygame.mouse.get_pos())
                words = cozyfont.render(render_text("How much sleep have you gotten today?", mouse_xy, 20), True, (255,255,255))
                WIN.blit(words, mouse_xy)

        pygame.display.flip() # This updates the screen to show all changes     
        
    pygame.quit()

if __name__ == "__main__":
    display_body_screen()