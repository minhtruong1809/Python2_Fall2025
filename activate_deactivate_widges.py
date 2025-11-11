import tkinter as tk

# methods 
def deactivate_widget():
    """deactivate widget"""
    label1.grid_remove()
def activate_widget():
    """activate widget"""
    label1.grid(row=0, column=0)

window = tk.Tk()
window.title('Testing deactivating/activating widget')
window.rowconfigure([0,1], minsize=100)
window.columnconfigure([0,1,2,3], minsize=100)


label1 = tk.Label(text='1000', bg='black',fg='red')
label2 = tk.Label(text='2000', bg='black',fg='blue')
label3 = tk.Label(text='3000', bg='black',fg='green')
label4 = tk.Label(text='4000', bg='black',fg='white')

label1.grid(row=0, column=0)
label2.grid(row=0, column=1, sticky='ew' )
label3.grid(row=0, column=2,sticky='ns')
label4.grid(row=0, column=3,sticky='ewns')

button1= tk.Button(window,text='Disable label 1', command=deactivate_widget)
button2= tk.Button(window,text=' Enable Label 1',command=activate_widget)
button1.grid(row=1, column=0, columnspan=2)
button2.grid(row=1, column=2,columnspan=2)

window.mainloop()



