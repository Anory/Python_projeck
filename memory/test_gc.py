

class Cat(object):
    def __init__(self):
        print("对象产生了{}".format(id(self)))

    def __del__(self):
        print("对象删除了{}".format(id(self)))


# def f():
#     while True:
#         c = Cat()

def f1():
    l = []
    while True:
        c = Cat()
        l.append(c)


if __name__ == '__main__':
    f1()
