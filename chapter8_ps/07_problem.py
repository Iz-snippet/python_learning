# write a python function to remove a given word from a list and strip it at the sme time

def rem(l,word):
    n=[]
    for item in l:
       if not(item==word):
           n.append(item.strip(word))
l=["Ishake","Upashana","kausiki","jit","ana"]

print(rem(l,"ana"))
