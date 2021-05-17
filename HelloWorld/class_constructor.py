class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


person = Person('Troni Dale')
person.talk()

bob = Person('Bob Smith')
bob.talk()
