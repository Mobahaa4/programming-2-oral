"""

Interface segreation : splites methods that are very large into smaller and more
specific ones and it is violated by writing a method that is not used in class 

"""
from abc import ABC, abstractmethod 

class Printer(ABC): 
    @abstractmethod 
    def print(self, document): 
        pass 
 
class Fax(ABC): 
    @abstractmethod 
    def fax(self, document): 
        pass 
 
class Scanner(ABC): 
    @abstractmethod 
    def scan(self, document): 
        pass 
 
class OldPrinter(Printer): 
    def print(self, document): 
        print(f"Printing {document} in black and white...") 
 
class NewPrinter(Printer, Fax, Scanner): 
    def print(self, document): 
        print(f"Printing {document} in color...") 
 
    def fax(self, document): 
        print(f"Faxing {document}...") 
 
    def scan(self, document): 
        print(f"Scanning {document}...") 
