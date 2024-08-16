from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# timmy = Turtle()
# phony = Turtle()
# mini = Turtle()
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("Green")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# x_position = [0, -20, -40]
#
# all_turtle = []
#
# for i in range(0, 3):
#
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.penup()
#     new_turtle.goto(x=x_position[i], y=0)
#     all_turtle.append(new_turtle)

is_game_on = True


while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:

        food.refresh()
        snake.extend()
        scoreboard.increment()
        # scoreboard.reset()
        # scoreboard.update_score()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < - 290 or snake.head.ycor() > 290 or snake.head.ycor() < - 290:
        scoreboard.reset()
        snake.reset_snake()
        # scoreboard.update_score()

    # Detect collision with its own tail
    if snake.detect_collision_with_tail():
        scoreboard.reset()
        snake.reset_snake()
        # scoreboard.update_score()

    # for all_tur in range(len(all_turtle)-1, 0, -1):
    #     new_x = all_turtle[all_tur - 1].xcor()
    #     new_y = all_turtle[all_tur - 1].ycor()
    #     all_turtle[all_tur].goto(new_x, new_y)
    #
    # all_turtle[0].forward(20)

# phony.shape("square")
# phony.color("White")
# phony.goto(x=-20, y=0)
#
# mini.shape("square")
# mini.color("White")
# mini.goto(x=-40, y=0)
#


screen.exitonclick()
