

## This program ist meant to sort your Desktop!
# Theres is no need for a virtual environment, this software is planned to be compiled, so that it can run on windows machines that dont have python installed. 


# all the Resources that are needed:
import json                                         # sice a json file is used, the module is needed
import os                                           # is needed to manipulate files


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
    whitelist.add(line.replace("\n","")             # Every Line ends with \n. This has to be cut, otherwise the comparison with that string will fail
    if not line:                                    # If the line is empy, that means that the file is read. Now the loop has to be ended.
        break
f.close()



