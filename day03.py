def start(func):
    def func2():
        print('start')
        func()
        print('end')

    return func2()


def temp():
    pass


start(temp)

