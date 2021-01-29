def foo():
    pass


def bar():
    global b
    b = 200
    print(b)


if __name__ == '__main__':
    print('call foo()')
    foo()

    print('call bar()')
    b = 100
    bar()
    print(b)
