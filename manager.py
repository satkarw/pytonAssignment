import os
from commonFunctions import updateProfile

userFile = 'users.txt'
menuFile ='menu.txt'
requestFile = 'ingredientsRequest.txt'


def manager_menu(userData):

    print(f"Welcome to Manager dashboard, {userData['userName']}")
    

    while True:
        
        print("\nManager Panel")
        print("\t1. Manage Customer (Add,Edit,Delete)")
        print("\t2. Manage menu")
        print("\t3. View Requested Ingredients")
        print("\t4. Update Profile")
        print("\t5. Logout")

        action = input("\nChoose an action: ")

        if action == "1":
            manageCustomer()

        elif action == "2":
            manageMenu()

        elif action == "3":
            viewRequests()

        elif action == "4":
            updateProfile(userData)

        elif action == "5":
            print("Logging out...")
            break
        
        else:
            print("Error! Please enter again")

def manageCustomer():

    allusers=[]
    id = 1

    with open(userFile,'r') as file:

        for line in file:

            userName,password,role = line.strip().split(",")
            
            allusers.append({
                    'id':id,
                    'userName':userName,
                    'password':password,
                    'role':role

                })
            id += 1
                

                
    
    action=input("\nWhat would you like to do ? (Add / Edit / Delete)?: ").lower()

    if action == "add":
            
        print("\nAdd Customer\n")

        userName = input("\nEnter User Name: ")
        password = input("\nEnter password: ")

        with open(userFile,'a') as file:
            file.write(f"{userName},{password},customer\n")
            
        input("\nNew user Added Successfully. Press Enter\n") 
    
    elif action == "delete":
        
        print("\nUsers\n")

        for user in allusers:
            if user['role'] == 'customer':
                print(f"id:{user['id']}\nName:{user['userName']}\nRole:{user['role']}")
                print("---------------------------------------------------------\n")
        
        selection = input("Enter id to delete: ")

        for user in allusers:

            if str(user['id']) == selection:
                allusers.remove(user)
        
        with open(userFile,'w') as file:
            file.write('')
        
        with open(userFile,'a') as file:
            
            for user in allusers:
                file.write(f"{user['userName']},{user['password']},{user['role']}\n")

        input("\nUser Deleted Successfully. Press Enter\n")
    
    elif action == "edit":
        
        print("\nUsers\n")

        for user in allusers:
            if user['role'] == 'customer':
                print(f"id:{user['id']}\nName:{user['userName']}\nRole:{user['role']}")
                print("---------------------------------------------------------\n")
        
        selection = input("Enter id to edit: ")

        for user in allusers:

            if str(user['id']) == selection:

                newName = input("\nEnter new name or press enter to leave it as it: ")
                newPass = input("\nEnter new password or press enter to leave it as it: ")

                if newName != '':
                    user['userName'] = newName 
                
                if newPass != '':
                    user['password'] = newPass
                
        
        with open(userFile,'w') as file:
            file.write('')
        
        with open(userFile,'a') as file:
            
            for user in allusers:
                file.write(f"{user['userName']},{user['password']},{user['role']}\n")

        input("\nUser Edited Successfully. Press Enter\n")
        
        
        
def manageMenu():
    id =1
    menu =[]

    with open(menuFile,'r') as file:
        for line in file:
            item,price = line.strip().split(",")

            menu.append({
                'id':id,
                "itemName":item,
                "price":price

            })
            id +=1
    
    print("\nMenu\n")

    for item in menu:

        print(f"\tid:{item['id']}\n\tName:{item['itemName']}\n\tPrice:{item['price']}")
        print("----------------------------------------------------------------\n")
    
    action = input("\nWhat would you like to do ? (Add / Edit / Delete)?: ").lower()

    if action == "add":

        print("\nAdd Item\n")

        itemName = input("\nEnter Item Name: ")

        price = input("\nEnter Price: ")

        with open(menuFile,'a') as file:

            file.write(f"{itemName},{price}\n")
        
        input("\nNew Item Added Successfully. Press Enter\n")
    
    elif action == "delete":

        print("\nMenu\n")

        selection = input("Enter id to delete: ")

        for item in menu:

            if str(item['id']) == selection:
                menu.remove(item)
        
        with open(menuFile,'w') as file:
            file.write('')
        
        with open(menuFile,'a') as file:
            
            for item in menu:
                file.write(f"{item['itemName']},{item['price']}\n")


        
        input("\nItem Deleted Successfully. Press Enter\n")
    
    elif action =="edit":
        
        print("\nMenu\n")

        for item in menu:

            print(f"id:{item['id']}\nName:{item['itemName']}\nPrice:{item['price']}")
            print("---------------------------------------------------------\n")
        
        selection = input("Enter id to edit: ")

        for item in menu:

            if str(item['id']) == selection:

                newName = input("\nEnter new name or press enter to leave it as it: ")
                newPrice = input("\nEnter new price or press enter to leave it as it: ")

                if newName != '':
                    item['itemName'] = newName 
                
                if newPrice != '':
                    item['price'] = newPrice
                
        
        with open(menuFile,'w') as file:
            file.write('')
        
        with open(menuFile,'a') as file:
            
            for item in menu:
                file.write(f"{item['itemName']},{item['price']}\n")

        input("\nItem Edited Successfully. Press Enter\n")



def viewRequests():
    requests = []

    with open(requestFile,'r') as file:
        for line in file:
            userName,ingredient = line.strip().split(",")

            requests.append({
                'userName':userName,
                'ingredient':ingredient
            })
    
    print("\nRequested Ingredients\n")

    for request in requests:

        print(f"\{request['userName']} reqested {request['ingredient']}")
        print("---------------------------------------------------------\n")
    
    input("\nPress Enter to go back to menu\n")

        
        
        



    
    