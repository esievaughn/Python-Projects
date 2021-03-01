

import os  #docs.python.org

fname = 'Hello.txt'

fPath = 'C:\\A\\'   #two escapes tells python to ignore the next character, so backlash indicates location instead of a new line

abPath = os.path.join(fPath, fname) #file name concatenated to path
print(abPath)               #created an absolute file path






