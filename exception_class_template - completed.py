# Work on exception class to handle customized exceptions

class BankAccount:
    """ Bank Account class to keep track banking activities """

    def __init__(self, name, balance=0):
        """ Initialize the account holder's name and starting balance """
        self.set_name(name)
        self.set_balance(balance)
    # getters and setters   
    def get_name(self):
        """ Return the account holder's name """
        return self.__name
    def set_name(self,name):
        """ Set the account holder's name """
        self.__name = name
    def get_balance(self):
        """ Return the current balance """
        return self.__balance
    def set_balance(self,balance):
        """ Set the current balance """
        self.__balance = balance
    
    # methods
    def deposit(self, amount):
        """ Deposit money into the account """
        if amount <=0.0:
            raise NegativeException('Deposit cannot be negative or zero')
        self.__balance += amount   
    def withdraw(self, amount):   
        """ Withdraw money from the account """
        if amount <= 0.0:
            raise NegativeException('Withdrawal amount cannot be negative or zero')
        elif amount > self.__balance:
            raise NegativeException('Insufficient Fund.')   
        else:
            self.__balance -= amount       
    def __str__(self):
        """ Return a string representation of the account """
        return f'Account holder: {self.__name}, Balance: ${self.__balance:.2f}'

# exception class
class NegativeException(Exception):
    """ Custom exception for negative values """
    def __init__(self, message):
        """ initializer """
        super().__init__(message)
def main():
    try: 
        # create a bank account
        jsmith_account = BankAccount("John Smith", 100.0)
        print(jsmith_account)

        # deposit money
        jsmith_account.deposit(50.0)
        print("After depositing $50:", jsmith_account)

        # withdraw money
        jsmith_account.withdraw(30.0)
        print("After withdrawing $30:", jsmith_account)

        # attempt to withdraw more than the balance
        jsmith_account.withdraw(150.0)

    except NegativeException as ne:
        print(ne)
    except Exception as ex:
        print("An unexpected error occurred:", ex)  
    # no error
    else:
        print('There is no error')
    finally:
        print('Wrap up the code')

main()
    