
#Python:    3.9
#Author:    Esie V.
#Purpose:   how to pass a function to function while producing a working game.
#           funcitonName(variable) _means that we pass in the variable.
#           return variable _means we are returning the variable back to the calling funciton


def start(nice=0,mean=0,name=""):
    #get user's name
    name = describeGame(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describeGame(name):
    """
        check if this is a new game or not.
        If is new, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game
    """
    #meaning, if we do not already this user's name, then they are a new player
    #and we need to get their name

    if name != "": #if name is empty..
        print("\nThank you for playing again, {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name?\n>>>").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \nby several different people. \nYou can choose to be nice or mean")
                    print("but at the of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you, \nand mencingly storms off..")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the three variables to the score()


def show_score(nice,mean,name):
    print("\n{}, your current total: \n{}, Nice) and ({}, Mean)".format(name,nice,mean))

def score(nice,mean,name):
    #score function is being passed the values stored within the three variables
    if nice > 2: #if condition is valid, call win functions passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: #if condition is valid, call lose function passing the variables
        lose(nice,mean,name)
    else:           #call niceMean function passing in the variable so it use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    #call again function and pass in our variables
    again(nice,mean,name)

def lose (nice,mean,name):
    print("\nAhhh too bad, game over! \n{}, you live all alone!".format(name))
    again(nice,mean,name)


def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n):\n>>>").lower()
        if choice == "y":
            stop = False    #do not stop game, continue to reset
            reset(nice,mean,name)
        if choice == "n":
                print("\nOh, so sad, sorry to see you go!")
                stop = False
                quit()
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'NO':\n>>>")


def reset(nice,mean,name):       
    nice = 0        #reset values from previous game
    mean = 0
    #notice, do not reset variable as that same user has elected to play again
    start(nice,mean,name)


if __name__ == "__main__":
    start()


