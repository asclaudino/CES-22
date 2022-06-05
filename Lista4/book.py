
from library import *

class Book(object):
    
    def __init__(self,title,author,year,press, genre,edition,sellPrice,buyPrice):
        self.tilte = title
        self.author = author
        self.year = year
        self.press = press
        self.genre = genre
        self.edition = edition
        self.sellPrice = sellPrice
        self.buyPrice = buyPrice
        self.taxes = self.calc_taxes(self.sellPrice,self.buyPrice,self.genre)
        
    
    def __str__(self):
        return "Title: " + self.tilte + " \nAuthor: " + self.author + " \nBook Year:" + str(self.year) + " \nPress:" + self.press + " \nGenre:" + self.genre + " \nEd:" + str(self.edition) + " \nSellPrice:" + str(self.sellPrice) + " \nBuyPrice:" + str(self.buyPrice) + " \nTaxes:" + str(self.taxes)    
    
    def calc_taxes(self,sellPrice,buyPrice,genre):
        if genre == "Fiction":
            return 0.15 * (sellPrice - buyPrice)
        elif genre == "Non-Fiction":
            return 0.05 * (sellPrice - buyPrice)    
        else:
            return 0.10 * (sellPrice - buyPrice)
        
        
    def get_taxes(self):
        return self.taxes
    def get_title(self):
        return self.title
    def get_author(self):
        return self.author
    def get_year(self):
        return self.year
    def get_press(self):
        return self.press
    def get_genre(self):
        return self.genre
    def get_edition(self):
        return self.edition
    def get_sellPrice(self):
        return self.sellPrice
    def get_buyPrice(self):
        return self.buyPrice
    