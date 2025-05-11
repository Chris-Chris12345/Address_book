from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

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

def update():
    key = name_ent.get()
    if key == "":
        messagebox.showinfo("Error","Name cannot be empty")
    else:
        if key not in my_address_book.keys():
            alist.insert(END,key)
        my_address_book[key] = (address_ent.get(),mobile_ent.get(),email_ent.get())
        clear_all()

def edit():
    clear_all()
    index = alist.curselection()
    if index:
        name_ent.insert(0,alist.get(index))
        details = my_address_book[name_ent.get()]
        address_ent.insert(0,details[0])
        mobile_ent.insert(0,details[1])
        email_ent.insert(0,details[2])
    else:
        messagebox.showinfo("Error","Select a name")

def delete():
    index = alist.curselection()
    if index:
        del my_address_book[alist.get(index)]
        alist.delete(index)
        clear_all()
    else:
        messagebox.showinfo("Error","Select a name")

def display(event):
    newWin = Toplevel(window)
    index = alist.curselection()
    contact = ""
    if index:
        key = alist.get(index)
        contact = "NAME  :  "+ key + "\n\n"
        details = my_address_book[key]
        contact += "ADDRESS  :  "+ details[0] + "\n"
        contact += "MOBILE  :  "+ details[1] + "\n"
        contact += "EMAIL  :  "+ details[2] + "\n"
    label = Label(newWin)
    label.grid(row=0,column=0)
    label.config(text=contact)

def save():
    fout = asksaveasfile(defaultextension = ".txt")
    if fout:
        print(my_address_book,file= fout)
        reset()
    else:
        messagebox.showwarning("Warning","Address Book not saved")

def open():
    global  my_address_book
    reset()
    fin = askopenfile(title="Open File")
    if fin:
        my_address_book = eval(fin.read())
        for key in my_address_book.keys():
            alist.insert(END, key)
        title.configure(text=os.path.basename(fin.name))
    else:
        messagebox.showwarning("Warning","No file was opened")


window = Tk()
window.title("Address Book")

title = Label(window,text="My Address Book:",width=35)
title.grid(row=0,column=1,columnspan=2,padx=5,pady=15)

open_btn = Button(window,text="Open",width=40,command=open)
open_btn.grid(row=0,column=3,padx=5,pady=5)

alist = Listbox(window,width=30,height=32)
alist.grid(row=2,column=0,padx=5,pady=5,columnspan=3,rowspan=5)
alist.bind('<<ListboxSelect>>', display)

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

save_btn = Button(window,text="Save",width=40,command=save)
save_btn.grid(row=8,column=1,padx=5,pady=5,columnspan=4)

edit_btn = Button(window,text="Edit",width=20,command=edit)
edit_btn.grid(row=7,column=0,padx=5,pady=5,columnspan=4)

delete_btn = Button(window,text="Delete",width=20,command=delete)
delete_btn.grid(row=7,column=2,padx=5,pady=5,columnspan=4)

add = Button(window,text="Update/Add",width=20,command=update)
add.grid(row=7,column=4,padx=5,pady=5,columnspan=4)

window.mainloop()
