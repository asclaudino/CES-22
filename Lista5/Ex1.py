import abc


### implementing the problem the abtract factory pattern ###

class Cake(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
      pass
    
    @abc.abstractmethod
    def __str__(self) -> str:
        """method should be implemented by subclasses"""
        
    @classmethod
    def get_cake(self,name,style):
        if name == "chocolate":
            return ChocolateCake(name, 10, "1kg", ["egg","milk", "chocolate","wheat","water","sugar"],style)
        elif name == "vanilla":
            return VanillaCake(name, 10, "1kg", ["egg","milk", "vanilla","wheat","water","sugar"],style)
        elif name == "carrot":
            return CarrotCake(name, 10, "1kg", ["egg","milk", "carrot","wheat","water","sugar"],style)
        else: 
            return None
        
    @abc.abstractmethod    
    def get_cake_topping():
        """method should be implemented in subclasses"""

    @abc.abstractmethod
    def get_cake_style():
        """method should be implemented in subclasses"""
        
        
        
class ChocolateCake(Cake):
    def __init__(self, name, price, weight, ingredients,style):
        self.name = name
        self.price = price
        self.weight = weight
        self.ingredients = ingredients
        self.topping = self.get_cake_topping()
        self.style = self.get_cake_style(style)        
        
    
    def __str__(self) -> str:
        return  "I'm a {} cake with {}g of weight and {} ingredients with  {}  and  {}".format(self.name, self.weight, self.ingredients, self.topping, self.style)
    
    def get_cake_topping(self):
        return "Chocolate and Cream"

    def get_cake_style(self,style):
        return style   
    
    
class VanillaCake(Cake):
    def __init__(self, name, price, weight, ingredients,style):
        self.name = name
        self.price = price
        self.weight = weight
        self.ingredients = ingredients
        self.topping = self.get_cake_topping()
        self.style = self.get_cake_style(style)  
    
    def __str__(self) -> str:
        return  "I'm a {} cake with {}g of weight and {} ingredients with  {}  and  {}".format(self.name, self.weight, self.ingredients, self.topping, self.style)
    
    def get_cake_topping(self):
        return "Vanilla"

    def get_cake_style(self,style):
        return style
    
class CarrotCake(Cake):
    def __init__(self, name, price, weight, ingredients,style):
        self.name = name
        self.price = price
        self.weight = weight
        self.ingredients = ingredients
        self.topping = self.get_cake_topping()
        self.style = self.get_cake_style(style)      
        
    
    def __str__(self) -> str:
        return  "I'm a {} cake with {}g of weight and {} as ingredients with  {} topping and {} style".format(self.name, self.weight, self.ingredients, self.topping, self.style)
    
    def get_cake_topping(self):
        return "Carrot"

    def get_cake_style(self,style):
        return style     
    
    
    
    

## example of using the abstract factory pattern ##
Choco = Cake.get_cake("chocolate","wedding")
print(Choco)