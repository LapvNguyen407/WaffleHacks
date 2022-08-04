import os
import pygame

SCREEN_HEIGHT = 1536
SCREEN_WIDTH = 864
WIN = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
pygame.display.set_caption("practice screen")
print(WIN.get_size())

WHITE = (255,255,255)
FPS = 60

background_image = pygame.image.load(os.path.join('resource', 'background.png')) #load an image as a surface
button_image = pygame.image.load(os.path.join('resource', 'button_mood_submit.png')).convert_alpha() #load an image, convert alpha preserves transparency
button_xy = (500,500)
button_rect = button_image.get_rect(topleft = button_xy)

def draw_image(image, xy):
    WIN.blit(image, xy) #Screen.blit(image, (x,y))


def draw_bg(color):
    WIN.fill(color) #fill the window with color, color is a tuple variable (R,G,B)


def draw_rect():
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.rect(WIN, (200,200,200), pygame.Rect(100,100,150,150))
    

def draw_line():
    #pygame.draw.rect(surface, color, pygame.Rect(30, 30, 60, 60))
    pygame.draw.line(WIN, (0,0,0), (0,0), (600,100), 6)
    


def main():
    clock = pygame.time.Clock()
    run = True
    while run: #main loop that runs every frame
        clock.tick(FPS) #controls the update speed of the program
        for event in pygame.event.get(): #Checks all pygame events every frane
            if event.type == pygame.QUIT: #If the user quits the program
                run = False #Stop running
            if event.type == pygame.QUIT or ( event.type == pygame.KEYDOWN and event.key == pygame.K_1): #If the player clicks X button, or presses keyboard 1 (the 1 key)
                pygame.quit() #quit
                exit() #terminate
            if event.type == pygame.MOUSEBUTTONDOWN: #If the user clicked 
                if(button_rect.collidepoint(event.pos)): #and the position of the click collides with the x_y for the button
                    pygame.quit() #quit
                    exit() #terminate

       
        draw_bg(WHITE) 
        draw_image(background_image, (0,0))
        draw_image(button_image, button_xy)
        draw_rect()
        draw_line()
        
        pygame.display.flip()#This updates the screen to show all changes     
        
    pygame.quit()

#__name__ prevents python from running file whenever it is imported by other files
if __name__ == "__main__":
    main()