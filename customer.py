import os
import auth
from commonFunctions import updateProfile

menuFile = "menu.txt"
orderFile = "order.txt"
feedBackFile = "feedback.txt"
userFile = 'users.txt'
uData=[]

def customer_menu(userData):
    global uData
    print(f"Welcome to customer page, {userData['userName']}")
    orders=[] 
    uData = userData

    while True:
        
        print("\nCustomer Panel")
        print("\t1. View Menu and Order")
        print("\t2. View Order Status")
        print("\t3. Give Feedback")
        print("\t4. Update Profile")
        print("\t5. Logout")

        action = input("\nChoose an action: ")

        if action == "1":
            viewMenu(orders)

        elif action == "2":
            viewOrderStatus()

        elif action == "3":
            giveFeedback(userData)

        elif action == "4":
            updateProfile(userData)

        elif action == "5":
            print("Logging out...")
            break
        else:
            print("Error! Please enter again")

def viewMenu(orders):

    print("\nMenu")
    menu = [] # will contain the whole menu after fetching from the file
    

    with open(menuFile,"r") as file:

        idCount = 1
        for line in file:
            item,price = line.strip().split(",")
            # menu[item] = int(price) # adding the menu with, price converted to int in the menu dictionary
            menu.append({
                        'id':idCount,
                         'item':item,
                         'price':int(price)
                         })
            idCount +=1

    count = 1

    for foods in menu:
        
        print(f"\t{count}. {foods['item']} Rs{foods['price']}")
        print("---------------------------------\n")
        count+=1
    
        
    placeOrder(menu,orders)


def placeOrder(menu,orders):

    
    totalPrice=0

    while True:

        itemId = int(input("\nEnter the food id to order (type 0 to finish): ").strip())
        

        if itemId == 0:
            break

        itemCount = int(input("Quantity of {itemName}: "))
        print("\n")

        if itemId > len(menu)+1:
            print("Please enter correct id")
            continue


        
        for food in menu:

            if food['id']==itemId:

                orders.append({
                                'id':food['id'],
                                'item':food['item'],
                                'price':food['price'],
                                'count':itemCount

                            })
               
                
            
    
    for items in orders:
        totalPrice += items['price']*items["count"]  #updating the total order price
    
    if totalPrice > 0:

        print(f"\nYour Order Have been Placed.\n\tTotal Order Price: {totalPrice}")

        action = input("\nEnter C : check/add/edit order , P : Confirm and Pay :> ").lower()


        if action == "c":
            viewOrder(orders)
        if action == "p":
            confirmOrder(orders,totalPrice)

    else:
        print("\nThankyou for visiting..")
        

        

def viewOrder(orders):
    totalPrice = 0

    print("\nYour Orders\n")

    for order in orders:
        print(f"\tItem-Id:{order['id']} || Name: {order['item']} || Price: {order['price']} || Quantity: {order['count']} ")
        print("================================================================================\n")

        totalPrice += order['price']*order["count"]
    
    print(f"Total Price:{totalPrice}")   

    action = input("\nEnter C to confirm / A to add / d to delete order:  ").lower()

    if action == "a":
        #will allow customer to add to their existing order
        viewMenu(orders)

    elif action == "c":
        #let customer confirm the order
        confirmOrder(orders,totalPrice)

    elif action == "d":
        deleteOrder(orders)
        

def deleteOrder(orders):

    itemId = int(input("\nEnter the ID of the item you want to delete: ").strip())

    found = False #To check if the Item ID exists

    for order in orders:
        if order['id'] == itemId:

            #Removes Item
            orders.remove(order) 

            found = True

            print(f"Item with ID {itemId} has been removed.")

            break

    if not found:
        print(f"No item found with ID {itemId}. Please enter a valid ID.")

    viewOrder(orders)




def confirmOrder(orders,totalPrice):
    

    print(f"Your Order Has Been Successfully Placed")

    print(f"\n\tItems\tPrice")

    for order in orders:
        print(f"\t{order['item']}\t{order['price']}")


    with open(orderFile,'a') as file:
        for order in orders:
            file.write(f"{uData['userName']},{order['item']},{order['price']},{order['count']},In Progress\n")


    print(f"\n\tTotal Amount:\t{totalPrice} ")


    i = input("\nPress Enter to go back to Customer Menu ")


#change this

def viewOrderStatus():
   
    with open(orderFile,'r') as file:
        print("\nYour Orders\n")
        for line in file:
            userName,itemName,price,quantity,status=line.strip().split(",")
            
            if userName == uData['userName']:
                print(f"\tname: {itemName}\n\tprice: {price}\n\tquantity: {quantity}\n\tStatus: {status}")
                print("=================================================\n")
    
    input("\nPress Enter to Return to Panel\n")
            


            
            
def giveFeedback(userData):
    #this function will handle adding feedback to the txt file

    print("\nPlease Provide your feedback")

    feedback = input("\tFeedback: ").strip()

    #adding the feedback to feedback.txt
    with open(feedBackFile,'a') as file:
        file.write(f"{userData['userName']} : {feedback}\n")
    
    print("\nThankyou for the feedback")


    

    



    

