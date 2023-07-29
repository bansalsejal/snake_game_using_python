from turtle import Screen
import time
from scoreBoard import ScoreBoard
from food import Food
from snake import Snake
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
score_board = ScoreBoard()
snake = Snake()
food = Food()

screen.tracer(0)
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")
screen.onkey(fun=snake.left, key="Left")

is_on = True
while is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.create()
        snake.update_snake()
        score_board.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        score_board.reset()
        snake.reset()

    for turtle in snake.all_turtles[1:]:
        if snake.head.distance(turtle) < 15:
            score_board.reset()
            snake.reset()


screen.exitonclick()
