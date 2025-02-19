#this module will contain common functions that can be used in any other modules

import os
userFile = 'users.txt'

def updateProfile(userData):

    print("\nUpadte Profile")
    print(f"\tUserName : {userData['userName']}")
    print(f"\tPassword: {userData['password']}")

    newUserName = userData['userName']
    newPassword = userData['password']
    newRole = userData['role']


    action= input("\nWhat would you like to update ? (only username or password ): ").lower()

    if action == 'username':
        newUserName = input("\nEnter your new username: ")


    elif action == 'password':
        newPassword = input("\nEnter new password: ")
    
    else:
        print("\nInvalid Choise.. No changes were made")
        return

    #reading the current user data before making changes
    users =[]
    with open(userFile,'r') as f:
        for line in f:
            u,p,r = line.strip().split(",") 

            users.append({
                'userName':u,
                'password':p,
                'role':r
            })
    
    changed = False #checks if changes were made

    for user in users:

        if user['userName'] == userData['userName'] and user['password']==userData['password']:
            user['userName']=newUserName
            user['password']=newPassword
            changed = True
            break
    
    if not changed:
        print("\nUser not found.. No changes were made")
    
    #clearing the file
    with open(userFile,'w') as file:
        file.write('')
    
    #adding updated data to the file
    with open(userFile,'a') as file:
        for user in users:
            file.write(f"{user['userName']},{user['password']},{user['role']}\n")

    input("\nProfile Updated Successfully. Press Enter to Continue")