A=True
while A==True:
    Y=input(">")
    if Y=="help" or Y=="Help" or Y=="HELP":
        print("start = start the car")
        print("stop = stop the car")
        print("quit = quit the game")
    elif Y=="start" or Y=="Start" or Y=="START":    
        print("Car Statarted...Ready to go")
    elif Y=="stop" or Y=="Stop" or Y=="STOP":
        print("Car stopped")
    elif Y=="quit" or Y=="Quit" or Y=="QUIT":
        A=False
    else:
        print("I didn't understand that...")