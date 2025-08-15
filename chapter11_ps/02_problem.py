#cerate a class "pets" from a class "Animals" and  further create class 'dog'from 'pets'.add a method 'bark' to class 'dog'

class Animals():
    pass

class pets(Animals):
    pass
class Dog(pets):    
    @staticmethod
    def bark():
        print("Wooooooooooooooooooooooooooof!")

d=Dog()
d.bark()
