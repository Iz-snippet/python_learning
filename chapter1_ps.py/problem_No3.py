"""Write a python program do print the contents of
 A directory using 0s module. Search online
 for the function which does that. """

import os

# Get the path of the directory you want to list
directory_path = input("Enter the directory path: ")

try:
    # List all files and directories in the given path
    contents = os.listdir(directory_path)
    
    print(f"\nContents of '{directory_path}':")
    for item in contents:
        print(item)

except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
