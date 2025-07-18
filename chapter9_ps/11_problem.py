# Write a Python program to rename a file to "renamed_by_python.txt".


with open("old.txt") as f:
    content=f.read()

with open("rename_by_python.txt", "w") as f:
   f.write("")



