import auth
import admin


def main():
    print("\nWelcome to Delicious Resturant Mangement System\nPlease Login to your Account")
    
    userData = auth.login() #redirects to login.py for user Auth and returns userData

    if userData['role'] == "admin":
        admin.admin_menu(userData)

    elif userData['role'] == "manager":
        # manager.manager_menu(userData)
        None

    elif  userData['role'] == "chef":
        # chef.chef_menu()
        None

    else:
        print("\nError! Exiting System")
    
if __name__ == "__main__":
    main()

