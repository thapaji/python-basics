class Person:
    def __init__(self, age, weight, height, first_name, last_name, catch_phrase):
        self.age = age
        self.weight = weight
        self.height = height
        self.first_name = first_name
        self.last_name = last_name
        self.catch_phrase = catch_phrase

    def walk(self):
        print(f'{self.first_name} is walking')

    def talk(self):
        print(f'Welcome to {self.last_name} talk')


def main():
    user = Person(25, 80, 177, "Sujan", 'Thapa', 'I am full stack developer')
    print(user.catch_phrase)
    user.walk()
    user.talk()


main()
