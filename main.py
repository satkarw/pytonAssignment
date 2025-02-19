import auth
import admin
import customer
import chef
import manager

def main():
    
    while True:
        print("\nWelcome to Delicious Resturant Mangement System\n\nPlease Login to your Account\n")
    
        userData = auth.login() #redirects to login.py for user Auth and returns userData

        if userData['role'] == "admin":
            admin.admin_menu(userData)

        elif userData['role'] == "manager":
            manager.manager_menu(userData)

        elif  userData['role'] == "chef":
            chef.chef_menu(userData)
        
        elif userData['role'] == "customer":
            
            customer.customer_menu(userData)

        else:
            print("\nError! Exiting System")
            break
        
if __name__ == "__main__":
    main()

