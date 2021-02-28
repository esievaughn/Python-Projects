


import DunderMethods



def printDund2():
    name = (__name__)
    return name

if __name__ == "__main__": #when call on name, it will return string value of name of this file "DunderMethod2}
    #The following is calling code from within this script
    print("I am running code from {}".format(printDund2()))

    #The following is calling code from the imported DunderMethods.py
    print("I am running code from {}".format(DunderMethods.printDund()))

    
