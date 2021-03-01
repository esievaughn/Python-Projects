

import os.path

fname = 'Hello.txt'

fPath = 'C:\\A\\'   #two escapes tells python to ignore the next character, so backlash indicates location instead of a new line

abPath = os.path.join(fPath, fname) #file name concatenated to path
print(abPath)               #created an absolute file path


import os 
  
  
# If we do not specify any path 
# os.listdir() method will return 
# the list of all files and directories 
# in current working directory 
  
dir_list = os.listdir() 
  
print("Files and directories in  current working directory :")  
  
# print the list 
print(dir_list) 
