from tkinter import *
from tkinter import messagebox

window = Tk()
'''''
#####################################################################################
##1.  Label and Entry

window.geometry("400x200")
window.title("Label and Entry Widgets")

user_var = StringVar()
pwd_var = StringVar()
def check_empty():
    if user_var.get()=="":
        print("User name is empty.")
def check_pwd():
    if len(pwd_var.get()) < 8:
        print("password must be at least 8 characters.")
    elif pwd_var.get().isalpha():
        print("password must contain digit.")
    elif pwd_var.get().isalnum():
        print("password must contain puntuation.")
    else:
        print("Password is valid.")
#widgets
label_user=Label(window,text="User Name:",font="Calibri 16 bold")
label_user.place(x=30,y=50)
label_password = Label(window, text="Password:",font="Calibri 16 italic bold")
label_password.place(x=30, y=90)

entry_user=Entry(window, width = 20, font="Calibri 16 bold",textvariable=user_var)
entry_user.place(x=150, y=50)
entry_user.bind("<FocusOut>", lambda e: check_empty())
entry_password = Entry(window, show="*", width=20, font="Calibri 16 bold", textvariable = pwd_var)
entry_password.place(x=150,y=90)

btn_login=Button(window,text="Verify",font="Calibri 16 bold",command=check_pwd)
btn_login.place(x=150,y=130)
#####################################################################################


##2. button widget
window.geometry("300x150")
window.title("Button Widget")

def btn_clicked():
    print(btn_top["text"],"button clicked..")
# widget
btn_west = Button(window,text="Red",fg="red")
btn_east = Button(window,text="Blue",highlightbackground="blue")
btn_top = Button(window, text="Green",command=btn_clicked,fg="green")
btn_bottom = Button(window,text="Yellow",highlightbackground="Yellow")

btn_west.pack(side=LEFT)
btn_east.pack(side=RIGHT)
btn_top.pack(side=TOP)
btn_bottom.pack(side=BOTTOM)

################################################################################

##3. check button widget
window.geometry("300x300")
window.title("Checkbutton widget")

frm_base = LabelFrame(window,text="Select course mode:",fg="red")
frm_base.pack()

ckbtn1 = IntVar()
ckbtn2 = IntVar()
ckbtn3 = IntVar()

ckbtn1.set(1)
def ckbtn_clicked():
    print("Oncampus value:",ckbtn1.get())
    print("Online Anytime value:",ckbtn2.get())
    print("Online On a Schedule:",ckbtn3.get())
    print()
Checkbutton(frm_base, text="Online Anytime",
            variable = ckbtn1,
            onvalue = 1,
            offvalue = 0,width = 20,anchor='w',command=ckbtn_clicked).pack()
Checkbutton(frm_base, text="On Campus",
            variable = ckbtn2,
            onvalue = 1,
            offvalue = 0,width = 20,anchor='w',command=ckbtn_clicked).pack()
Checkbutton(frm_base, text="Online On a Schedule",
            variable = ckbtn3,
            onvalue = 1,
            offvalue = 0, width=20,anchor='w',command=ckbtn_clicked).pack()


################################################################################

##4. Radiobutton widget
window.geometry("200x200")
window.title("Radiobutton Widget")
frm_base = LabelFrame(window, text="Select an option",fg="red")
frm_base.pack()

rb_var = StringVar(frm_base,1)
print(rb_var.get())

def option_clicked():
    print("Option",rb_var.get(),"has been selected.")

options = {"Option 1":1,
           "Option 2":2,
           "Option 3":3,
           "Option 4":4}
for (opt,val) in options.items():
    Radiobutton(frm_base,text=opt,variable=rb_var,
                value=val,command=option_clicked).pack()

############################################################################

##5.  Menu Widget
window.title("Menu Widget")
def process_save():
    print("Save menu item is selected.")
menu_bar = Menu(window)
window.config(menu=menu_bar)
file_menu=Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Save",command=process_save)

exit_menu=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="Exit",menu=exit_menu)
exit_menu.add_command(label="Quit",command=window.destroy)
 
#################################################################################

##6. frame with widget
window.title("Frame with Widgets")
window.geometry('500x250')

frame1 = Frame(window)

frame1.pack()
frame_bottom = Frame(window)
frame_bottom.pack(side=BOTTOM)

btn1 = Button(frame1,text="Button1",fg="red")
btn1.pack(side=RIGHT)
btn2 = Button(frame1,text="Button2",fg="red")
btn2.pack()

btn3=Button(frame_bottom,text="Button3",fg="green")
btn3.pack(side=BOTTOM)
btn4=Button(frame_bottom,text="Button4",fg="green")
btn4.pack()

#################################################################################

##6. Canvas
window.title("Canvas widget")
window.geometry("350x350")

cnv = Canvas(window, bg="black",height="300",width="300")

cnv.create_oval(10, 10, 80, 80, 
                            outline = "black", fill = "white",
                            width = 2)
cnv.create_oval(110, 10, 210, 80,
                            outline = "red", fill = "green",
                            width = 2)
cnv.create_rectangle(230, 10, 290, 80,
                                outline = "black", fill = "blue",
                                width = 2) 
cnv.create_arc(30, 200, 90, 100, start=0, extent=180, outline = "green",
                          fill = "red", width = 2)
cnv.pack()

################################################################################

##7. Canvas
window.title("list widget")
window.geometry("400x400")      
frame = Frame(window)
frame.pack()
scrb = Scrollbar(frame)


frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)

lst = Listbox(frame, font='Verdana, 12 bold',yscrollcommand = scrb.set)
scrb.config(command=lst.yview)

lst.grid(row=0, column=0, sticky='NSEW')
scrb.grid(row=0, column=1, sticky='NS')


for i in range(30):
    lst.insert(END, ' Item'+str(i))


################################################################################

## 8. Canvas
canvas_width =500
canvas_height = 150

window.title('Painting using Ovals')


def paint(event):
    x1,y1 = event.x-1,event.y-1
    x2,y2 = event.x+1,event.y+1
    c.create_oval(x1,y1,x2,y2, fill='green',width=3)

def clear_clicked():
    c.delete('all')
c = Canvas(window,
           width = canvas_width,
           height = canvas_height)
c.pack(expand=YES, fill=BOTH)
c.bind("<B1-Motion>", paint)
label = Label(window, text='Press and Drag the mouse to draw')
label.pack()
button = Button(window, text='Clear', command = clear_clicked)
button.pack()
################################################################################
'''''

##9. grid
for r in range(5):
    for c in range(3):
        lbl = Label(window, relief =SUNKEN, width=10, text=f'R{r} C{c}')
        lbl.grid(row=r,column=c,padx=5,pady=5)

################################################################################

window.mainloop()    
