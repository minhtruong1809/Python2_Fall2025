import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox

class TodoApp:
    def __init__(self, root):
        """initializer for todo app"""
        self.root = root
        self.root.title('To-Do List')
        self.root.geometry('400x400')

       

        # --- 1. Data Management ---
        # A Python list to store our tasks internally
        self.tasks = []

        #frame for input widgets
        self.frame_input = ttk.Frame(root, padding='10 10 10 10')
        self.frame_input.pack(side= tk.TOP,fill=tk.X)

        # Fram for the listbox and buttons (middle/bottom part)
        self.frame_list = ttk.Frame(root, padding='10 10 10 10')
        self.frame_list.pack(side=tk.TOP, fill= tk.BOTH, expand = True)

        # Input Widgets
        self.entry_task = ttk.Entry(self.frame_input, width=30)
        self.entry_task.grid(row=0,column=0,pady=5)
        self.entry_task.bind('<Return>',lambda e:self.add_task())

        self.button_add = ttk.Button(self.frame_input, text='Add Task', command=self.add_task)
        self.button_add.grid(row=0, column=1, pady=5)

        #list box and scollbox
        self.scrollbar = ttk.Scrollbar(self.frame_list,orient=tk.VERTICAL)
        self.listbox_tasks = tk.Listbox(
            self.frame_list,
            yscrollcommand=self.scrollbar.set,
            selectmode = tk.EXTENDED,
            height= 15 

        )
        self.scrollbar.config(command=self.listbox_tasks.yview)
        # place the widgets in the list frame
        self.listbox_tasks.grid(row=0, column=0, sticky=tk.NSEW)
        self.scrollbar.grid(row=0, column=1, sticky=tk.NS)

        # configure the list frame
        self.frame_list.columnconfigure(0, weight=1)
        self.frame_list.rowconfigure(0, weight=1)

        # delete button
        self.button_delete = ttk.Button(root, text='Delete selected task',command=self.delete_task)
        self.button_delete.pack(side=tk.BOTTOM, pady = 10)


    def add_task(self):
        """Gets text from entry, adds to list, and updates the Listbox."""
        task_text = self.entry_task.get().strip()

        if task_text:
            self.tasks.append(task_text)
            self.listbox_tasks.insert(tk.END, task_text)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning('Warning', 'Please enter a task.')

        
    def delete_task(self):
        """Removes the selected task from the list and the Listbox."""
        
        selected_indices = self.listbox_tasks.curselection()
        if not selected_indices:
            messagebox.showwarning('Warning', 'Please select one or more tasks to delete.')
            return
        for index in selected_indices[::-1]:
            self.listbox_tasks.delete(index)
            
        messagebox.showinfo('Done','All selected items are deleted')     
       
    

# --- 7. Main execution loop ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
