# customer reward program 
class Customer:
    """Customer class to keep track"""
    def __init__(self, name='', purchases=0.0):
        """initializer"""
        self.name= name
        self.purchases = purchases
    
    #getter and setters of name and purchases
    @property
    def name(self):
        """return the name"""
        return self.__name
    @name.setter
    def name(self,name):
        """set the name"""
        self.__name= name
    
    @property
    def purchases(self):
        """return the purchases"""
        return self.__purchases
    @purchases.setter
    def purchases(self,purchases):
        """set the purcchases"""
        self.__purchases= purchases
    # method
    def calc_reward(self):
        """calculate the reward"""
        return 0.0
    def __str__(self):
        """return object in string"""
        return f'Name: {self.name}  Purchases: {self.purchases}  Total Reward: {self.calc_reward():.2f}'
         
    
class RetailCustomer(Customer):
    """Retail customer to keep track its reward"""
    def __init__(self, name='', purchases=0.0, email=''):       # super().__init__ to get previous information
        """initializer"""
        super().__init__(name,purchases)
        self.email = email
    
    #getter and setter
    @property
    def email(self):
        """return the email"""
        return self.__email
    @email.setter
    def email(self,email):
        """set the email"""
        self.__email= email
    
    # methods to calculate the reward
    def calc_reward(self):
        """calculate the reward"""
        # rule - purchases <= 100 : 1%, <= 300: 2%, >300: 2.5% 
        if self.purchases <= 100.0:
            return self.purchases * 0.01
        elif self.purchases <= 300.0:
            return self.purchases * 0.02
        elif self.purchases > 300.0:
            return self.purchases * 0.025
    def __str__(self):
        """return in object string"""
        return f'{super().__str__()}  Email: {self.email}' 
            
    
class CoporateCustomer(Customer):
    """Corporate customer to keep track its reward"""
    def __init__(self, name='', purchases=0, contact=''):                # super().__init__ to get previous information
        """initializer"""
        super().__init__(name, purchases)
        self.contact = contact
    # getter and setter
    @property
    def contact(self):
        """return the contact"""
        return self.__contact
    @contact.setter
    def contact(self,contact):
        """set the contact"""
        self.__contact = contact
    
    # methods to calculate the reward
    def calc_reward(self):
        """calculate the reward"""
        # rule - purchases <= 500 : 1%, <= 1000: 2%, >1000: 2.5% 
        if self.purchases <= 500.0:
            return self.purchases * 0.01
        elif self.purchases <= 1000.0:
            return self.purchases * 0.02
        elif self.purchases > 1000.0:
            return self.purchases * 0.025
    def __str__(self):
        """return in object string"""
        return f'{super().__str__()}  Contact: {self.contact}' 

# test classes
if __name__ =='__main__':

    # test code
    john_smith= RetailCustomer()
    john_smith.name = 'John Smith'
    john_smith.purchases = 150.0
    john_smith.email = 'johnnsmith@gmail.com'
    


    xyz= CoporateCustomer('XYZ Corp.', 1250.0,'Mary Jones') 
    customers = [john_smith,xyz]
    for customer in customers:
        print(customer)






    