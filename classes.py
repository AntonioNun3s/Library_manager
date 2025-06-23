import json
from datetime import date, timedelta, datetime

class Book:
        
    def __init__(self, title, ID, author, ISBN, cate, borr, owner, date):
        self.title = title
        self.ID = ID
        self.author = author
        self.ISBN = ISBN
        self.category = cate
        self.borrowed = borr
        self.owner_ID = owner
        self.exp_date = date
    
    def toDict(self):
        return self.__dict__
    

class User:

    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.books_borrowed = []
    
    def toDict(self):
        return self.__dict__
    # borrows a book
    def borrow_book(self, ID):

        if len(self.books_borrowed) >= 3:
            return 2
        
        for book in library.books:
            if book.ID == ID and book.borrowed == False:
                self.books_borrowed.append(book)
                book.borrowed = True
                book.owner_ID = self.ID
                book.exp_date = date.today() + timedelta(weeks=2)
                library.borrowed_books.append(book)
                return 1
            
        return 0
    # returns book to the library
    def return_book(self, ID):

        if len(self.books_borrowed) <= 0:
            return 2

        for book in self.books_borrowed:
            if book.ID == ID:
                book.borrowed = False
                book.owner_ID = None
                book.exp_date = None
                self.books_borrowed.remove(book)
                library.borrowed_books.remove(book)
                return 1
        return 0

    
class Library:

    def __init__(self):
        self.books = []
        self.users = []
        self.borrowed_books = []
        self.load_data()
    # loads data automatically when opening the program and saving it
    def load_data(self):

        with open("library_manager/data.json", 'r') as file:
            loaded_data = json.load(file)

            self.books = []
            self.users = []
            self.borrowed_books = []

            for user in loaded_data["users"]:

                user_o = User(user["name"], user["ID"])
                self.users.append(user_o)

            for book in loaded_data["books"]:
                
                if book["exp_date"] != None:
                    book["exp_date"] = datetime.strptime(book["exp_date"], "%Y-%m-%d").date()
                        
                book_o = Book(book["title"], book["ID"], book["author"], book["ISBN"], book["category"], book["borrowed"], book["owner_ID"], book["exp_date"])
                self.books.append(book_o)

                if book_o.owner_ID != None:
                    self.redirect_to_user(book_o.owner_ID, book_o) # when loading the JSON, this function inserts the book object on the User that has borrowed it before

                if book_o.borrowed == True:
                    self.borrowed_books.append(book_o)
        # save the data to the json
    def save_data(self):

        to_json = {}
        to_json["books"] = []
        to_json["users"] = []
        # saves all the books
        for book in self.books:

            book = book.__dict__

            if book["exp_date"] != None:

                book["exp_date"] = str(book["exp_date"])

            to_json["books"].append(book)

            # checks if the user has any book borrowed and saves the user
        for idx, user in enumerate(self.users):

            user_a = []
            user = user.__dict__

            for book in user["books_borrowed"]:

                user["books_borrowed"]

                book = book.__dict__

                if book["exp_date"] != None:

                    book["exp_date"] = str(book["exp_date"])

                user_a.append(book)
            user["books_borrowed"].clear()
            to_json["users"].append(user)
            for book in user_a:

                to_json["users"][idx]["books_borrowed"].append(book)

        with open("library_manager/data.json", 'w') as file:
            json.dump(to_json, file, indent=4)
        
        self.load_data()
    # add a user to the library
    def add_user(self, name, ID,):
        user = User(name, ID)
        self.users.append(user)
    # remove a user by ID
    def remove_user(self, ID):

        for user in self.users:
            if user.ID == ID:
                for book in user.books_borrowed:
                    book.borrowed = False
                    self.borrowed_books.remove(book)
                self.users.remove(user)
                del user
                return 1
        return 0
    # add a book to the library
    def add_book(self, title, ID, author, ISBN, cate):
        book = Book(title, ID, author, ISBN, cate, False, None, None)
        self.books.append(book)
            
    # removes book by ID
    def remove_book(self, ID):

        for idx, book in enumerate(self.books):
            if book.ID == ID:
                if book in self.borrowed_books:
                    self.borrowed_books.remove(book)
                del self.books[idx]
                return 1
        return 0
    # searchs user by ID
    def search_User(self, ID):

        for user in self.users:
            if user.ID == ID:
                print("nome: " + user.name)
                print("ID: " + str(user.ID))
                print("livros alugados: ")
                for book in user.books_borrowed:
                    print("nome: " + book.title)
                    print("autor: " + book.author)
                    print()
                return user
        return 0
    # searchs the book by ID on the JSON file
    def search_book(self, ID):

        for book in self.books:
            if book.ID == ID:
                print("titulo: " + book.title)
                print("ID: " + book.ID)
                print("autor: " + book.author)
                print("ISBN: " + book.ISBN)
                print("categoria: " + book.category)
                if book.borrowed == True:
                    print("dono atual: " + book.owner)
                    print("data limite do aluguel: " + str(book.exp_date))
                else:
                    print("este livro ainda não foi alugado")
                
                return book
        return 0
    # prints all the users and their borrowed books
    def print_users(self):

        for user in self.users:
            print("nome: " + user.name + "   ID: " + str(user.ID))
            if len(user.books_borrowed) > 0:
                print()
                print("livros alugados: ")
                for book in user.books_borrowed:
                    print("nome: " + book.title)
                    print("autor: " + book.author)
                    print()
            else:
                print("este usuario não tem nenhum livro alugado no momento")
            print()
    # prints all the books and their owners
    def print_books(self):

        for book in self.books:
            print()
            print("titulo: " + book.title)
            print("ID: " + str(book.ID))
            print("autor: " + book.author)
            print("ISBN: " + str(book.ISBN))
            print("categoria: " + book.category)
            if book.borrowed == True:
                print("dono atual: " + str(book.owner_ID))
                print("data limite do aluguel: " + str(book.exp_date))
            else:
                print("este livro ainda não foi alugado")
            print()
    # prints all the borrowed books
    def print_borr_books(self):
                
        for book in self.borrowed_books:
            print()
            print("titulo: " + book.title)
            print("ID: " + str(book.ID))
            print("autor: " + book.author)
            print("ISBN: " + str(book.ISBN))
            print("categoria: " + book.category)
            print("dono atual: " + str(book.owner_ID))
            print("data limite do aluguel: " + str(book.exp_date))
            print()
    # redirects the book loaded to the user object
    def redirect_to_user(self, ID, book):

        user = None
        for user_to_find in self.users:

            if user_to_find.ID == ID:
                user = user_to_find
        
        user.books_borrowed.append(book)


library = Library()
