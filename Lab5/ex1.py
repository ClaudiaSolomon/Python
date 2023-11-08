import math


class Shape:
    def __init__(self):
        self.area = 1
        self.perimeter = 0

    def area_calcul(self):
        return self.area

    def perimeter_calcul(self):
        return self.perimeter


class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    def area_calcul(self):
        self.area = self.radius * self.radius * math.pi
        return super().area_calcul()

    def perimeter_calcul(self):
        self.perimeter = 2 * self.radius * math.pi
        return super().perimeter_calcul()


class Triangle(Shape):
    def __init__(self, edge1, edge2, edge3):
        super().__init__()
        self.edge1 = edge1
        self.edge2 = edge2
        self.edge3 = edge3

    def area_calcul(self):
        s = self.perimeter_calcul()/2
        self.area = math.sqrt(s * (s - self.edge1) * (s - self.edge2) * (s - self.edge3))
        return super().area_calcul()

    def perimeter_calcul(self):
        self.perimeter = self.edge1 + self.edge2 + self.edge3
        return super().perimeter_calcul()


class Rectangle(Shape):
    def __init__(self, edge1, edge2):
        super().__init__()
        self.edge1 = edge1
        self.edge2 = edge2

    def area_calcul(self):
        self.area = self.edge1 * self.edge2
        return super().area_calcul()

    def perimeter_calcul(self):
        self.perimeter = 2 * (self.edge1 + self.edge2)
        return super().perimeter_calcul()


def main():
    triangle = Triangle(1, 2, 3)
    print(triangle.perimeter_calcul())
    rectangle = Rectangle(3, 4)
    print(rectangle.area_calcul())


if __name__ == '__main__':
    main()
