
#Python:    3.9
#Author:    Esie V.
#Purpose:   Preliminary Framework for Nice/Mean Game--how to pass a function to function while producing a working game.
#           funcitonName(variable) _means that we pass in the variable.
#           return variable _means we are returning the variable back to the calling funciton


def start():            
        print(getNumber())


def getNumber():        #passes variable to start function 
    number = 12
    return number


def start():            
        print("Hello {}".format(getName())) #squiggly wild card that place holds input name

def getName():
    name = input("What is your name? ")
    return name

def start():
    fname = "Sarah"
    lname = "Connor"
    age = 28
    gender = "female"
    get_info(fname, lname, age, gender)

def get_info(fname, lname, age, gender):        #calls multiple variables 
    print("My name is {} {}. I am {} years old {}.".format(fname,lname,age,gender))



if __name__ == "__main__":
    start() 
