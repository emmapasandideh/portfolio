import pygame
from pygame.locals import KEYDOWN,K_ESCAPE, QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_RETURN
import random

pygame.init()

WIDTH = 600
HEIGHT = 700
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

rows = 15
columns = 15
blue = (0,0,255)
black = (0,0,0)
high_score = 0 

def update_coordinate(direction,coordinates):
    if direction == "north":
        column_position = coordinates[0][0]
        row_position = coordinates[0][1] - 1
    elif direction == "south":
        column_position = coordinates[0][0]
        row_position = coordinates[0][1] + 1
    elif direction == "east":
        column_position = coordinates[0][0] + 1
        row_position = coordinates[0][1]
    else:
        column_position = coordinates[0][0] - 1
        row_position = coordinates[0][1]  
    coordinates.pop(-1)
    return column_position, row_position 

def grid_to_pixels(column_position,row_position,square_width,square_height,offset_x,offset_y):
    x = column_position * square_width + offset_x
    y = row_position * square_height + offset_y 
    return x,y

def create_food(columns,rows):
    column_position = random.randrange(1,columns-1)
    row_position = random.randrange(1,rows-1)
    food_coordinate = column_position,row_position
    return food_coordinate

def colour_chooser(order,blue,black): 
    if order%2 == 0:
        colour = blue
    elif order%2 == 1:
        colour = black
    return colour

def main():
    while True:
        result = game()
        if result == "quit":
            break
        elif result == "restart":
            continue

def game(): 
    global high_score
    # Initialize global variables
    game_over = False
    direction = None
    offset_x = 0
    offset_y = 100
    square_height = (HEIGHT-offset_y)//rows
    square_width = (WIDTH-offset_x)//columns
    coordinates = []
    column_position = random.randrange(1,columns-1)
    row_position = random.randrange(1,rows-1)
    coordinates.append((column_position,row_position))
    foods = []
    for i in range(3):
        new_food = create_food(columns,rows)
        foods.append(new_food)
    score = 0
    white = (255,255,255)
    red = (255,0,0)
    light_green = (171,255,107)
    dark_green = (148,245,76)
    brown = (139,69,19)
    font_1 = pygame.font.Font("pixel.ttf", 60)
    font_2 = pygame.font.Font("pixel.ttf", 35)
    font_3 = pygame.font.Font("pixel.ttf", 30)
    font_4 = pygame.font.Font("pixel.ttf", 25)
    game_title = font_1.render("SNAKE", True, red)
    game_title_x = 30
    game_title_y = 0
    score_title = font_2.render("SCORE", True, black)
    score_title_x = 300
    score_title_y = 10
    score_value_x = 350
    score_value_y = 50
    high_score_title = font_2.render("HI", True, black)
    high_score_title_x = 500
    high_score_title_y = 10
    high_score_value = font_3.render(str(high_score), True, black)
    high_score_value_x = 510
    high_score_value_y = 50
    game_over_title = font_2.render("GAME OVER", True, red)
    game_over_x = WIDTH/2-WIDTH/4
    game_over_y = (HEIGHT+offset_y)/2-WIDTH/4
    game_over_width = WIDTH/2
    game_over_height= WIDTH/2
    retry_title = font_4.render("Retry: <ENTER>", True, black)
    quit_title = font_4.render("Quit: <ESC>", True, black)

    # ---------------------------

    running = True
    while running:
        # EVENT HANDLING
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False # this would stop the loop
                if event.key == K_RETURN and game_over == True:
                    if score > high_score:
                        high_score = score
                    return "restart"
                if event.key == K_ESCAPE and game_over == True:
                    return "quit"
                if event.key == K_UP:
                    if direction != "south":
                        direction = "north"
                elif event.key == K_DOWN:
                    if direction != "north":
                        direction = "south"
                elif event.key == K_LEFT:
                    if direction != "east":
                        direction = "west"
                elif event.key == K_RIGHT:
                    if direction != "west":
                        direction = "east"
            elif event.type == QUIT:
                running = False

        # GAME STATE UPDATES - move a player/ball, put math here
        # All game math and comparisons happen here
        
        # movement (only when playing)
        if game_over == False and direction != None:
            updated_coordinate = update_coordinate(direction,coordinates)
            coordinates.insert(0, updated_coordinate)

        # game over when snake touches itself 
        if coordinates[0] in coordinates[1:]: 
            game_over = True

        # eating and producing food after
        for i in range(len(foods)):
            if foods[i] == coordinates[0]:
                coordinates.append(coordinates[-1])
                foods.remove(foods[i])
                new_food = create_food(columns,rows)
                foods.append(new_food)
                score += 1
                
        # snake movement boundary
        if coordinates[0][0] <= 0 or coordinates[0][0] >= columns-1 or coordinates[0][1] <= 0 or coordinates[0][1] >= rows-1: 
            game_over = True

        # updating displayed score value
        score_value = font_3.render(str(score), False, black)
        
        # DRAWING
        screen.fill(white) # always the first drawing command!
        
        #floor
        grid_x = 0
        grid_y = 0
        order_1 = 0
        order_2 = 0
        while grid_y<rows:
            if grid_x == columns+1:
                grid_y += 1
                grid_x = 0
                order_1 += 1
                order_2 = 0
            x,y = grid_to_pixels(grid_x,grid_y,square_width,square_height,offset_x,offset_y)
            if order_1 % 2 == 0:
                if order_2 % 2 == 0:
                    pygame.draw.rect(screen,dark_green,(x,y,square_width,square_height))
                elif order_2 % 2 == 1:
                    pygame.draw.rect(screen,light_green,(x,y,square_width,square_height))
            elif order_1 % 2 == 1:
                if order_2 % 2 == 1:
                    pygame.draw.rect(screen,dark_green,(x,y,square_width,square_height))
                elif order_2 % 2 == 0:
                    pygame.draw.rect(screen,light_green,(x,y,square_width,square_height))
            grid_x += 1
            order_2 += 1


        # food
        for i in range(len(foods)):
            column_position = foods[i][0]
            row_position = foods[i][1]
            x,y = grid_to_pixels(column_position,row_position,square_width,square_height,offset_x,offset_y)
            pygame.draw.circle(screen,red,(x+square_width/2,y+square_height/2),square_height/2)
            pygame.draw.line(screen,brown,(x+square_width/2,y),(x+square_width/2,y-square_height/4),4)
            
        # snake
        for i in range(len(coordinates)):
            column_position = coordinates[i][0]
            row_position = coordinates[i][1]
            x,y = grid_to_pixels(column_position,row_position,square_width,square_height,offset_x,offset_y)
            colour = colour_chooser(i,blue,black)
            pygame.draw.rect(screen,colour,(x,y,square_width,square_height))
            # snake eyes - alive
            if game_over == False:
                if i == 0:
                    pygame.draw.circle(screen,white,(x+square_width/2,y+square_height//2),square_width//4)
                    pygame.draw.circle(screen,black,(x+square_width/2,y+square_height//2),square_width//8)
            # snake eyes - dead
            else:
                if i == 0:
                    pygame.draw.line(screen,black,(x+square_width//4,y+square_height//4),(x+3*square_width//4,y+3*square_height//4),5)
                    pygame.draw.line(screen,black,(x+3*square_width//4,y+square_height//4),(x+square_width//4,y+3*square_height//4),5)
        
        # game title
        screen.blit(game_title,(game_title_x,game_title_y))
        # score title
        screen.blit(score_title,(score_title_x,score_title_y))
        # score value
        screen.blit(score_value,(score_value_x,score_value_y))
        # high score title
        screen.blit(high_score_title,(high_score_title_x,high_score_title_y))
        # high score value
        screen.blit(high_score_value,(high_score_value_x,high_score_value_y))

        # game over screen
        if game_over == True:
            pygame.draw.rect(screen,white,(game_over_x,game_over_y,game_over_width,game_over_height))
            screen.blit(game_over_title,(game_over_x+45,game_over_y+game_over_height//8))
            screen.blit(retry_title,(game_over_x+50,game_over_y+2*game_over_height//5))
            screen.blit(quit_title,(game_over_x+50,game_over_y+3*game_over_height//5))

        # Must be the last two lines
        # of the game loop
        pygame.display.flip()
        clock.tick(10)
        #---------------------------


    pygame.quit()
    
if __name__ == "__main__":
    main()
