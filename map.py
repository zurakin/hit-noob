import numpy
from PIL import ImageTk, Image

class Block():
    def __init__(self, position, image_file = 'media/box1.png'):
        self.load = Image.open(image_file)
        self.image = ImageTk.PhotoImage(image = self.load)
        self.position = position

    def display(self, window):
        self.osd = window.canvas.create_image(self.position[0]*64, self.position[1]*64, image = self.image, anchor = 'nw')


class Bug():
    def __init__(self, position, image_file = 'media/bug.png', hp = 100, speed = 5):
        self.hp = hp
        self.speed = speed
        self.load = Image.open(image_file)
        self.image = ImageTk.PhotoImage(image = self.load)
        self.position = position

    def display(self, window):
        self.osd = window.canvas.create_image(self.position[0]*64, self.position[1]*64, image = self.image, anchor = 'nw')

class Player():
    def __init__(self, position, image_file = 'media/ninja.png', hp = 200, attack = 100, speed = 8):
        self.hp = hp
        self.speed = speed
        self.load = Image.open(image_file)
        self.image = ImageTk.PhotoImage(image = self.load)
        self.position = position
    def display(self, window):
        self.osd = window.canvas.create_image(self.position[0]*64, self.position[1]*64, image = self.image, anchor = 'nw')
    def move(self, coordinates):
        self.position[0] += coordinates[0]
        self.position[1] += coordinates[1]
