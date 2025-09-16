# SalsaSales Class
class SalsaSales:
    """ SalsaSales class to keep track the store's salsa sales """
    # initializer
    def __init__(self, flavor='', jars_sold=0, unit_price=0.0):
        """initializer"""
        self.__flavor = flavor
        self.__jars_sold= jars_sold
        self.__unit_price = unit_price
    # getter/setter
    def get_flavor(self):
        """return the flavor"""
        return self.__flavor
    def set_flavor(self, flavor):
        """set the flavor"""
        self.__flavor = flavor
    def get_jars_sold(self):
        """return the  jars  sold"""
        return self.__jars_sold
    def set_jars_sold(self,jars_sold):
        """set the jars sold"""
        self.__jars_sold= jars_sold
    def get_unit_price(self):
        """return unit price"""
        return self.__unit_price
    def  set_unit_price(self, unit_price):
        """set unit price"""
        self.__unit_price= unit_price
    #methods
    def total_price(self):
        """calculate total price for total jars"""
        return self.__jars_sold* self.__unit_price
    def __str__(self):
        """display salsa object in string"""
        return f"{self.__flavor:10s}{self.__jars_sold:10d}{self.__unit_price:12.1f}{self.total_price():12.1f}"
# test class
if __name__== '__main__':
    mild = SalsaSales('Mild',10,3.5)
    medium = SalsaSales('Medium',20,4.5)
    hot = SalsaSales()
    salsaSales = [mild,medium,hot]
    for sales in salsaSales:
        print(sales)
