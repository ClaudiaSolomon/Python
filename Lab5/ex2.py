class Account:
    def __init__(self, suma):
        self.suma = suma

    def deposit(self, value):
        self.suma += value

    def withdraw(self, value):
        if self.suma >= value:
            self.suma -= value

    def interest_calcul(self):
        return None


class SavingsAccount(Account):
    def __init__(self, suma, rate):
        super().__init__(suma)
        self.rate = rate

    def interest_calcul(self):
        interest = self.suma * self.rate
        return interest


class CheckingAccount(Account):
    def __init__(self, suma, comision):
        super().__init__(suma)
        self.comision = comision

    def deposit(self, value):
        super().deposit(value)
        self.suma -= self.comision

    def withdraw(self, value):
        super().withdraw(value)
        self.suma -= self.comision


def main():
    savings_account = SavingsAccount(10, 0.01)
    print(savings_account.interest_calcul())
    checking_account = CheckingAccount(10, 1)
    checking_account.deposit(12)
    checking_account.withdraw(2)
    print(checking_account.suma)


if __name__ == '__main__':
    main()
