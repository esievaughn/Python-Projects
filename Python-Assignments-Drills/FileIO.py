#ACCESSING AND OPENING FILES

print(dir(str)) #produces all the methods associated with the str class

print(help(str))#help module associated with str 

import os
print(os.getcwd()) #get current directory

##########################################################################
import os

def writeData():
    data = '\nHello world!'
    with open('test.txt', 'a') as f: #write would overwrite current text; append adds additional text
        f.write(data)
        f.close()
    

def openFile():
    with open('test.txt', 'r') as f: #mode r is reading; modes shown under print(help(open)) in the shell
        data = f.read()             #f name assigned to file
        print(data)
        f.close()           #closes file to prevent memory leak





if __name__ == "__main__":
    writeData()
    openFile()
