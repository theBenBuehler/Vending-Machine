"""
Vending Machine Project IU 2022
Ben Buehler
Create a Virtual Vending Machine
 First -- Example for data structure https://stackoverflow.com/questions/52912856/python-vending-machine
"""
"""
-----------------------
old way of ordering data
#make a dictionary for each item in the machine
a = {'item': 'chips', 'price': 1.5, 'stock': 2}
b = {'item': 'chocolate', 'price': 2, 'stock': 5}
c = {'item': 'headphones', 'price': 15, 'stock': 1}
d = {'item': 'popTarts', 'price': 2, 'stock': 2}
e = {'item': 'candy', 'price': 1.75, 'stock': 2}

#this list is everything in the vending machine a list of dictionaries
itemsList=[a,b,c,d,e]
----------------------

#how to reference individual items
#this will get the item
print("the item is", items.get("item1")[0], ".")
#this will get the cost of item 1
print("the cost is", items.get("item1")[1], "dollars")
#this will get the quantity
print("we have", items.get("item1")[2],",", itemsDict.get("item1")[0], "in stock")

#updates Quantity
print(items)
newQuant5 = int(items["item5"][2]) - 1
items["item5"][2] = newQuant5
print(items)
"""
#try it as a dictionary -- list of (item, cost, quantity)
#These are my items
items={'item1':['chips','1.5','2'], 'item2':['chocolate','2','5'], 'item3':['headphones','15','1'], 'item4':['poptarts','2','2'], 'item5':['candy','1.75','2']}

#Function that prints what's in the machine
def showMenu():
    layout = "{0:<12}{1:^10}{2:>4}" #set tabs
    print(layout.format("item","cost $$","Quant"))
    for thing in items:
        print(layout.format(items.get(thing)[0],items.get(thing)[1],items.get(thing)[2]))


#keeps asking for an item returns item if in machine and in stock
#returns the KEY (not the item)
def itemSelect():
    global thing #this will be used later
    while True:
        select = input("\nHello! Welcome to VENDSTAR!\nWhich item would you like to buy? ")
        for thing in items:
            if select == items.get(thing)[0]:
                #check stock - if item is available
                if int(items.get(thing)[2]) > 0:
                    return thing #dictionary key
                else:
                    print("Sorry, out of stock!\nPlease select a new item.")
        else:
            print("I'm sorry, I cannot VEND that to you. \nPlease come back when you're ready\n\n")

def itemBuy():
    while True:
        change = 0 #initialize
        
        #make sure they want less than the quantity on hand
        while True:
            quantInput = int(input("\nI have " + items.get(thing)[2] + " " +items.get(thing)[0] + " in stock\n How many would you like? "))
            if quantInput > int(items.get(thing)[2]):
                print("That is simply impossible, please select an appropriate amount.\n")
            elif 0 < quantInput <= int(items.get(thing)[2]):
                break
            else:
                print("Please select an appropriate number for how many you would like.")
                
        moneyInput = float(input("\nHow much money are you inserting?"))
        change = moneyInput - ((float(items[thing][1])*quantInput))

        if change > 0:
            print("Enjoy the " + items.get(thing)[0])
            makeChange(moneyInput, change)
            break
        else:
            print("sorry, that is not enough money")
            again = input("Do you have more money to add?\nSelect Y or N")
            if again == "N":
                break
            
def makeChange(moneyInput, change):
    twenties = int(change // 20)
    change = change - 20*twenties
    tens = int(change // 10)
    change = change - 10*tens
    fives = int(change // 5)
    change = change - 5*fives
    dollars = int(change // 1)
    change = change - 1*dollars
    quarters = int(change // .25)
    change = change - .25* quarters
    dimes = int(change //.1)
    change = change - .1* dimes
    nickels = int(change // .05)
    change = change - 0.05* nickels
    pennies = int(change // 0.009)
    
    #make a list for printing reasons
    #it feels like this should be a dictionary
    changeList=[twenties, tens, fives, dollars, quarters, dimes, nickels,pennies]
    changeNames=["$20 bills","$10 bills","$5 bills","$1 bills","quarters","dimes","nickels","pennies"]
    print("\nI will now VEND your change.\nYour Change is...\n")
    for i in range(8):
        if changeList[i] > 0:
            print(str(changeList[i]) + " " + changeNames[i])
    #I did this when I wanted each demoniation to be represented
    #print("Your change is:\n{0} $20 bills\n{1} $10 bills\n{2} $5 bills\n{3} $1 bills\n{4} quarters\n{5} dimes\n{6} nickels\n{7} pennies".format(twenties, tens, fives, dollars, quarters, dimes, nickels, pennies))

showMenu()
itemSelect()
itemBuy()
