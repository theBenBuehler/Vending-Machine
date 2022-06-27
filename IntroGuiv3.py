"""
Vending Machine Project IU 2022
Ben Buehler
Create a Virtual Vending Machine
 First -- Example for data structure https://stackoverflow.com/questions/52912856/python-vending-machine

Version 3 - make change no random
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
    buytitle1 = Label(vend, text="This is Where you buy stuff", pady=20).grid(row=3, column=1)
    backButton1=Button(vend,text="Go Back", padx = 200, pady=5, command=vend.destroy, fg="blue", bg="red")
    backButton1.grid(row=21, column=1, columnspan=3)
    
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
                itemBuy()
                return thing #maybe not necessary, but gets out of if statement
            else:
                outOfStock=Label(vend, text="I cannot VEND that to you 1.").grid(row=6, column=1)
  
    #If not in list
    outOfStock=Label(vend, text="I cannot VEND that to you.").grid(row=7, column=1)
  

#select which item to buy              
def itemBuy():
    global quantThis
    global eQuant
    
    eQuant = Entry(vend,width = 60, bg = "white", borderwidth = 3)
    eQuant.grid(row=8, column=1)
    eQuant.insert(0,"How many would you like to buy?")
    
    #click this button to show how many you want to buy
    quantThis=Button(vend,text="Buy Now", padx=10, pady=5, command=selectionQuant).grid(row=8, column=2)
    
  
    

#make sure they want less than the quantity on hand
def selectionQuant():
    
    global tooMany
    global eMoneyInput
    global changeResponse
    global errorMoreMoney
    global error
    global moneyInThis
    
    
    if int(eQuant.get()) > int(items.get(thing)[2]):
        tooMany=Label(vend, text="I don't have that many.").grid(row=9, column=1)
    elif 0 < int(eQuant.get()) <= int(items.get(thing)[2]):
        pass
    else:
        error = Label(vend, text="Please enter an appropriate number").grid(row=9,column=1)

    eMoneyInput = Entry(vend,width = 60, bg = "white", borderwidth = 3)
    eMoneyInput.grid(row=10, column=1)
    eMoneyInput.insert(0,"How much money are you inserting in dollars?")

    #click this button to enter how much money you input
    moneyInThis=Button(vend,text="Input Money", padx=10, pady=5, command=selectionMoney).grid(row=10, column=2)


#See if they added enough money
def selectionMoney():
    global change
    global moneyInput
    
    change = 0 #initialize
    
    moneyInput = float(eMoneyInput.get()) #to pass out of this function
    change = float(eMoneyInput.get()) - (float(items[thing][1])*int(eQuant.get()))

    if change >= 0:
        changeResponse = Label(vend, text="Please Remember your Change Below").grid(row=11, column =1)
        makeChange(moneyInput, change)
    else:
        errorMoreMoney = Label(vend, text="Please insert more money").grid(row=11, column = 1)

#calculate and report change
def makeChange(moneyInput, change):
    twenties = int(change // 20)
    change = change - 20*twenties
    changeLabel20=Label(vend, text="Twenty Dollar bills:", justify=RIGHT).grid(row=12, column=1, sticky='e')
    changeLabel20a = Label(vend, text=str(twenties)).grid(row=12,column=2)
    tens = int(change // 10)
    change = change - 10*tens
    changeLabel10=Label(vend, text="Ten Dollar bills:").grid(row=13, column=1, sticky='e')
    changeLabel10a = Label(vend, text=str(tens)).grid(row=13,column=2)
    fives = int(change // 5)
    change = change - 5*fives
    changeLabel5=Label(vend, text="Five Dollar bills:").grid(row=14, column=1, sticky='e')
    changeLabel5a = Label(vend, text=str(fives)).grid(row=14,column=2)
    dollars = int(change // 1)
    change = change - 1*dollars
    changeLabel1=Label(vend, text="One Dollar bills:").grid(row=15, column=1, sticky='e')
    changeLabel1a = Label(vend, text=str(dollars)).grid(row=15,column=2)
    quarters = int(change // .25)
    change = change - .25* quarters
    changeLabelQuarter=Label(vend, text="Quarters:").grid(row=16, column=1, sticky='e')
    changeLabelQuartera = Label(vend, text=str(quarters)).grid(row=16,column=2)
    dimes = int(change //.1)
    change = change - .1* dimes
    changeLabelDime=Label(vend, text="Dimes:").grid(row=17, column=1, sticky='e')
    changeLabelDimea = Label(vend, text=str(dimes)).grid(row=17,column=2)
    nickels = int(change // .05)
    change = change - 0.05* nickels
    changeLabelNickel=Label(vend, text="Nickels:").grid(row=18, column=1, sticky='e')
    changeLabelNickela = Label(vend, text=str(nickels)).grid(row=18,column=2)
    pennies = int(change // 0.009)
    changeLabelPenny=Label(vend, text="Pennies:").grid(row=19, column=1, sticky='e')
    changeLabelPennya = Label(vend, text=str(pennies)).grid(row=19,column=2)
    
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
