f= open("file.txt")
data=f.read()
print(data)
f.close()
print("\n")
#the same can be written using with statement like this :

with open("file.txt") as f:
    print(f.read())

# you dont habve to explicity close the file
