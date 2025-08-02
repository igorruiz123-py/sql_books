from db import DataBase
from time import sleep
from os import system

if __name__ == '__main__':
    while True:
        for i in range(1):
            print('1 - Create the tables')
            sleep(0.5)
            print('2 - Insert book to the Book Table')
            sleep(0.5)
            print('3 - Insert Clients to the Clients Table')
            sleep(0.5)
            print('4 - Delete data from Book Table')
            sleep(0.5)
            print('5 - Delete data from the Client Table')
            sleep(0.5)
        print()
        
        input_ = int(input('Choose an option ("no" to exit): '))
        system('cls')
        print()

        if input_ not in range(1, 6):
            print('Invalid input!')
            print()
            continue

        elif input_ == 1:
            run = DataBase()
            run.open_connection()
            run.create_table()
            run.close_connection()

        elif input_ == 2:
            run = DataBase()
            run.open_connection()
            run.book_entry()
            run.insert_book_table_1()
            run.close_connection()

        elif input_ == 3:
            run = DataBase()
            run.open_connection()
            run.buy_book()
            run.insert_client_table_2()
            run.close_connection()

        elif input_ == 4:
            run = DataBase()
            run.open_connection()
            run.delete_table_1()
            run.close_connection()

        elif input_ == 5:
            run = DataBase()
            run.open_connection()
            run.delete_table_2()
            run.close_connection()

        elif input_ == 'no':
            break

        else:
            print('Invalid input!')