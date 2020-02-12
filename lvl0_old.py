
if __name__ == '__main__':
    import gui, objects, multiprocessing, temp
    # def foo():
    #     global root
    #     root.run(30)
    root = gui.Window(title = 'level 0')
    map_file = 'maps/lvl0.txt'
    root.load_map(map_file)
    root.display_map()


    #
    multiprocessing.set_start_method('spawn')
    p = multiprocessing.Process(target = temp.run, args =[root])
    # p = multiprocessing.Process(target = foo)
    p.start()
    p.join()

    ##
    root.root.mainloop()
