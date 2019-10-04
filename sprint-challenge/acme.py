from random import randint


class Product():
    """A class for forming descriptors of Acme products"""
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000, 9999999)

    def stealability(self):
        steal_val = self.price / self.weight
        if steal_val < 0.5:
            return "Not so stealable..."
        elif steal_val < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        explode_val = self.flammability * self.weight
        if explode_val < 10:
            return "...fizzle."
        elif explode_val < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"


class BoxingGlove(Product):
    """A class describing the Acme Boxing Glove product"""
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"