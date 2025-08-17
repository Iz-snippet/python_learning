try:
    a=int(input("Hi Ishake, Enter a number:- "))
    print(a)
except ValueError as v:
    print("hey")
    print(v)
except TypeError as t:
    print(t)
except Exception as e:
    print(e)

