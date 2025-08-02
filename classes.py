from abc import ABC, abstractmethod
from os import system


class Client(ABC):
    def __init__(self):
        self.client_book = {'Client': [], 'Book': [], 'Email': []}
        super().__init__()

    @abstractmethod
    def buy_book(self):
        pass


class Book():
    def __init__(self):
        self.book_price = {'Book': [], 'Price': []}

    def book_entry(self):
        while True:
            try:
                book_amount = int(input('Type the amount of books wished to register: '))
                system('cls')
                print()

                for x in range(book_amount):
                    name = input('Type the Book name: ').strip()
                    price = float(input('Type the Book price: '))
                    print()

                    self.book_price['Book'].append(name)
                    self.book_price['Price'].append(price)

                break

            except ValueError:
                print('Invalid input!')
                print()
                continue