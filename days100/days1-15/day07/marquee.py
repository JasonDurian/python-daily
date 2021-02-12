import os
import time


def main():
    content = 'Welcome to Suzhou'
    i = 10
    while i > 0:
        os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]
        i -= 1


if __name__ == '__main__':
    main()
