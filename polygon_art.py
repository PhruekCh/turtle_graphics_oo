import turtle
import random

class Polygon:
    def __init__(self, num_sides = 3, size = 100, orientation = 0, location = [100,100], color = (0,0,0),border_size = 100):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size
        self.reduction_ratio = 0.618

    def draw_polygon(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

class PolygonRun:
    def __init__(self, choice = 1):
        self.random_attributes()
        self.choice = choice
        self.choices()

    def random_attributes(self):
        self.num_sides = random.randint(3, 5)
        self.size = random.randint(50, 150)
        self.orientation = random.randint(0, 90)
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        self.color = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        self.border_size = random.randint(1, 10)

    def choices(self):
        self.amount = 30
        if self.choice == 1:
            for i in range(self.amount):
                p = Polygon(3,self.size,
                                    self.orientation,
                                    self.location,
                                    self.color,
                                    self.border_size)
                p.draw_polygon()
                self.random_attributes()

        elif self.choice == 2:
            for i in range(self.amount):
                    p = Polygon(4, self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw_polygon()
                    self.random_attributes()

        elif self.choice == 3:
            for i in range(self.amount):
                    p = Polygon(5, self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw_polygon()
                    self.random_attributes()

        elif self.choice == 4:
             for i in range(self.amount):
                    p = Polygon(self.num_sides, self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw_polygon()
                    self.random_attributes()

        elif self.choice == 5:
            for i in range(self.amount):
                    p = EmbeddedPolygon(3 , self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw()
                    self.random_attributes()

        elif self.choice == 6:
            for i in range(self.amount):
                    p = EmbeddedPolygon(4 , self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw()
                    self.random_attributes()

        elif self.choice == 7:
            for i in range(self.amount):
                    p = EmbeddedPolygon(5 , self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw()
                    self.random_attributes()

        elif self.choice == 8:
            for i in range(self.amount):
                    p = EmbeddedPolygon(self.num_sides, self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw()
                    self.random_attributes()

        elif self.choice == 9:
            for i in range(int(self.amount/2)):
                    p = Polygon(self.num_sides, self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    p.draw_polygon()
                    self.random_attributes()
                    ep = EmbeddedPolygon(self.num_sides, self.size,
                                self.orientation,
                                self.location,
                                self.color,
                                self.border_size)
                    ep.draw()
                    self.random_attributes()

class EmbeddedPolygon(Polygon):
    def draw(self):
        super().draw_polygon()
        for i in range(3):
            turtle.penup()
            turtle.goto(self.location[0], self.location[1])
            turtle.setheading(self.orientation)
            turtle.color(self.color)
            turtle.pensize(self.border_size)
            turtle.pendown()
            for _ in range(self.num_sides):
                turtle.forward(self.size)
                turtle.left(360/self.num_sides)
            self.reset_position()

    def reset_position(self):
        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(self.size*(1-self.reduction_ratio)/2)
        turtle.right(90)
        self.location[0] = turtle.pos()[0]
        self.location[1] = turtle.pos()[1]
        self.size *= self.reduction_ratio


#Insert choice 1-9 for each type of Arts you wanted to display
PolygonRun(9)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()