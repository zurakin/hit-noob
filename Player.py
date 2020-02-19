import numpy, random
from PIL import ImageTk, Image
from math import cos, sin, pi, atan, sqrt

class Player():
    def __init__(self, position, image_file = 'media/ninja.png', hp = 200, attack = 100, speed = 8):
        self.hp = hp
        self.speed = speed
        self.alpha = 0
        self.load = Image.open(image_file).rotate(-90)
        self.position = position
        self.gama = atan(16/32)
        self.a = sqrt(32**2 + 16**2)
    def display(self, window):
        self.image = ImageTk.PhotoImage(image = self.load.rotate(self.alpha))
        self.osd = window.canvas.create_image(self.position[0], self.position[1], image = self.image, anchor = 'nw')
    def move(self, direction, window):
        newx = int(self.position[0] + sin(self.alpha*pi/180)* direction * self.speed)
        newy = int(self.position[1] + cos(self.alpha*pi/180)* direction * self.speed)
        if not self.check_collision(newx, newy, window):
            self.position = [newx, newy]
        if newx < 0 :
            self.position[0] = 0
        elif newx > (window.geometry[0]-1) * 64 :
            self.position[0] = (window.geometry[0]-1) * 64
        if newy < 0 :
            self.position[1] = 0
        elif newy > (window.geometry[1] - 1) * 64 :
            self.position[1] = (window.geometry[1] - 1) * 64

    def rotate(self, angle):
        # O = (self.position[0] + 32, self.position[1]+32)
        # polygone = [
        # (O[0] + self.a * cos(radalpha + radgama), O[1] - self.a * sin(radalpha + radgama)),
        # (O[0] + self.a * cos(radalpha - radgama), O[1] - self.a * sin(radalpha - radgama)),
        # (O[0] + self.a * cos(radalpha + radgama + pi), O[1] - self.a * sin(radalpha + radgama + pi)),
        # (O[0] + self.a * cos(radalpha - radgama + pi), O[1] - self.a * sin(radalpha - radgama + pi))]
        # possible = True
        # for block in window.obstacles:
        #     for point in polygone:
        #         if block.position[0]<point[0]< block.position[0]+64 and block.position[1]<point[1]< block.position[1]+64:
        #             return True
        # return False
        self.alpha += angle
        self.alpha = self.alpha%(360)
    def check_collision(self, newx, newy, window):
        O = (newx + 32, newy+32)
        radalpha = self.alpha*pi/180 - pi/2
        radgama = self.gama*pi/180
        polygone = [
        (O[0] + self.a * cos(radalpha + radgama), O[1] - self.a * sin(radalpha + radgama)),
        (O[0] + self.a * cos(radalpha - radgama), O[1] - self.a * sin(radalpha - radgama)),
        (O[0] + self.a * cos(radalpha + radgama + pi), O[1] - self.a * sin(radalpha + radgama + pi)),
        (O[0] + self.a * cos(radalpha - radgama + pi), O[1] - self.a * sin(radalpha - radgama + pi))]
        # window.canvas.create_rectangle(polygone[0], polygone[2], fill="blue")
        for block in window.obstacles:
            for point in polygone:
                if block.position[0]<point[0]< block.position[0]+64 and block.position[1]<point[1]< block.position[1]+64:
                    return True
        return False
