class Queue:
    def __init__(self):
        self.coada = []

    def push(self, number):
        self.coada.append(number)

    def pop(self):
        if len(self.coada) != 0:
            el = self.coada[0]
            self.coada[0] = None
            for i in range(len(self.coada) - 1):
                self.coada[i] = self.coada[i + 1]
            return el
        else:
            return None

    def peek(self):
        if len(self.coada) != 0:
            return self.coada[0]
        else:
            return None
