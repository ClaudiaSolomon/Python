class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def calculate_mileage(self):
        return 5

    def calculate_towing(self):
        return 0


class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self):
        if self.year < 2000:
            return 10
        else:
            return 7

    def calculate_towing(self):
        if self.make == "Jeep":
            return 1000
        else:
            return 750


class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_mileage(self):
        if self.year < 2000:
            return 15
        else:
            return 9


class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

    def calculate_towing(self):
        return 2000


def main():
    car = Car("Toyota", "Camry", 2020)
    print(car.calculate_mileage())
    truck = Truck("Ford", "F-150", 2019)
    print(truck.calculate_towing())
    motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2022)
    print(motorcycle.calculate_towing())


if __name__ == '__main__':
    main()
