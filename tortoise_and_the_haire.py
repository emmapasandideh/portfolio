import pygame, math, random
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, MOUSEBUTTONUP

pygame.init()
WIDTH = 1200
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables
platform_x = 0
platform_y = 0
platform_width = 1200
platform_height = 264
hare_x = 30
hare_y = 65
tortoise_x = 15
tortoise_y = 175
finish_x = 1101
finish_y = 0
finish_width = 99
finish_height = 264
score_x = 75
score_y = 350
score_width = 225
score_height = 100
target_x = 600
target_y = 475
slider_width = 360
slider_height= 80
slider_x = 420
slider_y = 675
line_y = 675
mid = 600
point_x = -100
point_y = -100
count = 0
tortoise_score = 0
hare_score = 0
max_score = 500
tortoise_running_length = 991
hare_running_length = 1011 
black = (0,0,0)
white = (255,255,255)
green = (0,255,0)
yellow = (255,255,0)
orange = (255,140,0)
red = (255,0,0)
font_1 = pygame.font.Font(None,50)
font_2 = pygame.font.Font(None,80)
font_3 = pygame.font.Font(None,30)
character_indicator = font_3.render("YOU", False, red)
score_title = font_1.render("SCORE:", False, black)
calculated_score = font_2.render((str(tortoise_score).zfill(3)),False, black)
great = font_1.render("Great!", False, green)
good = font_1.render("Good!", False, yellow)
ok = font_1.render("Ok.", False, orange)
bad = font_1.render("Bad.", False, red)
response_text = None
response_x = 950
response_y = 801
win = font_2.render("Slow and steady wins the race!", False, black)
lose = font_2.render("Better luck next time :)", False, black)

# ---------------------------
running = True
while running:
    # EVENT HANDLING
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False  # this would stop the loop
        if event.type == pygame.MOUSEBUTTONDOWN:
            point_x = line_x
            up_or_down = random.randrange(2)
            if up_or_down == 0:
                point_y = 475 + random.randrange(20)
            else:
                point_y = 475 - random.randrange(20)
            difference = abs(mid - line_x)
            if difference<=45:
                tortoise_score += 16
                response_text = great
                response_y = 801
            elif difference<=90:
                tortoise_score += 8
                response_text = good
                response_y = 801
            elif difference<=135:
                tortoise_score += 4
                response_text = ok
                response_y = 801
            else:
                tortoise_score += 2
                response_text = bad
                response_y = 801
            tortoise_complete_percent = tortoise_score / max_score
            tortoise_x = tortoise_running_length * tortoise_complete_percent + 55
            hare_score += random.choices([16,8,4,2],[5,4,3,1])[0]
            hare_complete_percent = hare_score / max_score
            hare_x = hare_running_length * hare_complete_percent + 45
            printed_score = str(tortoise_score)
            calculated_score = font_2.render(printed_score.zfill(3), False, black)
        elif event.type == QUIT:
            running = False

    # GAME STATE UPDATES - move a player/ball, put math here
    # All game math and comparisons happen here
    count += 1
    line_x = math.sin(count/6) * slider_width/2 + (slider_x+ slider_width/2)
    if response_text is not None :
        response_y -= 5
        if response_y <= 400:
            response_text = None
    
    # DRAWING
    screen.fill((255, 255, 255))  # always the first drawing command!
    
    #platform
    pygame.draw.rect(screen,(0,154,23),(platform_x,platform_y,platform_width,platform_height))
    
    #finish line
    pygame.draw.rect(screen,(0,0,0),(finish_x,finish_y,finish_width,finish_height))
    tile_x = finish_x
    tile_y = finish_y
    tile_width = 33
    position = 1
    while tile_y <= 561:
        if position % 2 == 1:
            pygame.draw.rect(screen,(255,255,255),(tile_x,tile_y,tile_width, tile_width))
            pygame.draw.rect(screen,(255,255,255),(tile_x+66,tile_y,tile_width, tile_width))
        if position % 2 == 0:
            pygame.draw.rect(screen,(255,255,255),(tile_x+33,tile_y,tile_width, tile_width))
        tile_y += 33
        position += 1

    #hare
    pygame.draw.ellipse(screen,(237,237,237),(hare_x,hare_y,90,70))
    pygame.draw.ellipse(screen,(237,237,237),(hare_x+60,hare_y+62,25,20))
    pygame.draw.ellipse(screen,(237,237,237),(hare_x+30,hare_y+62,25,20))
    pygame.draw.circle(screen,(237,237,237),(hare_x+90,hare_y+5),25)
    pygame.draw.circle(screen,(237,237,237),(hare_x-5,hare_y+30),12)
    pygame.draw.ellipse(screen,(237,237,237),(hare_x+70,hare_y-55,20,45))
    pygame.draw.ellipse(screen,(237,237,237),(hare_x+90,hare_y-55,20,45))
    pygame.draw.ellipse(screen,(255,82,220),(hare_x+98,hare_y-50,10,30))
    pygame.draw.ellipse(screen,(255,82,220),(hare_x+78,hare_y-50,10,30))
    pygame.draw.circle(screen,(0,0,0),(hare_x+90,hare_y),4)
    pygame.draw.circle(screen,(0,0,0),(hare_x+105,hare_y),4)
    pygame.draw.polygon(screen,(255,117,227),[(hare_x+95,hare_y+10),(hare_x+102,hare_y+10),(hare_x+98,hare_y+16)])

    #tortoise
    pygame.draw.circle(screen,(89,255,119),(tortoise_x+25,tortoise_y+58),12)
    pygame.draw.circle(screen,(89,255,119),(tortoise_x+80,tortoise_y+58),12)
    pygame.draw.arc(screen,(0,87,16),(tortoise_x,tortoise_y,110,105),0,3.14,100)
    pygame.draw.ellipse(screen,(0,186,34),(tortoise_x+18,tortoise_y+15,20,28))
    pygame.draw.ellipse(screen,(0,186,34),(tortoise_x+45,tortoise_y+10,20,35))
    pygame.draw.ellipse(screen,(0,186,34),(tortoise_x+70,tortoise_y+15,20,28))
    pygame.draw.ellipse(screen,(89,255,119),(tortoise_x+100,tortoise_y+5,35,32))
    pygame.draw.circle(screen,(0,0,0),(tortoise_x+120,tortoise_y+15),4)

    # character indicator
    screen.blit(character_indicator,(tortoise_x + 35, tortoise_y-20))

    # scoreboard
    pygame.draw.rect(screen,(255, 216, 138),(score_x,score_y,score_width,score_height))

    # text: score title
    screen.blit(score_title,(score_x+45,score_y-50))

    # text: total calculated score
    screen.blit(calculated_score,(score_x + 65, score_y+30))

    #target
    target_radius = 180
    target_colour = 1
    while target_radius>=45:
        if target_colour % 2 == 1:
            pygame.draw.circle(screen,(255,0,0),(target_x,target_y),target_radius)
        elif target_colour % 2 == 0:
            pygame.draw.circle(screen,(255,255,255),(target_x,target_y),target_radius)
        target_radius -= 45
        target_colour += 1

    # slider red zone
    pygame.draw.rect(screen,(255,0,0),(slider_x, slider_y,slider_width, slider_height))

    # slider orange zone
    pygame.draw.rect(screen,(255,140,0),(slider_x+45, slider_y,slider_width*0.75, slider_height))

    # slider yellow zone
    pygame.draw.rect(screen,(255,255,0),(slider_x+90, slider_y,slider_width*0.5, slider_height))

    # slider green zone
    pygame.draw.rect(screen,(0, 255, 0),(slider_x+135, slider_y, slider_width*0.25, slider_height))

    # slider outline
    pygame.draw.rect(screen,(0,0,0),(slider_x, slider_y, slider_width, slider_height),10)

    # slider line movement
    pygame.draw.line(screen,(0,0,0),(line_x, line_y), (line_x, line_y + slider_height), 4)

    # point of impact
    pygame.draw.line(screen,(black),(point_x,point_y),(point_x+10,point_y+10),4)
    pygame.draw.line(screen,(black),(point_x+10,point_y),(point_x,point_y+10),4)

    # response 
    if response_text is not None:
        screen.blit(response_text, (response_x, response_y))

    # win or lose 
    if tortoise_score>= 500 and hare_score<=500:
        pygame.draw.rect(screen,(196,217,255),(0,264,WIDTH,700))
        pygame.draw.arc(screen,(0,0,0),(tortoise_x+112,tortoise_y+15,30,20),3.14,3*3.14/2,3)
        screen.blit(win,(175,500))
    elif tortoise_score<=500 and hare_score>=500:
        pygame.draw.rect(screen,(196,217,255),(0,264,WIDTH,700))
        pygame.draw.arc(screen,(0,0,0),(hare_x+80,hare_y+5,30,20),3.14,3*3.14/2,3)
        screen.blit(lose,(300,500))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    # ---------------------------

pygame.quit()
