import multiprocessing, temp

if __name__ == '__main__':
    a = 'zura'
    p = multiprocessing.Process(target = temp.foo, args = [a])
    p.start()
    p.join()
    print(a)
