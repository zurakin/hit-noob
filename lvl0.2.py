import game, settings


root = game.Game(title = 'level 0',geometry = (20,11))
map_file = 'maps/lvl0.2.txt'
root.load_map(map_file)
root.display_map()
root.run(refresh_rate = settings.refresh_rate)
root.root.mainloop()
