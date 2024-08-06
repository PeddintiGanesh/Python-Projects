#@SuperMarketBillGeneration Project
#@Author: Ganesh

from datetime import datetime

name = input("Enter your name: ")

#List of Items 
lists= '''
Rice    Rs 50/kg
Wheat   Rs 40/kg
Milk    Rs 30/liter
Oil     Rs 70/liter
Sugar   Rs 40/kg
Salt    Rs 20/kg
Boost   Rs 100/each
Bread   Rs 20/each
Jam     Rs 10/each
'''

# Declaration

price = 0
pricelist=[]
totalprice = 0
Finalprice = 0
ilist=[]
qlist=[]
plist=[]

# rates for items
items = {'Rice':50,
         'Wheat':40,
         'Milk':30,
         'Oil':70,
         'Sugar':40,
         'Salt':20,
         'Boost':100,
         'Bread':20,
         'Jam':10}

option = input("For list of items Press 1: ")
if option == '1':
    print(lists)
else :
    print("Invalid Option")
    
for i in range(len(items)):
    input1 = int(input("Press '1' for list of items \nPress '2' for exit: "))
    if input1 == 2:
        break
    if input1 == 1:
        item = input("Enter your items: ")
        quantity = int(input("Enter the quantity: "))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice = totalprice + price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            GST= (totalprice*5)/100
            Finalprice = totalprice + GST
        else :
            print("Sorry..! The item that you have entered is not available")
    else:
        print("Please choose correct number")
    input3 = input("Can i proceesd to the bill the items 'Yes' or 'No': ")
    if input3 == 'Yes':
        pass
        if Finalprice!=0:
            print(28*"=","Amma Supermarket",28*"=")
            print(31*" ","Wanaparthy")
            print("Name: ",name,28*" ","Date:",datetime.now())
            print(75*"-")

            for i in range(len(pricelist)):
                print("SNo: ",i+1,"Item: ",ilist[i],"\tQuantity: ",qlist[i],"\tPrice: ",plist[i])
            print(75*"-")
            print(50*" ",'TotalPrice :','Rs',totalprice)
            print(50*" ","GST Amount :",'Rs',GST)
            print(50*" ",'FinalAmount:','Rs',Finalprice)
            print(75*"-")   
            print(28*" ","Thanks For Visiting..")
            print(75*"-") 



