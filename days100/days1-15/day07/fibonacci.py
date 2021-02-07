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


def recursive_fib(n):
    if n <= 1:
        return n
    else:
        """
        n = 4:
        recursive_fib(3) + recursive_fib(2)
        recursive_fib(2) + recursive_fib(1) + recursive_fib(1) + recursive_fib(0)
        recursive_fib(1) + 1 + 1 + 0
        1 + 1 + 1 + 0
        """
        return recursive_fib(n - 1) + recursive_fib(n - 2)


def main():
    # for val in fib(20):
    #     print(val)
    for val in range(1, 21):
        print(recursive_fib(val))


if __name__ == '__main__':
    main()
