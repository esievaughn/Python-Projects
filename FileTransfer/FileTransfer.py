#   FILE TRANSFER CHALLENGE

import shutil
import os

#   set the destination path to folderB
source= '/Users/Owner/Desktop/FileTransfer/FolderA/'

#   set the destination path to folderB
destination='/Users/Owner/Desktop/FileTransfer/FolderB/'
files = os.listdir(source)

for i in files:
    #   move the files represented by 'i' to their new destination
    shutil.move(source+i, destination)
    
