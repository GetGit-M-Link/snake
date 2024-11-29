from turtle import Turtle

START_POSITION = (0, 0)
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.snake_length = 3
        self.move_direction = 270
        self.direction_lock = False
        for _ in range(self.snake_length):
            snake_part = self.new_segment()
            snake_part.setx((-20 * _) + START_POSITION[0])
            snake_part.sety(START_POSITION[1])
            self.segments.append(snake_part)
        self.head = self.segments[0]

    @staticmethod
    def new_segment():
        snake_part = Turtle()
        snake_part.penup()
        snake_part.shape("square")
        snake_part.color("white")
        snake_part.penup()
        return snake_part


    def move(self):
        """moves the snake 20 in the move direction"""
        for index in range(- 1, - len(self.segments), -1):
            position_of_snake_part_before_x = self.segments[index - 1].pos()[0]
            position_of_snake_part_before_y = self.segments[index - 1].pos()[1]
            self.segments[index].goto(position_of_snake_part_before_x, position_of_snake_part_before_y)
        self.head.setheading(self.move_direction)
        self.head.forward(20)
        self.direction_lock = False

    def grow(self):
        new_tail = self.new_segment()
        self.segments.append(new_tail)

    def up(self):
        if self.move_direction != DOWN and not self.direction_lock:
            self.move_direction = UP
            self.direction_lock = True


    def down(self):
        if self.move_direction != UP and not self.direction_lock:
            self.move_direction = DOWN
            self.direction_lock = True


    def right(self):
        if self.move_direction != LEFT and not self.direction_lock:
            self.move_direction = RIGHT
            self.direction_lock = True


    def left(self):
        if self.move_direction != RIGHT and not self.direction_lock:
            self.move_direction = LEFT
            self.direction_lock = True

