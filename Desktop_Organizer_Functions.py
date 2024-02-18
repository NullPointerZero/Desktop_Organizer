
import os

# To keep things Tidy i want a seperate Functions folder in which all the functions will be coded. 

def organize(foldercontent, current_path, whitelist):
    for file in foldercontent:
        if file in whitelist:
            continue
        


''' This function takes foldercontent (list of files in folder)
the currentPath and a subdirectory in which it can put the files.
The subdirectory is defaulted as "sorted".
The function will take the filetype and make it a folder in sorted

'''
def make_directories(foldercontent, current_path, whitelist, sub_dir = "sorted"):
    file_type_list = [] 

    #This For loop is just to make a list with unique filetypes
    for file in foldercontent:      # iterate through the files
        if file in whitelist:       # Skip the whitelist files
            continue
        if "." in file:             # Only Files should be taken in the list. Files always have a ., so this is the condition.
            file_type = file.split(".")
            file_type_list.append(file_type[1])   # create a list of filetypes

    file_type_list_unique = list( set(file_type_list))  # make the list a set, and then a set again. This way the lisstcontent will be unique
    print(file_type_list_unique)
    
    # This for Loop is to make aktually make the directories.
    for file_type in file_type_list_unique:

        try:
            os.makedirs(os.path.join(current_path, sub_dir, file_type))
            print("Directories wurden erstellt")
        except:
            continue
        else:
            print(f"Directory '{file_type}' has been created")
    
    return

#change made
