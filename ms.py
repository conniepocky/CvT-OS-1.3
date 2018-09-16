import pygame
import time
import random
import sys
pygame.init()

display_width = 800
display_height = 600
#music
music = pygame.mixer.Sound("sounds/sounds/adventure capitalist music.wav")

#colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
GREY = (128,128,128)
GREEN = (0,255,0)
#player width
ship_width = 73
gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Meteor Shower')
clock = pygame.time.Clock()
explode = pygame.mixer.Sound("ex.wav")
carImg = pygame.image.load("ship.png")
def meh(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Avoided:"+str(count), True, GREEN)
    gameDisplay.blit(text, (0,0))
def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])
def car(x,y):
    gameDisplay.blit(carImg,(x,y))
def crash():
    message_display('You Crashed')

def text_objects(text, font):
    textSurface = font.render(text, True, GREEN)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()
    explode.play()
    time.sleep(2)

    game_loop()
def thing(thing1x, thing1y, thing1w, thing1h, color1):
    pygame.draw.rect(gameDisplay, color1, [thing1x, thing1y, thing1w, thing1h])
def game_loop():
    music.stop()
    music.play()
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0
    #second block
    thing_startx = random.randrange(400, display_width)
    thing_starty = -600
    thing_speed = 10
    thing_width = 100
    thing_height = 100
    #1st block
    thing1_startx = random.randrange(0, 400)
    thing1_starty = -600
    thing1_speed = 7
    thing1_width = 100
    thing1_height = 100

    gameExit = False
    dodged = 0
    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
               quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
 
        x += x_change
        gameDisplay.fill(black)
        meh(dodged)
        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx, thing_starty, thing_width, thing_height, GREY)
        thing_starty += thing_speed
        # things(thingx, thingy, thingw, thingh, color)
        thing(thing1_startx, thing1_starty, thing1_width, thing1_height, GREY)
        thing1_starty += thing1_speed
        car(x,y)
        if thing_starty > display_height:
            thing_starty = 0 - thing_height
            thing_startx = random.randrange(400,display_width)
            dodged += 1
        if thing1_starty > display_height:
            thing1_starty = 0 - 100
            thing1_startx = random.randrange(0,400)
            dodged += 1
        ####
        if y < thing_starty+thing_height:
            #print('y crossover')

            if x > thing_startx and x < thing_startx + thing_width or x+ship_width > thing_startx and x + ship_width < thing_startx+thing_width:
                #print('x crossover')
                crash()
        if y < thing1_starty+thing1_height:
            #print('y crossover')

            if x > thing1_startx and x < thing1_startx + thing1_width or x+ship_width > thing1_startx and x + ship_width < thing1_startx+thing1_width:
                #print('x crossover')
                crash()
        ####
        
        pygame.display.update()
        clock.tick(60)
        

game_loop()
pygame.quit()
quit()
sys.exit()
