class Smartphone:

    def __init__ (self, brand, model, number):
        self.brand = brand
        self.model = model
        self.number = number

    def __str__(self):
        return self.brand + " - " + self.model + ". " + self.number

    
        