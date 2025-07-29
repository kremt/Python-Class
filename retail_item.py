#Creating a Retail_Item class module
class Retail_Item:
    #Initalize objects of this class with the following attributes:
    def __init__ (self):
        self.description = ""
        self.units = 1
        self.price = 0.00

    #Getters and Setters for each attribute
    def set_description(self, string):
        self.description = string
        
    def get_description(self):
        return self.description
        
    def set_units(self, units):
        self.units = units
        
    def get_units(self):
        return int(self.units)
        
    def set_price(self, price):
        self.price = price
        
    def get_price(self):
        return float(self.price)
