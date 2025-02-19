import os
from commonFunctions import updateProfile

ordersFile = 'order.txt'
requestFile = 'ingredientsRequest.txt'

#since we will need fetching orders in multiple functions, we will be doing that here 
orders =[]


with open(ordersFile,'r') as file:
    orderId =1

    for line in file:
        userName,itemName,price,count,status = line.strip().split(',')

        orders.append({
            'orderId':orderId,
            'userName':userName,
            'itemName':itemName,
            'price':price,
            'count':count,
            'status':status
        })
        orderId +=1



def chef_menu(userData):
    print(f"Welcome to chef dashboard, {userData['userName']}")
    

    while True:
        
        print("\nChef Panel")
        print("\t1. View Orders")
        print("\t2. Update Order Status")
        print("\t3. Request Ingredients")
        print("\t4. Update Profile")
        print("\t5. Logout")

        action = input("\nChoose an action: ")

        if action == "1":
            viewOrders()

        elif action == "2":
            updateOrderStatus()

        elif action == "3":
            requestIngredients(userData)

        elif action == "4":
            updateProfile(userData)

        elif action == "5":
            print("Logging out...")
            break
        
        else:
            print("Error! Please enter again")



def viewOrders():
    #this function will let the chef view all orders
    global orders

    print("\nOrders\n")

    for order in orders:
        print(f"\tUserName: {order['userName']}\n\tItem Name: {order['itemName']}\n\tQuantity: {order['count']}\n\tStatus: {order['status']}..")
        print("==============================================\n")

    input("\nPress Enter to go back to menu\n")
    

def updateOrderStatus():

    print("\nOrders\n")
    for order in orders:
        print(f"\tOrderId:{order['orderId']}\n\tUserName: {order['userName']}\n\tItem Name: {order['itemName']}\n\tQuantity: {order['count']}\n\tStatus: {order['status']}..")
        print("==============================================\n")
    
    while True:

        selectedId = input("\nEnter the order id if the order is completed to change its status or 0 to exit: ")
        
        if selectedId == "0":

            break

        for order in orders:

            if str(order['orderId']) == selectedId:
                order['status'] = "Completed"
            
        
        
    #clearing the file
    with open(ordersFile,'w') as file:
        file.write('')

    #adding Updated Data
    with open(ordersFile,'a') as file:

        for order in orders:
            file.write(f"{order['userName']},{order['itemName']},{order['price']},{order['count']},{order['status']}\n")



    input("\nThe status has been updated from 'In Progress' to 'Completed'\nPress Enter to Return to Panel\n")
        
    
    


def requestIngredients(userData):

    while True:
        request = input("\nEnter your request or type done to exit: ")
        if request.lower() == 'done':
            break

        with open(requestFile,'a') as file:
            file.write(f"{userData['userName']},{request}\n")
            print("request added\n")
        


    
    