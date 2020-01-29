import tkinter, map, multiprocessing, time, media_creator
from PIL import ImageTk, Image


class Window():

    def __init__(self, title, geometry = (7,6)):
        self.root = tkinter.Tk()
        self.root.title(title)
        self.geometry = geometry
        self.root.geometry('{}x{}'.format( str(geometry[0]*64) , str(geometry[1]*64) ) )
        self.canvas = tkinter.Canvas(self.root, bg = 'blue')
        self.canvas.pack(expand = 'yes', fill = 'both')
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
                self.obstacles.append(map.Block(image_file = line[3].strip(),
                 position = (int(line[0]), int(line[1]))))

            if line[2].strip() == '2':
                self.bugs.append(map.Bug(image_file = line[3].strip(),
                 position = (int(line[0]), int(line[1]))))
            if line[2].strip() == '0':
                self.player = map.Block(image_file = line[3].strip(),
                 position = (int(line[0]), int(line[1])))
    def display_map(self):
        for obstacle in self.obstacles:
            obstacle.display(self)
        for bug in self.bugs:
            bug.display(self)
        self.player.display(self)

    def run(self, refresh_rate = 30):
        while True:
            for bug in bugs:
                self.canvas.delete(bug.osd)
                bug.display(self)

            self.canvas.delete(player.osd)
            self.player.display(self)
            time.sleep(1/30)
