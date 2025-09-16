# superclass and subclass demo
class Super:
    """super class"""
    def __init__(self,super_name):
        """initializer for super class"""
        self.super_name = super_name
        print('Super Class:',self.super_name)
# sub
class Sub(Super):
    """sub class"""
    def __init__(self, super_name,sub_name):
        """initializer"""
        super().__init__(super_name)
        self.sub_name = sub_name
        print('Sub Class',self.sub_name)
sub = Sub('I am super','I am sub')
print(sub)



class Employee:
    """Employee super class"""
    def __init__(self,name):
        self.name = name 
class Hourly_Paid(Employee):
    """Hourly paic sub class"""
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate 
    def pay(self):
        return self.hours * self.rate
john_smith = Hourly_Paid('John Smith',30,20.5)
print('John Smith made:' ,john_smith.pay(),'dollars this week.')
