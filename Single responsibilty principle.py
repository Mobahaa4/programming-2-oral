"""
Single responsibility principle : sould have one single responsibilty and one 
single purpose that lead to conculde and one reason to change

"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_info(self):
        return f"'{self.title}' by {self.author}"


class Bookprinter:
    
    def print_info(book):
        print(book.get_info())




book1 = Book("1990", "mohamed")
Bookprinter.print_info(book1)


        

    
