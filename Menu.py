
# Simple menu for giving options

def KeyNum():

    correct=False
    num=0
    
    while(not correct):
        
        print(''' 
            Welcome to this menu. You have the following options:

                        1.- PID Windows
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
        print ("PID Windows")
    elif option == 2:
        print ("Option 2")
    elif option == 3:
        exit = True
    else:
        print(" Give me a correct option")

print ("End") 
