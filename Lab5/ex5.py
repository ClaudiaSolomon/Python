class Animal:
    def __init__(self, number_of_legs):
        self.number_of_legs = number_of_legs

    def has_babies(self):
        return 0


class Mammal(Animal):
    def __init__(self, number_of_legs, babies):
        super().__init__(number_of_legs)
        self.babies = babies

    def has_babies(self):
        if self.babies > 0:
            return 1
        else:
            return 0

    def runs(self):
        print("running with " + str(self.number_of_legs) + " legs")


class Bird(Animal):
    def __init__(self, number_of_legs, eggs):
        super().__init__(number_of_legs)
        self.eggs = eggs

    def has_babies(self):
        if self.eggs > 0:
            return 1
        else:
            return 0

    def flies(self):
        print("flying with " + str(self.number_of_legs) + " legs")


class Fish(Animal):
    def __init__(self, number_of_legs, fish_roe):
        super().__init__(number_of_legs)
        self.fish_roe = fish_roe

    def has_babies(self):
        if self.fish_roe > 0:
            return 1
        else:
            return 0

    def swims(self):
        print("swimming with " + str(self.number_of_legs) + " legs")


def main():
    mammal=Mammal(4,7)
    print(mammal.has_babies())
    fish=Fish(3,100)
    fish.swims()


if __name__ == '__main__':
    main()