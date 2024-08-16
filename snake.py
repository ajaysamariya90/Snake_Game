from turtle import Turtle

x_position = [0, -20, -40]
movement = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):

        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for i in range(0, 3):
            self.add_turtle((x_position[i], 0))

    def add_turtle(self, position):

        new_turtle = Turtle(shape="square")
        new_turtle.speed("fastest")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtle.append(new_turtle)
        self.all_turtle[0].color("Black")

    def extend(self):
        self.add_turtle(self.all_turtle[-1].position())

    def detect_collision_with_tail(self):
        # Check if the head collides with any segment of the body
        for segment in self.all_turtle[1:]:
            if self.head.distance(segment) < 10:  # Adjust the distance threshold as needed
                return True
        return False

    def move(self):

        for all_tur in range(len(self.all_turtle) - 1, 0, -1):
            new_x = self.all_turtle[all_tur - 1].xcor()
            new_y = self.all_turtle[all_tur - 1].ycor()
            self.all_turtle[all_tur].goto(new_x, new_y)

        self.head.forward(movement)

    def reset_snake(self):
        for seg in self.all_turtle:
            seg.goto(1000, 1000)
        self.all_turtle.clear()
        self.create_snake()
        self.head = self.all_turtle[0]

    def up(self):

        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):

        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):

        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
