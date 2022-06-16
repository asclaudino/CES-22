import abc

### implementing the problema with the builder pattern ###


class CakeDirector(object):
    def __init__(self, cakeBuilder):
        self.cakeBuilder = cakeBuilder
    
    def makeCake(self):
        self.cakeBuilder.build()



class CakeBuilder(object):
    __metaclass__ = abc.ABCMeta
    
    @abc.abstractmethod    
    def build():
        """method should be implemented in subclasses"""
        
    @abc.abstractmethod    
    def build_name():
        """method should be implemented in subclasses"""

    @abc.abstractmethod
    def build_price():
        """method should be implemented in subclasses"""
        
    @abc.abstractmethod    
    def build_name():
        """method should be implemented in subclasses"""    
    
    @abc.abstractmethod
    def build_weight():
        """method should be implemented in subclasses"""	
    
    @abc.abstractmethod
    def build_ingredients():
        """method should be implemented in subclasses"""
    
    @abc.abstractmethod
    def build_topping():
        """method should be implemented in subclasses"""
        
    @abc.abstractmethod
    def build_style():
        """method should be implemented in subclasses"""               
        
        
class ChocolateCakeBuilder(CakeBuilder):
    def __init__(self):
        self.product = Cake()
    
    def build_name(self):
        self.product.set_name("Chocolate Cake") 
    
    def build_price(self):
        self.product.set_price(5)
    
    def build_weight(self):
        self.product.set_weight(100)
    
    def build_ingredients(self):
        self.product.set_ingredients(["egg","milk", "chocolate","wheat","water","sugar"])
        
    def build_topping(self):
        self.product.set_topping("Chocolate and Cream")
    
    def build_style(self):
        self.product.set_style("Wedding")
    
    def build(self):
        self.build_ingredients()
        self.build_name()
        self.build_price()
        self.build_weight()
        self.build_topping()
        self.build_style()
    
    def get_product(self):
        return self.product    
    
    
    
class Cake(object):
        def __init__(self):
            self.name = None
            self.price = None
            self.weight = None
            self.ingredients = None
            self.topping = None
            self.style = None
        
        def __str__(self) -> str:
            return  "I'm a {} cake with {}g of weight made with {},plus a delicious {} topping,  styled for a {}.".format(self.name, self.weight, self.ingredients, self.topping, self.style)    
        
        def set_name(self, name):
            self.name = name
            
        def set_price(self, price):
            self.price = price
        
        def set_weight(self, weight):
            self.weight = weight
        
        def set_ingredients(self, ingredients):
            self.ingredients = ingredients
        
        def set_topping(self, topping):
            self.topping = topping
        
        def set_style(self, style):
            self.style = style    




## example of using the builder pattern ##        

b = ChocolateCakeBuilder()
d = CakeDirector(b)
d.makeCake()
Bolo = b.get_product()
print(Bolo)