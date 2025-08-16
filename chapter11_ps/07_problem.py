# Override the __len__() method on Vector of problem 5 to display the dimension of the vector.


class Vector:
    def __init__(self,list):
        self.l=list
       


    def __len__(self):
        return len(self.l)
# Test the implementation
v1=Vector([1,2,3])
v2=Vector([4,5,6])
v3=Vector([7,8,9])

print(len(v1))
print(len(v2))
print(len(v3))
