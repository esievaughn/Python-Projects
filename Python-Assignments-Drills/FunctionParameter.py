
mySentence= 'loves the color'

colorList= ['red','blue','purple','orange','yellow', 'gray']

def colorFunction(name):    #parameter defined in function
    for i in colorList:
        print("{0} {1} {2}".format(name,mySentence,i))
        


colorFunction('Skylar') #calling in function and passing in argument for name




mySentence2= 'loves the color'

colorList2= ['red','blue','purple','orange','yellow', 'gray']

def colorFunction2(name1):
    list = [] #creating a temporary list to sort through all names
    for i in colorList2:
        msg= "{0} {1} {2}".format(name1,mySentence2,i)
        list.append(msg)#adds to the temporary list
    return list #msg is new variable to be sent back out; return indentation--if aligned pritns first index, if indented before msg it will return last index 
        


print(colorFunction2('Sky')) #print shows the return msg

list= colorFunction2('Sky') #returns better looking list by unpacking from array
for i in list:
    print(i) #each iteration printed

def getName():
    go= True
    while go: 
        name2= input('What is your name? ') #indent shows it is part of while/go block
        if name2 == '':      #if name is empty then print...
            print("You need to provide your name!")
        elif name2 == 'Sally':
            print("Sally you may not use this software.")
        else:
            go = False #will tell the while loop to stop 
    list= colorFunction2(name2)
    for i in list:
        print(i)

getName()

