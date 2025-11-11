from tkinter import *

class Calculator:
    """gui version of the calculator"""
    def __init__(self,window):
        self.window = window
        self.window.title('Mini Calculator')
        #widges
        Label(window, text = 'First Num').grid(row =0, column =0, padx =0, pady =5)
        self.entry_num1 = Entry(window, width= 10)
        self.entry_num1.grid(row=0, column=1, padx=10 , pady=5)
        
        Label(window, text='Second Num').grid(row=1, column=0, padx=10, pady=5)
        self.entry_num2 = Entry(window, width=10)
        self.entry_num2.grid(row=1, column=1, padx=10, pady=5)

        #button
        self.button_add = Button(window, text='Add',command=self.calculate_sum)
        self.button_add.grid(row=2, column=0, pady=10)
        
        self.button_multiply = Button(window, text='Multiply',command=self.calculate_product)
        self.button_multiply.grid(row=2, column=1, pady=10)



        # label to keep the result or error message
        self.label_result = Label(window, text = 'Result', font=('Arial',12))
        self.label_result.grid(row=3, column=0, columnspan=2, pady=10)
    # methods
    def calculate_sum(self):
        """calculate the sum of two numbers"""
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            result = num1 + num2 
            self.label_result.config(text=f'Result = {result}')    
        except ValueError:
            self.label_result.config(text='Invalid input:reenter the numbers')
    
    def calculate_product(self):
        """calculate the sum of two numbers"""
        try:
            num1 = float(self.entry_num1.get())
            num2 = float(self.entry_num2.get())
            result = num1 * num2 
            self.label_result.config(text=f'Result = {result}')    
        except ValueError:
            self.label_result.config(text='Invalid input:reenter the numbers')
# test class
root_window= Tk()
myapp = Calculator(root_window)
root_window.mainloop()