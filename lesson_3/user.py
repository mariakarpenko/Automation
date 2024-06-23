class User:
    def __init__ (self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def sayFirstName (self):
        print("My first name is", self.first_name)

    def sayLastName (self):
        print("My last name is", self.last_name)

    def sayFullName (self):
        print("My full name is", self.first_name, self.last_name )