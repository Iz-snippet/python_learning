# write a program to greet all the person names stored in a list l1 and whicj starts with s

# l1=["Ishake","Harry","jit","Disha","siddharth"]

l1=["Ishake","Harry","jit","Disha","Siddharth"]
for name in l1:
    if(name.startswith("S")):
        print(f"Hello {name}")