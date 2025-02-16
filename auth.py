import os

userFile = "users.txt"

def login():
    loginAttempts = 3 #max 3 attemts only

    while loginAttempts > 0:

        print(f"For demo purpose here are the login data: \n\tadmin,admin123,admin\n\tmanager1,pass123,manager\n\tchef1,chefpass,chef\n\tcustomer1,custpass,customer")
        userName = input("\nEnter userName: ").strip()
        password = input("\nEnter your password: ").strip()

        role = userAuth(userName,password) #authenticates user and returns role if user exists
        userData= {
                    'userName':userName,
                    'password':password,
                    'role':role
                   }

        if role:
            print(f"\nSuccessfully Logged-in!")
            return userData
        
        else:
            loginAttempts -=1
            print(f"\nInvalid username or password. No of attempts left {loginAttempts}")

    print("\nLogin attempt limit exceeded. Exiting System \n")
    exit()
        
def userAuth(userName,password):
    # this function will authenticate the user

    f = open(userFile,"r")
    for line in f:
        uname,passw,role = line.strip().split(",") #fetching userName, password and role from txt file

        if userName == uname and password == passw:
            return role #IF A MATCH IS FOUND
        
    return None # if no match is found