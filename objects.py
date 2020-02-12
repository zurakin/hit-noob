import numpy, random
from PIL import ImageTk, Image
from math import cos, sin, pi

class Block():
    def __init__(self, position, image_file = 'media/box1.png'):
        self.load = Image.open(image_file)
        self.image = ImageTk.PhotoImage(image = self.load)
        self.position = position

    def display(self, window):
        self.osd = window.canvas.create_image(self.position[0],
         self.position[1], image = self.image, anchor = 'nw')


class Bug():
    def __init__(self, position, image_file = 'media/bug.png', hp = 100, speed = 4):
        self.hp = hp
        self.speed = speed
        self.rotating_speed = 6
        self.alpha = 0
        self.target_alpha = 0
        self.state = 0 #0 for normal mode, 1 for chasing mode, 2 for cuatious mode, 3 for rotating mode
        self.load = Image.open(image_file)
        self.position = position
        self.sleep = 0

    def display(self, window):
        self.image = ImageTk.PhotoImage(image = self.load.rotate(self.alpha))
        self.osd = window.canvas.create_image(self.position[0],
        self.position[1], image = self.image, anchor = 'nw')
    def move(self, window):
        if self.state == 3:
            if self.position[0] % 64 != 0:
                print('x:', self.position[0])
            if self.position[1] % 64 != 0:
                print('y:', self.position[1])
            if self.alpha ==self.target_alpha:
                self.state = 0
            elif 0<self.target_alpha - self.alpha <180 :
                self.alpha += self.rotating_speed
                self.alpha = self.alpha%360
            else:
                self.alpha -= self.rotating_speed
                self.alpha = self.alpha%360

        elif self.state == 0:
            if self.check_collision(window):
                pass
            else:
                newx = int(self.position[0] - sin(self.alpha*pi/180) * self.speed)
                newy = int(self.position[1] - cos(self.alpha*pi/180) * self.speed)
                if newx < 0 :
                    self.position[0] = 0
                    self.rotate()
                elif newx > (window.geometry[0]-1) * 64 :
                    self.position[0] = (window.geometry[0]-1) * 64
                    self.rotate()
                else :
                    self.position[0] = newx
                if newy < 0 :
                    self.position[1] = 0
                    self.rotate()
                elif newy > (window.geometry[1] - 1) * 64 :
                    self.position[1] = (window.geometry[1] - 1) * 64
                    self.rotate()
                else :
                    self.position[1] = newy
    def rotate(self):
        self.state = 3
        self.target_alpha = self.alpha + random.choices((90, -90, 180),(0.45, 0.45, 0.1))[0]
        self.target_alpha = self.target_alpha%(360)
    def check_collision(self, window):
        for block in window.obstacles:
            # if block.position[0] - 64 < self.position[0] < block.position[0]:
            #     if self.position[1] == block.position[1] - 64:
            #         self.position[0] = block.position[0] - 64
            #         self.rotate()
            #         return True
            #     if self.position[1] == block.position[1]):
            #         self.position[0] == block.position[1] - 64
            #         self.rotate()
            #         return True
            #
            # if block.position[0] < self.position[0] < block.position[0] + 64:
            #     if self.position[1] == block.position[1]:
            #         self.position[0] = block.position[0]
            #         self.rotate()
            #         return True
            #     if self.position[1] == block.position[1]):
            #         self.position[0] == block.position[1] - 64
            #         self.rotate()
            #         return True
            if block.position[0]-64<self.position[0]<block.position[0] and self.position[1] == block.position[1]:
                self.position[0] = block.position[0]-64
                self.rotate()
                return True
            if block.position[0]<self.position[0]<block.position[0]+64 and self.position[1] == block.position[1]:
                self.position[0] = block.position[0] + 64
                self.rotate()
                return True
            if block.position[1]-64<self.position[1]<block.position[1] and self.position[0] == block.position[0]:
                self.position[1] = block.position[1]-64
                self.rotate()
                return True
            if block.position[1]<self.position[1]<block.position[1]+64 and self.position[0] == block.position[0]:
                self.position[1] = block.position[1] + 64
                self.rotate()
                return True

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
