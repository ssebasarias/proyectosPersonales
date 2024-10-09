class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f'El libro {self.title} ha sido prestado')
        else:
            print(f'El libro {self.title} no esta disponible')

    def return_book(self):
        self.available = True
        print(f'El libro {self.title} ha sido devuelto')

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            print(f'Se presto correctamente')
        else:
            print(f'El libro {book.title} no esta disponible')

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print('Se ha devuelto correctamente')
        else:
            print(f'El libro {book.title} no esta en la lista')

class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_books(self, book):
        self.books.append(book)
        print(f'Se agrego correctamente {book.title}')

    def add_users(self, user):
        self.users.append(user)
        print(f'Se agrego correctamente {user.name}')

    def show_available_books(self):
        print(f'Libros disponibles: ')
        for book in self.books:
            if book.available:
                print(f'{book.title} por {book.author}')

book1 = Book('Mi lucha', 'Hitler')
book2 = Book('El Principito', 'Antonie de Saint')
book3 = Book('Game Of Thrones', 'Gorge R.R. Martin')

user1 = User('Sebastian', '001')

library = Library()
library.add_books(book1)
library.add_books(book2)
library.add_books(book3)

library.add_users(user1)

library.show_available_books()
user1.borrow_book(book1)
library.show_available_books()
user1.return_book(book1)
library.show_available_books()
