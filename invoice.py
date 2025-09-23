# invoice class
import datetime 
class Invoice:
    """Invoice class"""
    # init
    def __init__(self, inv_no):
        self.inv_no = inv_no
        self.inv_date = datetime.datetime.now()
        self.items = []

    # getter/ setter
    @property
    def inv_no(self):
        """return inv number"""
        return self.__inv_no
    
    @inv_no.setter
    def inv_no(self, inv_no):
        """set inv no"""
        self.__inv_no = inv_no
    
    #method
    def add_item(self,item):
        """add  item to the item list"""
        self.items.append(item)
    def remove_item(self, item):
        """delete item from item list"""
        self.items.remove(item)
    def calc_inv_total(self):
        """calculate the invoice total"""
        invoice_total = 0.0
        for item in self.items:
            invoice_total += item.total_price()
        return invoice_total
    def __str__(self):
        """display invoice object in the string"""
        dt_string = self.inv_date.strftime('%x')
        return f'Invoice no: {self.inv_no}  Date:{dt_string} Invoice total:{self.calc_inv_total():.2f}'
    
    

     

    
