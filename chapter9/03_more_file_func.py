f=open("file.txt","r")
lines=f.readlines()
print(lines, type(lines))

line1=f.readline()
print(line1, type(line1))

line2=f.readline()
print(line2, type(line2))

line3=f.readline()
print(line3, type(line3))
f.close()

