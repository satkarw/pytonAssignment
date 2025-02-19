import os

userFile = "users.txt"

def login():
    loginAttempts = 3 #max 3 attemts only

    while loginAttempts > 0:

        print(f"For demo purpose here are the Authentication Credentials: \n\n\tadmin, admin123 for admin\n\n\tmanager, manager123 for manager\n\n\tchef,chef123 for chef\n\n\tcustomer,customer123 for customer")
        userName = input("\nEnter userName: ").strip()
        password = input("\nEnter your password: ").strip()

        role = userAuth(userName,password) #authenticates user and returns role if user exists
        userData= {
                    'userName':userName,
                    'password':password,
                    'role':role
                   }

        if role:
            print(f"\nSuccessfully Logged-in!\n")
            return userData
        
        else:
            loginAttempts -=1
            print(f"\nInvalid username or password. No of attempts left {loginAttempts}\n")

    print("\nLogin attempt limit exceeded. Exiting System \n")
    exit()
        
def userAuth(userName,password):
    # this function will authenticate the user

    with open(userFile,"r") as f:
        for line in f:
            uname,passw,role = line.strip().split(",") #fetching userName, password and role from txt file

            if userName == uname and password == passw:
                return role #IF A MATCH IS FOUND
        
    return None # if no match is found

