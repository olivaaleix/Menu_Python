#   Menu of PID Windows

import psutil
import os
import sys

def get_pid(name):
    notepads = (item.pid for item in psutil.process_iter() if item.name() == name)
    return list(notepads)

def KeyNum():

    correct=False
    num=0
    
    while(not correct):
        
        print(''' 
            Welcome to PID Option. You have the following options: 
            1.- Check and prints the actual PID and process names
            2.- Option 2
            3.- Option 3
            0.- Close
        ''')

        try:
            num = int(input("Give me an option: "))

            correct=True
        except ValueError:
            print ("Please, give me the correct number. Thanks")
    return num

exit = False
option = 0

while not exit:

    option = KeyNum()

    if option == 1:
        pid_name = input("PID Windows: ") #This 1st option lists with name and PID the actual active services
        results = get_pid(pid_name + ".exe")
        
        if len(results) > 0:
            # close them
            print(results)
            print("\n")
            print("Do you want to terminate the process? (y/n)")
            confirm = input()
            if confirm.lower() == 'y':
                os.system("taskkill /im "+pid_name+".exe 2> nul")
        else:
            print('No items found with that PID.')

    elif option == 2:
        print ("Option 2")
    elif option == 3:
        exit = True
    elif option == 0:
        print("Thanks for using this program!")
        sys.exit()
    else:
        print(" Give me a correct option")

print ("End") 
