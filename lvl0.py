import game, settings


root = game.Game(title = 'level 0')
map_file = 'maps/lvl0.txt'
root.load_map(map_file)
root.display_map()
root.run(refresh_rate = settings.refresh_rate)
root.root.mainloop()
