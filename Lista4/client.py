class Client(object):
    def __init__(self, name, age, address, phone, email):
        self.name = name
        self.age = age
        self.address = address
        self.phone = phone
        self.email = email
        self.past_orders = []
        
    def __str__(self):
        return "Name: " + self.name + " \nAge: " + str(self.age) + " \nAddress: " + self.address + " \nPhone: " + str(self.phone) + " \nEmail: " + self.email 
    
    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def get_address(self):
        return self.address
    
    def get_phone(self):
        return self.phone
    
    def get_email(self):
        return self.email
    
    def get_past_orders(self):
        if(self.past_orders == []):
            return print("Client has no past orders")
        for index,order in enumerate(self.past_orders): 
            print("Order " + str(index +1) + ":")
            print(order)
            print("----------------------------------------")
    
    def add_order(self, order):
        self.past_orders.append(order)
        
    def remove_order(self, order):
        if(order in self.past_orders):
            self.past_orders.remove(order)
        else:
            print("Order not found")    