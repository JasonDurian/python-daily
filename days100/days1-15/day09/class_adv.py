class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property  # getter
    def name(self):
        return self._name

    @property  # getter
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s is playing the piano' % self._name)
        else:
            print('%s is playing cards' % self._name)


def main():
    person = Person('Jason', 12)
    person.play()
    person.age = 22
    person.play()
    # person.name = 'Oreo'


if __name__ == '__main__':
    main()
