# operator overloading for numbers

class Number():
    """ Number class to demonstrate operator oberloading """

    def __init__(self, value):
        """initialzer"""
        self.value = value

    def __add__(self, other):
        """add two objects"""
        if isinstance(other,Number):
            return  Number(self.value + other.value)
        raise TypeError('Incompatible objects')


    def __gt__(self, other):
        """compare two objects to see whether one has a greater value"""
        if isinstance(other,Number):
            return(self.value > other.value)
        
    def __eq__(self, other):
        """compare whether two objects has the same value"""
        if isinstance(other,Number):
            return self.value == other.value
        
        
    
    def __str__(self):
        """display number object in string"""
        return f'{self.value}'
    
# test class
if __name__ == '__main__':
    try:
        pass
        # create number objects
        num1 = Number(100)
        num2 = Number(50)

       

        # add two number objects
        num3 = num1 + num2 
       

        # display results
        print(f'{num1} + {num2} = {num3}')
        

        # compare two number objects and display results
        # test for equality (==)
        print(f'{num1} equals to {num2} : {num1 == num2}')
        
        #test for greater than 
        print(f'{num1} is greater than {num2} : {num1 > num2}')


        # test for number object with non-number object
        print(num1 + 100)
       

    except TypeError as te:
        print(te)
    except Exception as ex:
        print(ex)
