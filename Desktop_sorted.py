

## This program ist meant to sort your Desktop!
# Theres is no need for a virtual environment, this software is planned to be compiled, so that it can run on windows machines that dont have python installed. 


# all the Resources that are needed:
import json                                         # sice a json file is used, the module is needed
import os                                           # is needed to manipulate Files
from Desktop_Organizer_Functions import *           # Usually it is bad practice to import everything, but this file is made to fit, so we need everything.

# Some Initial Values go Here
current_path = os.getcwd()                          # The current Path may be needed as a parent folder

# Initialise the Program by loading the json file and putting it into a dictionary. 
# This way we can later check wether the key aka.fileending is in the dictionary and use the value as filepath 
f = open("folderconfig.json","r")
folder_config = json.loads(f.read())
f.close()

# next we initialise the whitelist. Not all Files should be sorted. And for the testing purposes in the folder, the configs and whitelists should also be untouched.
f = open("whitelist.txt","r")
whitelist = set()                                   # Here the set is built. A set is fast and doesnt allow duplicates.
while True:
    line = f.readline()
    whitelist.add(line.replace("\n",""))             # Every Line ends with \n. This has to be cut, otherwise the comparison with that string will fail
    if not line:                                    # If the line is empy, that means that the file is read. Now the loop has to be ended.
        break
f.close()


# This is just for testing purpose. I ll need it for my next coding session to remember what i did and what to do. Delete later.
foldercontent = os.listdir()
make_directories(foldercontent, current_path, whitelist)

"""
This is the mechanic to move the files. I have to come up with a mechanic to check wether a file with the same name already exists, since it will be overwritten otherwise.

current_path_and_name = os.path.join(current_path, foldercontent[3])
destination_path_and_name = os.path.join(current_path,"sorted",dir_name,foldercontent[3])
os.rename(current_path_and_name, destination_path_and_name)

"""
