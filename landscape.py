import pygame
import math
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONDOWN
pygame.init()
WIDTH = 640
HEIGHT = 480
SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
percent = 0.0051
start = pygame.Color(168, 219, 255)
end = pygame.Color(11, 11, 69)
transition_speed = 0.0051
sun_x = 0
sun_y = 0
moon_x=150
moon_y=480
star_x= 200
star_y= 80
star_colour = (168, 219, 255)
house_x = 400
house_y = 250
smoke_x = 530
smoke_y = 180
sheep_x = 110
sheep_y = 430
# ---------------------------
running = True
while running:
    if percent >= 1:
        transition_speed = -transition_speed
    elif percent <= 0:
        transition_speed = -transition_speed
    percent = round(percent + transition_speed, 2)
    print(percent)
    new_color = start.lerp(end, percent)

    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False # this would stop the loop
        elif event.type == QUIT:
            running = False
        elif event.type == MOUSEBUTTONDOWN:
            print(event.pos)
        
    # GAME STATE UPDATES - move a player/ball, put math here
    # All game math and comparisons happen here

    # DRAWING
    screen.fill((new_color)) # always the first drawing command!
    #stars
    pygame.draw.circle(screen,(star_colour),(moon_x+100,moon_y-30),3)
    pygame.draw.circle(screen,(star_colour),(moon_x+150,moon_y-75),3)
    pygame.draw.circle(screen,(star_colour),(moon_x+230,moon_y-90),3)
    pygame.draw.circle(screen,(star_colour),(moon_x+180,moon_y-20),3)
    pygame.draw.circle(screen,(star_colour),(moon_x-80,moon_y+80),3)
    pygame.draw.circle(screen,(star_colour),(moon_x-10,moon_y-70),3)
    pygame.draw.circle(screen,(star_colour),(moon_x-120,moon_y-10),3)
    #sun
    pygame.draw.circle(screen,(255,77,0),(sun_x,sun_y),60)
    pygame.draw.circle(screen,(255,129,0),(sun_x,sun_y),50)
    pygame.draw.circle(screen,(255, 242, 0),(sun_x,sun_y),40)
    #moon
    pygame.draw.circle(screen,(244, 244, 244),(moon_x,moon_y),50)
    pygame.draw.circle(screen,(202, 202, 202),(moon_x-30,moon_y+15),6)
    pygame.draw.circle(screen,(202, 202, 202),(moon_x-20,moon_y-30),4)
    pygame.draw.circle(screen,(202,202,202),(moon_x-10, moon_y-40),3)
    pygame.draw.ellipse(screen,(202,202,202),(moon_x-40, moon_y-20,10,20))
    pygame.draw.circle(screen,(202,202,202),(moon_x-20, moon_y-10),8)
    pygame.draw.circle(screen,(202,202,202),(moon_x-20, moon_y-10),3)
    pygame.draw.circle(screen,(202,202,202),(moon_x-10,moon_y+30),5)
    # changes in sky (colour, position of sun, moon, stars)
    if 0.0<=percent<=0.5:  # day
        moon_x = -50
        sun_x+=8
        sun_y= ((sun_x - WIDTH/2)**2) / WIDTH +75
        window_colour = (245, 245, 245)
        star_colour = (new_color)
    elif 0.5<=percent<=1:  # night
        sun_x = -80
        moon_x +=9
        moon_y= ((moon_x - WIDTH/2)**2) / WIDTH +75
        window_colour = (255,255,167)
        star_colour = (255,255,0)
    #hills
    pygame.draw.arc(screen,(16, 227, 55),(200,300,900,500),3.14/2,3.14, 400)
    pygame.draw.arc(screen,(222, 93, 0),(310,350,400,600),3.14/2,3.14, 30)
    pygame.draw.arc(screen,(0,154,23),(-400,380,700,200),0,3.14/2, 400)
    #house
    pygame.draw.rect(screen,(255, 183, 94),(house_x,house_y,150,130))
    #windows
    pygame.draw.rect(screen,((window_colour)),(house_x+20,house_y+40,30,30))
    pygame.draw.rect(screen,((window_colour)),(house_x+100,house_y+40,30,30))
    pygame.draw.line(screen,(255,200,50),(house_x+35,house_y+40),(house_x+35,house_y+70), 2)
    pygame.draw.line(screen,(255,200,50),(house_x+20,house_y+55),(house_x+50,house_y+55), 2)
    pygame.draw.line(screen,(255,200,50),(house_x+115,house_y+40),(house_x+115,house_y+70), 2)
    pygame.draw.line(screen,(255,200,50),(house_x+100,house_y+55),(house_x+130,house_y+55), 2)
    #smoke
    pygame.draw.circle(screen,(186, 193, 194),(smoke_x,smoke_y),5)
    pygame.draw.circle(screen,(186, 193, 194),(smoke_x+8,smoke_y-40),8)
    pygame.draw.circle(screen,(186, 193, 194),(smoke_x-8,smoke_y-80),10)
    #smoke movement
    smoke_x = math.sin(0.1*smoke_y)*20 + 535
    smoke_y-= 4
    if smoke_y==-20:
        smoke_y = 180
    #chimmney
    pygame.draw.rect(screen,(255,183,94),(house_x+120,house_y-70,20,100))
    pygame.draw.rect(screen,(110, 59, 14),(house_x+115,house_y-70,30,10))
    #roof
    pygame.draw.polygon(screen,(110, 59, 14),[(house_x, house_y), (house_x+150, house_y), (house_x+75,house_y-70)])
    #door
    pygame.draw.rect(screen,(181, 84, 0),(house_x+60, house_y+80,30,50))
    pygame.draw.circle(screen,(153, 148, 148),(house_x+85,house_y+110),4)
    #sheep
    pygame.draw.line(screen,(0,0,0),(sheep_x,sheep_y),(sheep_x-8, sheep_y+35),8)
    pygame.draw.line(screen,(0,0,0),(sheep_x+10,sheep_y),(sheep_x+8, sheep_y+35),8)
    pygame.draw.line(screen,(0,0,0),(sheep_x+30,sheep_y),(sheep_x+35, sheep_y+35),8)
    pygame.draw.line(screen,(0,0,0),(sheep_x+40,sheep_y),(sheep_x+45, sheep_y+35),8)
    pygame.draw.circle(screen,(255,255,255),(sheep_x,sheep_y),15)
    pygame.draw.circle(screen,(255,255,255),(sheep_x+20,sheep_y),25)
    pygame.draw.circle(screen,(255,255,255),(sheep_x+40,sheep_y),15)
    pygame.draw.circle(screen,(0,0,0),(sheep_x+50,sheep_y-15),10)
    pygame.draw.circle(screen,(255,255,255),(sheep_x+45,sheep_y-25),5)
    pygame.draw.circle(screen,(255,255,255),(sheep_x+50,sheep_y-25),5)
    pygame.draw.circle(screen,(255,255,255),(sheep_x+55,sheep_y-25),5)
    #sheep movement
    sheep_x+=5
    if sheep_x == WIDTH+10:
        sheep_x = 0

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------
pygame.quit()
