class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s is studying %s.' % (self.name, course_name))

    def watch_movie(self):
        if self.age < 18:
            print('%s only can watch Bear.' % self.name)
        else:
            print('%s is watching AV.' % self.name)


class Test:
    def __init__(self, foo):
        self.__foo = foo

    def __bar(self):
        print(self.__foo)
        print('__bar')


def main():
    stu1 = Student('Jason', 24)
    stu1.study('Python Crash Course')
    stu1.watch_movie()
    stu2 = Student('Oreo', 16)
    stu2.study('Cooking')
    stu2.watch_movie()

    test = Test('hello')
    # test.__bar()
    # print(test.__foo)
    test._Test__bar()
    print(test._Test__foo)


if __name__ == '__main__':
    main()
