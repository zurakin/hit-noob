import numpy, random
from PIL import ImageTk, Image
from math import cos, sin, pi, atan

class Player():
    def __init__(self, position, image_file = 'media/ninja.png', hp = 200, attack = 100, speed = 8):
        self.hp = hp
        self.speed = speed
        self.alpha = 0
        self.load = Image.open(image_file).rotate(-90)
        self.position = position
    def display(self, window):
        self.image = ImageTk.PhotoImage(image = self.load.rotate(self.alpha))
        self.osd = window.canvas.create_image(self.position[0], self.position[1], image = self.image, anchor = 'nw')
    def move(self, direction, window):
        self.position[0] += sin(self.alpha*pi/180)* direction * self.speed
        self.position[1] += cos(self.alpha*pi/180)* direction * self.speed
    def rotate(self, angle):
        self.alpha += angle
        self.alpha = self.alpha%(360)
