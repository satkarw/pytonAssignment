import os
from commonFunctions import updateProfile

userFile = 'users.txt'
orderFile = 'order.txt'
feedbackFile = 'feedback.txt'

def admin_menu(userData):
    print(f"\nWelcome {userData['userName']} to the Admin Panel")

    while True:
        os.system('clear' if os.name == 'posix' else 'cls')  # Clearing terminal for better experience
        print("\nAdmin Panel")
        print("\t1. Manage Staff : Add/Edit/Delete")
        print("\t2. View Sales Reports")
        print("\t3. View Customer Feedback")
        print("\t4. Update Profile")
        print("\t5. Logout")

        action = input("\nChoose an action: ")

        if action == "1":
            manageStaff()

        elif action == "2":
            view_salesReport()

        elif action == "3":
            viewFeedback()

        elif action == "4":
            updateProfile(userData)

        elif action == "5":
            print("Logging out...")
            break

        else:
            print("Invalid choice! Please Enter again")


def manageStaff():
    allusers = []
    id = 1

    with open(userFile, 'r') as file:
        for line in file:
            userName, password, role = line.strip().split(",")
            allusers.append({
                'id': id,
                'userName': userName,
                'password': password,
                'role': role
            })
            id += 1

    action = input("\nWhat would you like to do? (Add / Edit / Delete): ").lower()

    if action == "add":
        print("\nAdd Staff Member\n")

        userName = input("\nEnter User Name: ")
        password = input("\nEnter password: ")
        role = input("\nEnter role (manager/chef/customer): ")

        with open(userFile, 'a') as file:
            file.write(f"{userName},{password},{role}\n")

        input("\nNew staff member added successfully. Press Enter\n")

    elif action == "delete":
        print("\nStaff Members\n")

        for user in allusers:
            if user['role'] != 'admin':
                print(f"id:{user['id']}\nName:{user['userName']}\nRole:{user['role']}")
                print("---------------------------------------------------------\n")

        selection = input("Enter id to delete: ")

        for user in allusers:
            if str(user['id']) == selection:
                allusers.remove(user)

        with open(userFile, 'w') as file:
            file.write('')

        with open(userFile, 'a') as file:
            for user in allusers:
                file.write(f"{user['userName']},{user['password']},{user['role']}\n")

        input("\nStaff member deleted successfully. Press Enter\n")

    elif action == "edit":
        print("\nStaff Members\n")

        for user in allusers:
            if user['role'] != 'admin':
                print(f"id:{user['id']}\nName:{user['userName']}\nRole:{user['role']}")
                print("---------------------------------------------------------\n")

        selection = input("Enter id to edit: ")

        for user in allusers:
            if str(user['id']) == selection:
                newName = input("\nEnter new name or press enter to leave it as it: ")
                newPass = input("\nEnter new password or press enter to leave it as it: ")
                newRole = input("\nEnter new role or press enter to leave it as it: ")

                if newName != '':
                    user['userName'] = newName
                if newPass != '':
                    user['password'] = newPass
                if newRole != '':
                    user['role'] = newRole

        with open(userFile, 'w') as file:
            file.write('')

        with open(userFile, 'a') as file:
            for user in allusers:
                file.write(f"{user['userName']},{user['password']},{user['role']}\n")

        input("\nStaff member edited successfully. Press Enter\n")


def view_salesReport():
    orders = []

    with open(orderFile, 'r') as file:
        for line in file:
            userName, itemName, price, quantity, status = line.strip().split(',')
            orders.append({
                'userName': userName,
                'itemName': itemName,
                'price': int(price),
                'quantity': int(quantity),
                'status': status
            })

    total_sales = 0
    print("\nSales Report\n")

    for order in orders:
        if order['status'] == 'Completed':
            total_sales += order['price'] * order['quantity']
            print(f"User: {order['userName']}, Item: {order['itemName']}, Quantity: {order['quantity']}, Price: {order['price']}, Status: {order['status']}")
            print("---------------------------------------------------------\n")

    print(f"Total Sales: {total_sales}\n")
    input("Press Enter to go back to menu\n")


def viewFeedback():
    feedbacks = []

    with open(feedbackFile, 'r') as file:
        for line in file:
            feedbacks.append(line.strip())

    print("\nCustomer Feedback\n")

    for feedback in feedbacks:
        print(feedback)
        print("---------------------------------------------------------\n")

    input("Press Enter to go back to menu\n")