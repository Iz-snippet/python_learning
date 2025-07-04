# Importing the 'os' module to interact with the operating system
import os

# Asking the user to enter the path of the directory
directory_path = input("Enter the directory path: ")

# Try-except block to handle errors like invalid path or permission issues
try:
    # os.listdir() returns a list of files and folders in the specified directory
    contents = os.listdir(directory_path)

    # Printing a header message
    print(f"\nContents of '{directory_path}':")

    # Looping through the list and printing each item
    for item in contents:
        print(item)

# Handling the case where the directory doesn't exist
except FileNotFoundError:
    print("❌ Error: The specified directory does not exist.")

# Handling the case where the user doesn't have access to the directory
except PermissionError:
    print("❌ Error: You don't have permission to access this directory.")
