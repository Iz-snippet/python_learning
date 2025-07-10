a={
    "name" : "Ishake",
    "form" : "India",
    "marks": [92,98,96]
}

# methods of dictionaries
print(a.items()) # returns a list of tuples containing key-value pairs

print(a.keys()) # returns a list of keys

(a.update({"age" : 19})) # adds a new key-value pair to the dictionary
print(a)

print(a.get("name")) # returns the value of the key "name"