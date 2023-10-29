class Stack:
    def __init__(self):
        self.stiva = []

    def push(self, number):
        self.stiva.append(number)

    def pop(self):
        if len(self.stiva) != 0:
            el = self.stiva[len(self.stiva) - 1]
            self.stiva = self.stiva[:(len(self.stiva) - 1)]
            return el
        else:
            return None

    def peek(self):
        if len(self.stiva) != 0:
            return self.stiva[len(self.stiva) - 1]
        else:
            return None
