import zadanie_1 as z1

class Slice(z1.Pizza):

    __how_many_slices: int

    def __init__(self, how_many_slices: int):
        if how_many_slices<4 or how_many_slices>12 or how_many_slices%2 != 1:
            print("Quantity of slices is wrong")
            exit(-10)
        self.__how_many_slices = how_many_slices

    def part_price(self, ordered_slices):
        return ordered_slices