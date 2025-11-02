import time

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        
    def get_details(self):
        return (f'title: {self.title}, author: {self.author}, isbn: {self.isbn}, '
                f'status: {"available" if self.available == True else "not available"}')
        
class User:
    def __init__(self, id: str, name):
        self.user_id = id
        self.name =  name
        self.borrowed_books = []

    def borrow_book(self, book: Book):
        self.borrowed_books.append(book)
        
    def return_book(self, book: Book):
        self.borrowed_books.remove(book)
        
class Library:
    def __init__(self, max_borrow_days: int = 14):
        self.max_borrow_days = max_borrow_days
        self.books:dict[str, Book] = {}
        self.users: dict[str, User] = {}

    def register_user(self, user: User) -> None:
        self.users[user.user_id] = user
        
    def add_book(self, book: Book) -> None:
        self.books[book.isbn] = book
    
    def __str__(self):
        return f'books: {self.books}, member: {self.users}'
    
    def perform_borrow(self, user_id: str, isbn: str) -> None:
        if user_id in self.users and isbn in self.books:
            if self.books[isbn].available:
                self.users[user_id].borrow_book(self.books[isbn])
                self.books[isbn].available = False
                Logger.log_action("BORROW", user_id, isbn)
                SystemAdmin.update_transactions_count()

            else:
                raise ValueError('book is not available')
        else:
            raise KeyError('no such member or book') 
        
    def perform_return(self, user_id: str, isbn: str) -> None:
        if user_id in self.users and isbn in self.books:
            if not self.books[isbn].available:
                self.users[user_id].return_book(self.books[isbn])
                self.books[isbn].available = True
                Logger.log_action("RETURN", user_id, isbn)
                SystemAdmin.update_transactions_count()

            else:
                raise ValueError('book is available')
        else:
            raise KeyError('no such member or book') 
        
class Logger:
    @staticmethod
    def log_action(action_type: str, user_id: str, isbn: str) -> None:
        curr = time.time()
        curr = time.ctime(curr)
        print(f'{action_type}, user_id: {user_id}, isbn: {isbn}, {curr}')
        
class SystemAdmin:
    total_transactions = 0
    
    @classmethod
    def update_transactions_count(cls, amount: int = 1) -> None:
        cls.total_transactions += amount
        
    @classmethod
    def report_stats(cls) -> None:
        print(f'total transactions: {cls.total_transactions}')

                
    
b1 = Book('voina i mir', 'tolstoi', '1234')

u1 = User('3427', 'gad')

lib = Library()

lib.register_user(u1)

lib.add_book(b1)

lib.perform_borrow(u1.user_id, b1.isbn)
lib.perform_return(u1.user_id, b1.isbn)