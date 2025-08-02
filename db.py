from pathlib import Path
import sqlite3 as sql
from classes import Book, Client
import re

class DataBase(Book, Client):
    def __init__(self):
        Book.__init__(self)
        Client.__init__(self)
        self.DB_FILE = Path(__name__).parent / 'book_data_base.db'
        self.TABLE_NAME_1 = 'book_price'
        self.TABLE_NAME_2 = 'client_book'

    def open_connection(self):
        self.connection = sql.connect(self.DB_FILE)
        self.cursor = self.connection.cursor()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def create_table(self):
        try:

            self.cursor.execute('PRAGMA foreign_keys = ON;')

            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.TABLE_NAME_1}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                book TEXT NOT NULL UNIQUE, 
                price REAL NOT NULL);''')
            
            self.cursor.execute(f'''
                CREATE TABLE IF NOT EXISTS {self.TABLE_NAME_2}
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                client TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                book_id INTEGER NOT NULL,
                FOREIGN KEY (book_id) REFERENCES {self.TABLE_NAME_1}(id) ON DELETE CASCADE); ''')
            
            self.cursor.execute(f'''
                SELECT {self.TABLE_NAME_2}.client, {self.TABLE_NAME_1}.book
                FROM {self.TABLE_NAME_2}
                JOIN {self.TABLE_NAME_1} ON {self.TABLE_NAME_2}.book_id = {self.TABLE_NAME_1}.id''')
            
            self.connection.commit()

        
        except Exception:
             print('Error to create the tables!')
             print()

    def insert_book_table_1(self):
            try:

                data = (
                    f'INSERT INTO {self.TABLE_NAME_1}'
                    '(book, price)'
                    'VALUES'
                    '(?, ?);')
                
                self.cursor.executemany(data, list(zip(self.book_price['Book'], self.book_price['Price'])))
                print('Books inserted successfully!')
                print()
                self.connection.commit()

            except sql.OperationalError:
                print('Error to insert data into the table!')
                print()

    def buy_book(self):
         while True:
            try:
                client_name = input('Type the Client name: ')
                for y in client_name:
                    if y.isdigit():
                        raise ValueError

                email_format = r'^[\w\.-]+@[\w\.-]+\.\w{3,}$'

                client_email = input('Type the client E-mail: ')
                print()
                if not re.match(email_format, client_email):
                    raise ValueError

                self.cursor.execute(f'''
                SELECT book, price, id FROM {self.TABLE_NAME_1};
                ''')
              
                self.books = self.cursor.fetchall()

                for i, row in enumerate(self.books, start=1):
                    book, price, _id = row
                    print(f'{i} - {book} | {price} | {_id}')
                
                book_choice = int(input('Type the Book index wished to buy: '))

                if book_choice < 1 or book_choice > len(self.books):
                    raise ValueError
                
                book_selected_id = self.books[book_choice - 1][2]
                                 

                self.client_book['Client'].append(client_name)
                self.client_book['Book'].append(book_selected_id)
                self.client_book['Email'].append(client_email)
                
                break
            
            except ValueError:
                print('Invalid input!')
                print()
                continue

    def insert_client_table_2(self):
        try:
            data = (f'''
            INSERT INTO {self.TABLE_NAME_2}
            (client, email, book_id)
            VALUES
            (?, ?, ?);''')

            self.cursor.executemany(data, list(zip(self.client_book['Client'], self.client_book['Email'], self.client_book['Book'])))
            self.connection.commit()

            print('Client inserted successfully!')
            print()

        except Exception:
            print('Error to insert clients into the table!')
            print()

    def delete_table_1(self):
        while True:
            try:
        
                self.cursor.execute(f'''
                SELECT id, book, price FROM {self.TABLE_NAME_1};''')

                books = self.cursor.fetchall()

                for i, row in enumerate(books, start=1):
                    id_, book, price = row
                    print(f'{i} - {id_} {book} | {price}')
                print()

                delete_input = int(input('Type the id of the Book wished to delete: '))
                print()

                ids = [row[0] for row in books]
                if delete_input not in ids:
                    print('ID not found!')
                    print()
                    continue

                self.cursor.execute(f'''
                DELETE FROM {self.TABLE_NAME_1}
                WHERE id = ?; ''', (delete_input,))

                self.connection.commit()

                print(f'id: {delete_input} deleted successfully!')
                print()
            
                break

            except ValueError:
                print('Invalid input!')
                continue
            except Exception:
                print('Error to delete Book from the table!')

    def delete_table_2(self):
        while True:
            try:
                
                self.cursor.execute(f'''
                SELECT id, client, email, book_id FROM {self.TABLE_NAME_2};''')

                clients = self.cursor.fetchall()

                for i, row in enumerate(clients, start=1):
                    id_, client, email, book_id = row
                    print(f'{i} - {id_} {client} | {email} | {book_id}')

                delete_input = int(input('Type the id of the Client wished to delete: '))
                print()

                ids = [row[0] for row in clients]
                if delete_input not in ids:
                    print('ID not found!')
                    print()
                    continue

                self.cursor.execute(f'''
                    DELETE FROM {self.TABLE_NAME_2}
                    WHERE id = ?; ''', (delete_input,))
                
                self.connection.commit()

                print(f'id: {delete_input} deleted successfully!')
                print()

                break

            except ValueError:
                print('Invalid input!')
                continue
            except Exception:
                print('Error to delete Book from the table!')  