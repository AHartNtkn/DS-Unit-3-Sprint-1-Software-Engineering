from acme import Product
from random import randint, choice, uniform


def mean(l):
    return sum(l)/len(l)

ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    newProds = [Product(
                  " ".join([choice(ADJECTIVES), choice(NOUNS)]),
                  randint(5, 100),
                  randint(5, 100),
                  uniform(0.0, 2.5))
                for _ in range(num_products)]

    return newProds


def inventory_report(products):
    unique_names = len(set([p.name for p in products]))
    mean_price = mean([p.price for p in products])
    mean_weight = mean([p.weight for p in products])
    mean_flammability = mean([p.flammability for p in products])

    print("ACME CORPORATION OFFICIAL INVENTORY REPORT",
          "\nUnique product names: ", unique_names,
          "\nAverage price: ", mean_price,
          "\nAverage weight: ", mean_weight,
          "\nAverage flammability: ", mean_flammability)

if __name__ == '__main__':
    inventory_report(generate_products())
