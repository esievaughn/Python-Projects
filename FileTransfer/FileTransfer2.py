#   FILE TRANSFER CHALLENGE

import datetime as dt
import os
from os import scandir
import shutil

     
#   DEMONSTRATING PULL FOR EACH FILE AND ITS META TIME IN SECONDS
with os.scandir('/Users/Owner/Desktop/NewModified/') as files:
    for f in files:
        info = f.stat()
        print("\nFILE NAME: ", f.name, "\nLAST MODIFIED: ", info.st_mtime)    


#   
#   DEFINING VARIABLES FOR TIME COMPARISION
now = dt.datetime.now()
ago = now-dt.timedelta(hours=24)
strftime = "%H:%M %m/%d/%Y"
created = '/Users/Owner/Desktop/NewModified/'
dest = '/Users/Owner/Desktop/HomeOffice/'

#   CREATE A FUNCTION UTILIZINZ WALK METHOD & SHUTIL COPY METHOD
def copyFile(self):
    for root, dirs, files in os.walk(created):
        for fname in files:
            self.path = os.path.join(root, fname)    #   JOIN FILE SYSTEM PATH WITH FILE NAE
            self.st = os.stat(path)                  #   RETURN STAT INFO REGARDING SPECIFED PATH
            self.mtime = dt.datetime.fromtimestamp(st.st_mtime)  #   MODIFIED TIME
            if self.mtime > ago:                     #   IF MODIFED IN THE LAST 24 HOURS
                print("NEW OR EDITED FILE TO BE MOVED:  ", fname, " at ", mtime.strftime("%H:%M %m/%d/%Y"))
                shutil.copy(path, dest)         #   COPY FILES TO DESTINATION FOLDER


if __name__ == "__main__":
    copyFile()
