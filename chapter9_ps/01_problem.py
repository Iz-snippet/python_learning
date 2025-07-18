# write a program  to read the text from a given file"poem.txt" and find
# out whether it contains the word "wander"

with open("poem.txt") as f:
    c= f.read()
    if("wander" in c):
        print("The word wander is present in the content")
    else:
        print("The word Wander is not present in the content")




