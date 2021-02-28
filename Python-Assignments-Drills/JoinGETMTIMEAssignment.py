

import os.path
#################################   FUNCTION TO PRINT ENTIRE CURRENT WORKING DIRECTORY
dirList = os.listdir()         
print("\nLIST ALL FILES IN CURRENT WORKING DIRECTORY: \n")  
print(dirList)

#################################   GLOB METHOD TO FIND FILES MATCHING .TXT pattern
import glob

os.chdir(r'C:\\A\\')        #using glob method, return only .txt files
myFiles = glob.glob('*.txt')
print("\nLIST ONLY .txt FILES WITHIN CURRENT DIRECTORY: \n")
print(myFiles)



###################################### OS.PATH.JOIN AND GETMTIME()
import time
import datetime

modTime = os.path.getmtime('Hello.txt')
modificationTime1 = datetime.datetime.fromtimestamp(modTime).strftime('%Y-%m-%d %H:%M:%S')  #modificationTime structures time
fname1 = 'Hello.txt'
fPath2 = 'C:\\A\\'  

NameTime = os.path.join("\n"+ fname1 + "   " + modificationTime1) #file name concatenated to path
######################################

modTime2 = os.path.getmtime('file1.txt')
modificationTime2 = datetime.datetime.fromtimestamp(modTime2).strftime('%Y-%m-%d %H:%M:%S')
fname2 = 'file1.txt'
fPath3 = 'C:\\A\\'  

NameTime2 = os.path.join("\n"+ fname2 + "   " + modificationTime2) #file name concatenated to path
#######################################

modTime3 = os.path.getmtime('NewFile.txt')
modificationTime3 = datetime.datetime.fromtimestamp(modTime3).strftime('%Y-%m-%d %H:%M:%S')
fname3 = 'NewFile.txt'
fPath4 = 'C:\\A\\'  

NameTime3 = os.path.join("\n"+ fname3 + "   " + modificationTime3) #file name concatenated to path

print("\nLIST.txt FILES AND THEIR LAST MODIFICATION TIME: \n" + NameTime, NameTime2, NameTime3)
