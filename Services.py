#   Menu of PID Windows, this menu will have the diferents functions
#   that 

import psutil

def KeyNum():

    correct=False
    num=0
    
    while(not correct):
        
        print(''' 
            Welcome to PID Option. You have the following options: 
            1.- Check and prints the actual PID and process names
            2.- Option 2
            3.- Option 3
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
        print ("PID Windows :") #This 1st option lists with name and PID the actual active services

        for proc in psutil.process_iter():
            try: 
              pinfo = proc.as_dict (attrs=["pid", "name"])
            except psutil.NoSuchProcess:
              pass
        else:
             print(pinfo)

    elif option == 2:
        print ("Option 2")
    elif option == 3:
        exit = True
    else:
        print(" Give me a correct option")

print ("End") 
