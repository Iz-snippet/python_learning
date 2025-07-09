# list methods

list=['1','8','7','2','21','15']

list.append("iz-snippet") # appends "iz-snippet" to the end of the list

print(list)

list.sort() # sorts the list in place
print(list)

list.reverse() # reverses the list in place
print(list) 

list.insert(31,10) # inserts 10 at index 31, which is out of bounds, so it will be added at the end
print(list)

list.pop(2) # removes the element at index 2
print(list)

list.remove('21') # removes the first occurrence of '21'
print(list)
