def main():
    try:
        a=int(input("Hi Ishake, Enter a number:- "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("hey,I am inside the finally")

main()