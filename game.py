import tkinter, Block, Bug, Player, multiprocessing, time, media_creator, sys, keyboard, random
from PIL import ImageTk, Image
from math import pi


class Game():

    def __init__(self, title, geometry = (7,6)):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.geometry = geometry
        self.root.geometry('{}x{}'.format( str(geometry[0]*64) , str(geometry[1]*64) ) )
        self.canvas = tkinter.Canvas(self.root, bg = 'blue')
        self.canvas.pack(expand = 'yes', fill = 'both')
        self.running = True
        self.add_keybinds()
        self.add_objects()

    def stop(self, *args):
        self.running = False

    def add_keybinds(self):
        self.root.bind('q', self.stop)
        # self.root.bind('<Up>', lambda *args : self.player.move((0,-1)))
        # self.root.bind('<Down>', lambda *args : self.player.move((0,1)))
        # self.root.bind('<Right>', lambda *args : self.player.move((1,0)))
        # self.root.bind('<Left>', lambda *args : self.player.move((-1,0)))
    def check_movement(self):
        if keyboard.is_pressed('up'):
            self.player.move(-1, self)
            if keyboard.is_pressed('right'):
                self.player.rotate(-9)
            if keyboard.is_pressed('left'):
                self.player.rotate(9)
        if keyboard.is_pressed('down'):
            self.player.move(1, self)
            if keyboard.is_pressed('right'):
                self.player.rotate(-9)
            if keyboard.is_pressed('left'):
                self.player.rotate(9)
    def add_objects(self):
        self.obstacles = []
        self.bugs = []
        self.player = None


    def load_map(self, map_file):
        self.bg_array = media_creator.make_background(self.geometry,
         [0,204,204])
        self.bg_image = Image.fromarray(self.bg_array)
        self.bg_photo = ImageTk.PhotoImage(image = self.bg_image)
        self.bg = self.canvas.create_image(0, 0, image = self.bg_photo,
         anchor = 'nw')
        with open(map_file, 'r') as file:
            lines = file.readlines()
            lines = [line.strip().split(':') for line in lines]
        for line in lines :
            if line[2].strip() == '1':
                self.obstacles.append(Block.Block(
                image_file = line[3].strip(),
                 position = [int(line[0]) * 64, int(line[1]) * 64]))

            if line[2].strip() == '2':
                self.bugs.append(Bug.Bug(image_file = line[3].strip(),
                 position = [int(line[0]) * 64, int(line[1]) * 64]))
            if line[2].strip() == '0':
                self.player = Player.Player(image_file = line[3].strip(),
                 position = [int(line[0]) * 64, int(line[1]) * 64])
    def display_map(self):
        for obstacle in self.obstacles:
            obstacle.display(self)
        for bug in self.bugs:
            bug.display(self)
        self.player.display(self)

    def run(self, refresh_rate = 30):
        while self.running:
            self.check_movement()
            for bug in self.bugs:
                bug.check_danger(self)
                if not bug.rotating and bug.position[0] %64 == 0 and bug.position[1] %64 == 0 and random.choices([True, False], [0.25, 0.75])[0]:
                    bug.rotate()
                bug.move(self)
                self.canvas.delete(bug.osd)
                bug.display(self)
            self.canvas.delete(self.player.osd)
            self.player.display(self)
            time.sleep(1/refresh_rate)
            self.root.update()
        self.root.destroy()
