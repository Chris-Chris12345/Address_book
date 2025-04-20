from tkinter import *
from tkinter.ttk import *

#functions
my_address_book = {}

#function to clear all the text boxes in the main screen
def clear_all():
    name_ent.delete(0,END)
    address_ent.delete(0,END)
    mobile_ent.delete(0,END)
    email_ent.delete(0,END)

def reset():
    clear_all()
    alist.delete(0,END)
    my_address_book.clear()


window = Tk()
window.title("Address Book")

title = Label(window,text="My Address Book",width=40)
title.grid(row=0,column=1,columnspan=2,padx=5,pady=15)

open_btn = Button(window,text="Open")
open_btn.grid(row=0,column=3,padx=5,pady=5)

alist = Listbox(window,width=30,height=32)
alist.grid(row=2,column=0,padx=5,pady=5,columnspan=3,rowspan=5)

name = Label(window,text="Name:")
name_ent = Entry(window)
name.grid(row=2,column=3,padx=5)
name_ent.grid(row=2,column=4,padx=5)

address = Label(window,text="Address:")
address_ent = Entry(window)
address.grid(row=3,column=3,padx=5)
address_ent.grid(row=3,column=4,padx=5)

mobile = Label(window,text="Mobile:")
mobile_ent = Entry(window)
mobile.grid(row=4,column=3,padx=5)
mobile_ent.grid(row=4,column=4,padx=5)

email = Label(window,text="Email:")
email_ent = Entry(window)
email.grid(row=5,column=3,padx=5)
email_ent.grid(row=5,column=4,padx=5)

save = Button(window,text="Save",width=40)
save.grid(row=8,column=1,padx=5,pady=5,columnspan=4)

window.mainloop()