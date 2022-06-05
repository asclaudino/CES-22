from book import *
from client import *
from author import *

class Order:
    def __init__(self, client, book, date):
        self.client = client
        self.book = book
        self.date = date
        self.add_order(client,book)
    def __str__(self):
        return "Order: \nClient: " + str(self.client) + "\nBook: " + str(self.book) + "\nDate: " + str(self.date)
    
    def add_order(self, client, order):
        client.add_order(order)
        
    def remove_order(self, client, order):
        client.remove_order(order)    
    
    def get_book(self):
        return self.book
    
    def get_book_name(self):
        return self.book.title()    
    
    def get_client_name(self):
        return self.client.get_name()