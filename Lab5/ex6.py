class LibraryItem:
    def __init__(self, price):
        self.price = price

    def display_info(self):
        return "item"

    def return_item(self, was_bought):
        if was_bought == 1:
            return "it can be returned"
        else:
            return "it cant be returned"

    def checkout(self, money):
        if money >= self.price:
            return "it can be bought"
        else:
            return "it cant be bought"


class Book(LibraryItem):
    def __init__(self, price, category):
        super().__init__(price)
        self.category = category

    def display_info(self):
        return "price: " + str(self.price) + " category: " + self.category


class DVD(LibraryItem):
    def __init__(self, price, color):
        super().__init__(price)
        self.color = color

    def display_info(self):
        return "price: " + str(self.price) + " color: " + self.color


class Magazine(LibraryItem):
    def __init__(self, price, pages):
        super().__init__(price)
        self.pages = pages

    def display_info(self):
        return "price: " + str(self.price) + " pages: " + str(self.pages)


def main():
    magazine = Magazine(100, 25)
    print(magazine.return_item(1))
    book = Book(50, "romance")
    print(book.display_info())
    dvd = DVD(35, "blue")
    print(dvd.checkout(30))


if __name__ == '__main__':
    main()
