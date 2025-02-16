import auth

def admin_menu(userData):
    #this will be the main function of this module
    print(f"\nWelcome {userData['userName']} to the Admin Panel")

    while True:

        print("\nAdmin Panel")
        print("1. Manage Staff : Add/Edit/Delete")
        print("2. View Sales Reports")
        print("3. View Customer Feedback")
        print("4. Update Profile")
        print("5. Logout")

        action = input("Choose acton: ")
        
        if action == "1":
            continue
            manageStaff()

        elif action == "2":
            continue
            view_salesReport()

        elif action == "3":
            continue
            viewFeedback()

        elif  action== "4":
            continue
            updateProfile()

        elif action == "5":
            print("Logging out...")
            break

        else:
            print("Invalid choice! Please Enter again")
        







