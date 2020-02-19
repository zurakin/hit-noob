import numpy, random
from PIL import ImageTk, Image
from math import cos, sin, pi, acos, sqrt

class Bug():
    def __init__(self, position, image_file = 'media/bug.png', hp = 100, speed = 4):
        self.hp = hp
        self.speed = speed
        self.rotating_speed = 6
        self.alpha = 90
        self.beta = 0
        self.target_alpha = 0
        self.view_distance = 192
        self.fov = 90
        self.rotating = False
        self.endangered = False
        self.load = Image.open(image_file)
        self.load2 = Image.open('media/endangered_bug.png')
        self.loadfov = Image.open('media/fov.png')
        self.position = position
        self.sleep = 0

    def display(self, window):
        if self.endangered:
            self.image = ImageTk.PhotoImage(image = self.load2.rotate(self.alpha))
            self.imagefov = ImageTk.PhotoImage(image = self.loadfov.rotate(self.alpha+ 90))
        else:
            self.image = ImageTk.PhotoImage(image = self.load.rotate(self.alpha))
            self.imagefov = ImageTk.PhotoImage(image = self.loadfov.rotate(self.alpha+ 90))

        self.osd = window.canvas.create_image(self.position[0],
        self.position[1], image = self.image, anchor = 'nw')
        #
        O = (self.position[0] + 32, self.position[1]+32)
        radalpha = self.alpha*pi/180
        A = [O[0]+128*cos(radalpha+ pi/2), O[1]-128*sin(radalpha+pi/2)]
        #
        self.osdfov = window.canvas.create_image(A[0],
        A[1], image = self.imagefov, anchor = 'center')

    def move(self, window):
        if self.rotating:
            # if self.position[0] % 64 != 0:
            #     print('x:', self.position[0])
            # if self.position[1] % 64 != 0:
            #     print('y:', self.position[1])
            if self.alpha ==self.target_alpha:
                self.rotating = False
            elif 0<self.target_alpha - self.alpha <180 :
                self.alpha += self.rotating_speed
                self.alpha = self.alpha%360
            else:
                self.alpha -= self.rotating_speed
                self.alpha = self.alpha%360

        elif not self.rotating:
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

    def check_danger(self, window):
        x, y = self.position[0]+32, self.position[1]+32
        xp, yp = window.player.position[0]+32, window.player.position[1]+32
        n2 = sqrt((xp-x)**2 + (y-yp)**2)
        if n2 > self.view_distance:
            self.endangered = False
            return
        angle = (self.alpha+90)%360
        pscal = (cos(angle*pi/180)*(xp-x)) + (+sin(angle*pi/180)*(y-yp))
        if n2== 0 :
            pass
        else:
            self.beta = acos(pscal/n2)*180/pi
        if self.beta < self.fov/2:
            self.endangered = True
        else:
            self.endangered = False

    def rotate(self):
        self.rotating = True
        self.target_alpha = self.alpha + random.choices((90, -90, 180),(0.45, 0.45, 0.1))[0]
        self.target_alpha = self.target_alpha%(360)
    def check_collision(self, window):
        for block in window.obstacles:
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
