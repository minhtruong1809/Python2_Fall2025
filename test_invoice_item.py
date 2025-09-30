from invoice import Invoice
from item import Item                       # from Filename.py import class Item

def main():
    """main function"""
    item1 = Item('Pencil',10,1.50)
    item2 = Item('Printer',10,65.0)

    invoice= Invoice('110')
    invoice.add_item(item1)
    invoice.add_item(item2)

    print(invoice)
    for item in invoice.items:
        print(item)



main()
        