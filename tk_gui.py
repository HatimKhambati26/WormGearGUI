from tkinter import *
from tkinter import messagebox

root = Tk()
name = StringVar(value='Enter Name Here')
cn = StringVar(value='Enter CN Here')
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, width=400, height=400, yscrollcommand=scrollbar.set)


# def random():
#     mlabel = Label(root, text="U CLicked Me").pack()
#     return
#

def random1():
    mtext = name.get()
    mno = cn.get()
    # mlabel2 = Label(root, text=mtext).pack()
    # mlabel3 = Label(root, text=mno).pack()
    mylist.insert(END, mtext)
    mylist.insert(END, mno)

#
# def mquit():
#     mexit = messagebox.askyesno(title="Quit", message="Quit The Test ?")
#     if mexit > 0:
#         root.destroy()
#         return


root.geometry('700x700+400+400')
root.title('Welcome To Quiz')

# mainmenu = Menu(root)
#
# root.configure(menu=mainmenu)
#
# submenu = Menu(mainmenu, tearoff=0)
# mainmenu.add_cascade(label="Options", menu=submenu)
# submenu.add_command(label="Restart", command=random)
# submenu.add_command(label="Close", command=mquit)

mentry = Entry(root, textvariable=name).pack()
mentry = Entry(root, textvariable=cn).pack()
mbutton = Button(root, text='Submit', command=random1, fg='red', bg='grey').pack()

mylist.pack(side=LEFT, fill=BOTH)
scrollbar.config(command=mylist.yview)
root.mainloop()
