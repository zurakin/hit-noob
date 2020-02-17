import numpy, random
from PIL import ImageTk, Image
from math import cos, sin, pi, atan

class Block():
    def __init__(self, position, image_file = 'media/box1.png'):
        self.load = Image.open(image_file)
        self.image = ImageTk.PhotoImage(image = self.load)
        self.position = position

    def display(self, window):
        self.osd = window.canvas.create_image(self.position[0],
         self.position[1], image = self.image, anchor = 'nw')
