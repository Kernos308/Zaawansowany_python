from functools import reduce


# zad1

class CitiesIterator:
    def __init__(self, cities):
        self.cities = cities
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < len(self.cities):
            current_city = self.cities[self.idx]
            self.idx += 1
            return current_city
        else:
            raise StopIteration


def print_cities(cities):
    iterator = CitiesIterator(cities)
    while True:
        try:
            city = next(iterator)
            print(city)
        except StopIteration:
            break


cities_list = ["Warszawa", "Berlin", "Kijow", "Praga", "Paryz"]
print_cities(cities_list)

# zad5


cel = [5, 7.3, 30, 22, 21]

celsius_to_fahrenheit = map(lambda x: x * (9 / 5) + 32, cel)
print(list(celsius_to_fahrenheit))

# zad6

fahrenheit = [41.0, 45.14, 86.0, 71.6, 69.8]

fahrenheit_to_celsius = map(lambda x: (x - 32) * 5 / 9, fahrenheit)
print(list(fahrenheit_to_celsius))

# zad7

fibb = [1, 2, 3, 4, 5]

fibb_odd = list(filter(lambda x: x % 2 == 1, fibb))
print(fibb_odd)

# zad8

fibb_even = list(filter(lambda x: x % 2 == 0, fibb))
print(fibb_even)

# zad9

tab = [1, 5, 12, 55, 141, 0, 2, 3]

max_from_tab = reduce(max, tab)
print(max_from_tab)

# zad10

max_from_tab = reduce(lambda x, y: x if x > y else y, tab)
print(max_from_tab)
