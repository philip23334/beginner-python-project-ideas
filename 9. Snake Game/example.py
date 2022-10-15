# this is bugged, didnt bother to fix it

import pygame
import random
screen = pygame.display.set_mode((640, 480))
# create a function to draw the snake
def draw_snake(snake):
    # loop through the snake
    for i in range(len(snake)):
        # draw the snake
        pygame.draw.rect(screen, (0, 255, 0), (snake[i][0], snake[i][1], 10, 10))
# create a function to draw the food
def draw_food(food):
    # draw the food
    pygame.draw.rect(screen, (255, 0, 0), (food[0], food[1], 10, 10))
# create a function to check if the snake has eaten the food
def check_eat(snake, food):
    # if the snake has eaten the food
    if snake[0][0] == food[0] and snake[0][1] == food[1]:
        # return True
        return True
    # if the snake has not eaten the food
    else:
        # return False
        return False
# create a function to check if the snake has hit the wall
def check_wall(snake):
    # if the snake has hit the wall
    if snake[0][0] < 0 or snake[0][0] > 490 or snake[0][1] < 0 or snake[0][1] > 490:
        # return True
        return True
    # if the snake has not hit the wall
    else:
        # return False
        return False
# create a function to check if the snake has hit itself
def check_self(snake):
    # loop through the snake
    for i in range(1, len(snake)):
        # if the snake has hit itself
        if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
            # return True
            return True
    # if the snake has not hit itself
    else:
        # return False
        return False
# create a function to check if the snake has hit something
def check_hit(snake):
    # if the snake has hit something
    if check_wall(snake) or check_self(snake):
        # return True
        return True
    # if the snake has not hit something
    else:
        # return False
        return False
# create a function to move the snake
def move_snake(snake, direction):
    # create a variable to store the new snake
    new_snake = []
    # if the snake is moving up
    if direction == "up":
        # create a variable to store the new head
        new_head = [snake[0][0], snake[0][1] - 10]
    # if the snake is moving right
    elif direction == "right":
        # create a variable to store the new head
        new_head = [snake[0][0] + 10, snake[0][1]]
    # if the snake is moving down
    elif direction == "down":
        # create a variable to store the new head
        new_head = [snake[0][0], snake[0][1] + 10]
    # if the snake is moving left
    elif direction == "left":
        # create a variable to store the new head
        new_head = [snake[0][0] - 10, snake[0][1]]
    # add the new head to the new snake
    new_snake.append(new_head)
    # loop through the snake
    for i in range(len(snake) - 1):
        # add the rest of the snake to the new snake
        new_snake.append(snake[i])
    # return the new snake
    return new_snake
# create a function to move the snake and check if it has hit something
def move(snake, direction):
    # if the snake has not hit something
    if not check_hit(snake):
        # move the snake
        snake = move_snake(snake, direction)
    # return the snake
    return snake
# create a function to get the direction
def get_direction():
    # get the direction
    direction = input("Enter a direction (up, right, down, left): ")
    # return the direction
    return direction
# create a function to get the food
def get_food(snake):
    # create a variable to store the food
    food = []
    # create a variable to store the food coordinates
    food_coords = [random.randint(0, 49) * 10, random.randint(0, 49) * 10]
    # loop through the snake
    for i in range(len(snake)):
        # if the food coordinates are the same as the snake coordinates
        if food_coords[0] == snake[i][0] and food_coords[1] == snake[i][1]:
            # get the food again
            food = get_food(snake)
            # break the loop
            break
    # if the food coordinates are not the same as the snake coordinates
    else:
        # set the food
        food = food_coords
    # return the food
    return food
# create a function to get the snake
def get_snake():
    # create a variable to store the snake
    snake = []
    # create a variable to store the snake coordinates
    snake_coords = [random.randint(0, 49) * 10, random.randint(0, 49) * 10]
    # add the snake coordinates to the snake
    snake.append(snake_coords)
    # return the snake
    return snake
# create a function to get the score
def get_score(snake):
    # create a variable to store the score
    score = len(snake) - 1
    # return the score
    return score
# create a function to display the score
def display_score(score):
    # display the score
    print("Score: " + str(score))
# create a function to display the game over message
def display_game_over():
    # display the game over message
    print("Game Over")
# create a function to display the game
def display_game(snake, food, score):
    # clear the screen
    screen.fill((0, 0, 0))
    # draw the snake
    draw_snake(snake)
    # draw the food
    draw_food(food)
    # display the score
    display_score(score)
    # update the display
    pygame.display.update()
# create a function to play the game
def play_game():
    # create a variable to store the snake
    snake = get_snake()
    # create a variable to store the food
    food = get_food(snake)
    # create a variable to store the score
    score = get_score(snake)
    # create a variable to store the direction
    direction = "right"
    # create a variable to store the game over status
    game_over = False
    # create a variable to store the clock
    clock = pygame.time.Clock()
    # loop until the game is over
    while not game_over:
        # loop through the events
        for event in pygame.event.get():
            # if the event is a quit event
            if event.type == pygame.QUIT:
                # set the game over status to True
                game_over = True
        # if the snake has eaten the food
        if check_eat(snake, food):
            # get the food
            food = get_food(snake)
            # add a new part to the snake
            snake.append([0, 0])
            # update the score
            score = get_score(snake)
        # move the snake
        snake = move(snake, direction)
        # display the game
        display_game(snake, food, score)
        # set the frame rate
        clock.tick(10)
    # display the game over message
    display_game_over()
# play the game
play_game()