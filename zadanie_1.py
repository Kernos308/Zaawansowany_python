import math
import sys

class Pizza():
    __price: float
    __toppings: list[str]
    __diameter: float

    @staticmethod
    def area(diameter: float):
        return math.pi * math.pow(diameter * 0.5, 2)

    def __init__(self, diameter: float, toppings: list[str]):
        if diameter<20:
            print("Wrong radius")
            sys.exit(-10)
        self.__toppings = toppings
        self.__diameter = diameter
        self.__price = 0.005 * self.area(self.__diameter) + float(len(self.__toppings)) * 2.0

    @property
    def diameter(self):
        return self.__diameter

    @diameter.setter
    def diameter(self, diameter: float):
        if diameter<20:
            print("Wrong radius")
            sys.exit(-10)
        self.__diameter = diameter
        self.__price = 0.005 * area(self.__diameter) + len(self.__toppings) * 2

    def add_topping(self, topping: str):
        self.__toppings.append(topping)
        self.__price +=2

    def __repr__(self):
        if not self.__toppings:
            print("Pizza:\nsrednica: ", self.__diameter)
        else:
            print("Pizza:\nsrednica: ", self.__diameter)
            print("dodatki: ", [x for x in self.__toppings])
        return f"cena: {self.__price:.2f}"

    def __add__(self, diameter: float, toppings: list[str]):
        self.__diameter = max(self.__diameter, diameter)
        self.__toppings = self.__toppings + toppings


