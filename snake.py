from turtle import Turtle

POSITION = [(0, 0), (-20, 0), (-40, 0)]
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create()
        self.head = self.all_turtles[0]

    def create(self):
        for position in POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def update_snake(self):
        self.add_segment(self.all_turtles[-1].position())

    def move(self):
        for turtle in range(len(self.all_turtles) - 1, 0, -1):
            back_turtle = self.all_turtles[turtle]
            front_turtle = self.all_turtles[turtle - 1]
            back_turtle.goto(front_turtle.position())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        else:
            self.head.setheading(self.head.heading())

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        else:
            self.head.setheading(self.head.heading())

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        else:
            self.head.setheading(self.head.heading())

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        else:
            self.head.setheading(self.head.heading())

    def reset(self):
        for segments in self.all_turtles:
            segments.goto(1000, 1000)
        self.all_turtles.clear()
        self.create()
        self.head = self.all_turtles[0]
