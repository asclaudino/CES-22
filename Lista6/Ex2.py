import abc 

## implementing the problem using the decorator pattern


class BasePizza(object):

    def __init__(self):
        self.ingredients = ["trigo","farinha","ovos","queijo","azeitona"]
        
    def __str__(self):
        return "Pizza with: " + str(self.ingredients)
    
    def get_ingredients(self):
        return self.ingredients
    
    def print_ingredients(self):
        aux = ""
        for ingredient in self.ingredients:
            aux = aux + " " + ingredient
        return aux 
    
    def make_pizza(self):
        print("Just made a simple pizza with:" + self.print_ingredients())
        
        

class Marguerita(BasePizza):

    def __init__(self):
        super().__init__()
        
        
    def make_pizza(self):
        self.ingredients.append("marguerita")
        print("Just made a marguerita pizza with:" + self.print_ingredients())

    def print_ingredients(self):
        aux = ""
        for ingredient in self.ingredients:
            aux = aux + " " + ingredient
        return aux    
    
    

class Calabresa(BasePizza):

    def __init__(self):
        super().__init__()
        
        
    def make_pizza(self):
        self.ingredients.append("calabresa")
        print("Just made a calabresa pizza with:" + self.print_ingredients())

    def print_ingredients(self):
        aux = ""
        for ingredient in self.ingredients:
            aux = aux + " " + ingredient
        return aux    

## before decorator pattern    
SimplePizza = BasePizza()
SimplePizza.make_pizza()

## After decorator pattern
Mypizza = Marguerita()
Mypizza.make_pizza()

Mypizza1 = Calabresa()
Mypizza1.make_pizza()
