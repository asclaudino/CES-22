from matplotlib.style import library
from library import *
from book import *
from client import *
from author import *
from orders import *

LivrariaSA = Library([],[],[])
Romeo = Book("Romeo e Julieta", "William Shakespeare", 1597, "Pinguin", "Fiction", 1, 20, 10)
Shakespeare = Author("William"," Shakespeare", "1564", "1616", [Romeo])
DomCasmurro = Book("Dom Casmurro", "Machado de Assis", 1876, "Pinguin", "Romance", 1, 20, 10)
Machado = Author("Machado de"," Assis", "1839", "1908", [DomCasmurro])
Ariel = Client("Ariel", "23", "Rua do Pinguin", "988888888", "fake@mail.com")
Joao = Client("Joao", "23", "Rua do Pinguin", "988888888", "fake@mail.com")



## Adding Queries
LivrariaSA.add_book(Romeo)
LivrariaSA.add_author(Shakespeare)
LivrariaSA.add_book(DomCasmurro)
LivrariaSA.add_author(Machado)
LivrariaSA.add_client(Ariel)

## Listing all Queries
# LivrariaSA.get_clients()
# LivrariaSA.get_books()
# LivrariaSA.get_authors()


## Finding Queries
# LivrariaSA.find_client(Ariel)
# LivrariaSA.find_client(Joao) 
# LivrariaSA.find_book(Romeo)
# LivrariaSA.find_author(Shakespeare)

## Removing Queries
# LivrariaSA.remove_client(Ariel)
# LivrariaSA.get_clients()
# LivrariaSA.remove_book(Romeo)
# LivrariaSA.get_books()
# LivrariaSA.remove_author(Shakespeare)
# LivrariaSA.get_authors()

## Order Queries
# Order1 = Order(Ariel, Romeo, "05/06/2022")
# Ariel.get_past_orders()
# Ariel.remove_order(Order1.get_book())
# Ariel.get_past_orders()


