# Class definition

class Animal(object):
    """Makes cute animals."""
    # For initializing our instance objects
    def __init__(self, name, age, is_hungry):
        self.name = name
        self.age = age
        self.is_hungry = is_hungry

    def descript(self):
        print('method called')


zebra = Animal("Jeffrey", 2, True)
giraffe = Animal("Bruce", 2, False)
panda = Animal("Chad", 7, True)


print(zebra.name, zebra.age, zebra.is_hungry)
print(giraffe.name, giraffe.age, giraffe.is_hungry)
print(panda.name, panda.age, panda.is_hungry)

zebra.descript()
