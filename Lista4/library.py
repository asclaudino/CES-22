from library import *
from book import *
from client import *
from author import *



class Library(object):
    def __init__(self, clients, books,authors):
        self.clients = clients
        self.books = books
        self.authors = authors
    
    
    
    # Library Queries    
    def get_clients(self):
        if(self.clients == []):
            return print("Library has no clients")
        print("Clients:")
        print("----------------------------------------")
        for index,client in enumerate(self.clients):
            if(client != None):
                print("Client " + str(index +1) + ":")
                print("----------------------------------------")
                print(client)
                print("----------------------------------------")
    
    def get_books(self):
        if(self.books == []):
            return print("Library has no books")
        print("Books:")
        print("----------------------------------------")
        for index,book in enumerate(self.books):
            if(book != None):
                print("Book " + str(index +1) + ":")
                print("----------------------------------------")
                print(book)
                print("----------------------------------------")
    
    def get_authors(self):
        if(self.authors == []):
            return print("Library has no authors")
        print("Authors:")
        print("----------------------------------------")
        for index,author in enumerate(self.authors):
            if(author != None):
                print("Author " + str(index +1) + ":")
                print("----------------------------------------")
                print(author)
                print("----------------------------------------")
    
    ## CRUD Clients
    def add_client(self, client):
        self.clients.append(client)
        
    def find_client(self, client):
        if(client in self.clients):
            return print("---------------------------------------- \n" + str(self.clients[self.clients.index(client)]) + "\n----------------------------------------")
        return print("Client not found")
    
    def remove_client(self, client):
        if(client in self.clients):
            self.clients.remove(client)
        else:
            print("Client not found")
    
    
    ## CRUD Books
    def add_book(self, book):
        self.books.append(book)
    
    def remove_book(self, book):
        if(book in self.books):
            self.books.remove(book)
        else:
            print("Book not found")    
    
    def find_book(self, book):
        if(book in self.books):
            return print("---------------------------------------- \n" + str(self.books[self.books.index(book)]) + "\n----------------------------------------")
        return print("Book not found")    
    
    
    ## CRUD Authors    
    def add_author(self, author):
        self.authors.append(author)    
    
    def remove_author(self, author):
        if(author in self.authors):
            self.authors.remove(author)
        else:
            print("Author not found")
                
    def find_author(self, author):
        if(author in self.authors):
            return print("---------------------------------------- \n" + str(self.authors[self.authors.index(author)]) + "\n----------------------------------------")
        return print("Author not found")    
        



