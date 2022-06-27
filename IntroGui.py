"""
Vending Machine Project IU 2022
Ben Buehler
Create a Virtual Vending Machine
 First -- Example for data structure https://stackoverflow.com/questions/52912856/python-vending-machine
"""
from tkinter import *
import time

root = Tk()
root.title("Vending Machine")

def showMenu():
    menu = Toplevel()
    menu.title("This is what's in the machine")
    global title1
    global title2
    global title3
    
    #destroyButtons()
    title1 = Label(menu, text="ITEM").grid(row=3, column=1)
    title2 = Label(menu, text="COST").grid(row=3, column=2)
    title3 = Label(menu, text="QUANTITY").grid(row=3, column=3)
    
    counter = 1
    for thing in items:
        thing = Label(menu, text=items.get(thing)[0]).grid(row=counter+3, column=1)
        counter = counter + 1

    counter = 1
    for thing in items:
        thing = Label(menu, text=items.get(thing)[1]).grid(row=counter+3, column=2)
        counter = counter + 1

    counter = 1
    for thing in items:
        thing =Label(menu, text=items.get(thing)[2]).grid(row=counter+3, column=3)
        counter = counter + 1

    backButton=Button(menu,text="Back to Menu", padx = 180, pady=5, command=menu.destroy, fg="blue", bg="red")
    backButton.grid(row=counter+4, column=1, columnspan=3)


#try it as a dictionary -- list of (item, cost, quantity)
#These are my items
items={'item1':['chips','1.5','2'], 'item2':['chocolate','2','5'], 'item3':['headphones','15','1'], 'item4':['poptarts','2','2'], 'item5':['candy','1.75','2']}

    
def destroyButtons():
    menuButton.destroy()
    buyButton.destroy()
    quitButton.destroy()


def buyClick():#when button is clicked delete everything show menu
    global buyThis
    global vend
    vend = Toplevel()
    vend.title("This is where you buy stuff")
    buytitle1 = Label(vend, text="This is Where you buy stuff").grid(row=3, column=1)
    backButton1=Button(vend,text="Go Back", padx = 200, pady=5, command=vend.destroy, fg="blue", bg="red")
    backButton1.grid(row=8, column=1, columnspan=3)
    
    #e stands for entry widget so you can enter stuff text box
    global eBuy
    eBuy = Entry(vend,width = 60, bg = "white", borderwidth = 3)
    eBuy.grid(row=5, column=1)
    eBuy.insert(0,"What would you like to buy?")
    
    #click this button when you want to buy
    buyThis=Button(vend, text="Buy This", padx=10, pady=5,command=selection)
    buyThis.grid(row=5, column=2)

def selection():
    global select
    global thing #this will be used later
    select = eBuy.get()
    for thing in items:
        if select == items.get(thing)[0]:
            #check stock - if item is available
            if int(items.get(thing)[2]) > 0:
                yum = Label(vend, text="Yum. Vending Item").grid(row=6, column=1)
                return thing #dictionary key
            else:
                outOfStock=Label(vend, text="I'm sorry, I cannot VEND that to you. \nPlease come back when you're ready\n\n").grid(row=6, column=1)


#returns the KEY (not the item)
def itemSelect():
    #e stands for entry widget so you can enter stuff text box
    eBuy = Entry(vend,width = 20, bg = "white", borderwidth = 3)
    eBuy.grid(row=5, column=1)
    eBuy.insert(0,"What would you like to buy?")
    global thing #this will be used later
    while True:
        time.sleep(5)
        select = eBuy.get()
        for thing in items:
            if select == items.get(thing)[0]:
                #check stock - if item is available
                if int(items.get(thing)[2]) > 0:
                    return thing #dictionary key
                else:
                    outOfStock = Label(vend, text="I'm sorry, I cannot VEND that to you. \nPlease come back when you're ready\n\n").grid(row=6, column=1)

    
def quitClick():#when button is clicked delete everything show menu
    destroyButtons()
    secondScreen.destroy()
    goodbye = Label(root,text="Get your Goodies Elsewhere").grid(row=2, column=2)

def mainScreen():
    global menuButton 
    global buyButton
    global quitButton
    global backButton
    
    menuButton=Button(root,text="See Menu", padx = 30, pady=30, command=showMenu, fg="red", bg="blue")
    buyButton=Button(root,text="Buy Goodies", padx = 30, pady=30, command=buyClick, fg="black", bg="green")
    quitButton=Button(root,text="Quit", padx = 30, pady=30, command=quitClick, fg="blue", bg="red")
    
    
    firstText = Label(root,text="Hello, welcome to VENDSTAR").grid(row=0, column=2)
    secondText = Label(root,text="What would you like to do?").grid(row=1, column=2)
    menuButton.grid(row=3, column=1)
    buyButton.grid(row=3, column=2)
    quitButton.grid(row=3, column=3)

mainScreen()
root.mainloop()
