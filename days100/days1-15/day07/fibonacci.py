def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
        """
        a, b
        1, 1
        1, 2
        2, 3
        3, 5
        5, 8
        """
        yield a


def main():
    for val in fib(20):
        print(val)


if __name__ == '__main__':
    main()
