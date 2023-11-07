class Employee:
    def __init__(self, salary):
        self.salary = salary

    def is_successful(self):
        return 0


class Engineer(Employee):
    def __init__(self, salary, number_of_projects):
        super().__init__(salary)
        self.number_of_projects = number_of_projects

    def is_successful(self):
        if self.number_of_projects > 5:
            return 1
        else:
            return 0


class Manager(Employee):
    def __init__(self, salary, number_of_teams):
        super().__init__(salary)
        self.number_of_teams = number_of_teams

    def is_successful(self):
        if self.number_of_teams > 10:
            return 1
        else:
            return 0


class Salesperson(Employee):
    def __init__(self, salary, number_of_sales):
        super().__init__(salary)
        self.number_of_sales = number_of_sales

    def is_successful(self):
        if self.number_of_sales > 100:
            return 1
        else:
            return 0


def main():
    salesperson = Salesperson(10000, 75)
    print(salesperson.is_successful())
    engineer = Engineer(20000, 10)
    print(engineer.is_successful())


if __name__ == '__main__':
    main()
