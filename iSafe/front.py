#A program keeps track of physical money that hasn't been put in the bank.

from tkinter import *
import back

#Creating the window and assigning it to the object 'root'.
root = Tk()
root.title('iSafe by @dave.finesse')

#Imports the programs icon
root.iconbitmap(r'icons\growth_gGt_icon.ico')

#Assigns Account class from back.py to account object
account = back.Account('balance.txt')

#Creates button commands for view, withdrawel, deposit and confirm
def view_command():
    list.delete(END,0)
    bal = back.view()
    list.insert(END, bal)

def withdrawl_command():
    list.delete(END,0)
    account.balance = account.balance - int(withdrawl_text.get())
    list.insert(END, account.balance)

def deposit_command():
    list.delete(END, 0)
    account.balance = account.balance + int(deposit_text.get())
    list.insert(END, account.balance)

def confirm():
    with open('balance.txt', 'w') as file:
        file.write(str(account.balance))

#Creates and places widgets in the window
l1 = Label(root, text='iSafe', font = 'Comic 18 bold', fg='green')
l1.grid(row=0, column=0)

photo = PhotoImage(file='icons\growth.png')
l2 = Label(root, image=photo)
l2.grid(row=4, column=0, columnspan=2)

b1 = Button(root, text='Withdrawl', width = 12, command=withdrawl_command)
b1.grid(row = 1, column=0, pady=5)

b2 = Button(root, text='Deposit', width = 12, command=deposit_command)
b2.grid(row=2, column=0, pady=5)

withdrawl_text = StringVar()
e1 = Entry(root, width=12, textvariable=withdrawl_text)
e1.grid(row=1, column=1)

deposit_text = StringVar()
e2 = Entry(root, width=12, textvariable=deposit_text)
e2.grid(row=2, column=1)

list = Listbox(root)
list.grid(row=1, column=2, rowspan=4, padx=5, pady=5)

b3 = Button(root, text='Confirm', width=12, command=confirm)
b3.grid(row=3, column=0, columnspan=2)

b4 = Button(root, text='Check Balance', width=12, command=view_command)
b4.grid(row=5, column=2, pady= 5)


root.mainloop()
