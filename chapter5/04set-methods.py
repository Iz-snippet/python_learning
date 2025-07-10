s= {1,5,32}

s.add(100)
print(s) # adds 100 to the set

print(len(s)) # prints the length of the set

s.remove(100) # removes 100 from the set
print(s) 

s.pop() # removes and returns an arbitrary element from the set
print(s)

s.clear() # clears the set
print(s) 

b= {83, 56, 67, 43, 1}
b.union({1,43,56.67}) # returns a new set with elements from both sets
print(b)

b.intersection({1,43,56.67}) # returns a new set with elements common to both sets
print(b)