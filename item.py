# Create Item Class to keep track the inventory
class Item:
    """ Create Item Class to keep track the inventory """
    # initializer
    def __init__(self, name, qty, unit_price):
        """ initalizer/constructor """
        self.__name = name
        self.__qty = qty
        self.__unit_price = unit_price
    # getters/setters
    def get_name(self):
        """return item's name"""
        return self.__name
    def set_name(self,name):
        """set item's name"""
        self.__name = name

    def get_qty(self):
        """return item's qty"""
        return self.__qty
    def set_qty(self,qty):
        """set item's qty"""
        self.__qty = qty

    def get_unit_price(self):
        """return item's unit_price"""
        return self.__unit_price
    def set_unit_price(self,unit_price):
        """set item's unit_price"""
        self.__unit_price = unit_price

    # methods
    def total_price(self):
        """calculate total price"""
        return self.__qty * self.__unit_price
    def __str__(self):
        """display object in string"""
        return f"Item Name:{self.__name} Total Price:{self.total_price():.2f}"
    
    # test class
if __name__ == '__main__':
        item1 = Item('Pencil',10,1.50)
        print(item1)
        #print(item1.get_name())
        item3 = Item('Pen',20,3.00)
        print(item3)
        item10 = Item('Computer',1,1000)
        print(item10)


        
        item2 = Item()
        item2.set_name('Printer')
        item2.set_qty(10)
        item2.set_unit_price(65.0)
        items = [item1,item2]
        for item in items:
            print(item)
        

