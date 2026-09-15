while True:
    print("1.Add")
    print("2.Substract")
    print("3.Multiplication")
    print("4.Division")
    print("5.Factorial")
    print("6.exit")
    choice=int(input("Enter the choice="))
    match choice:
        case 1:
            a=int(input("Enter first number="))
            b=int(input("Enter second number="))
            print("Addition=",a+b)
        case 2:
            a=int(input("Enter first number="))
            b=int(input("Enter second number="))
            print("Substraction=",a-b)
        case 3:
            a=int(input("Enter first number="))
            b=int(input("Enter second number="))
            print("Multiplication=",a*b)
        case 4:
            a=int(input("Enter first number="))
            b=int(input("Enter second number="))
            print("Division=",a/b)
        case 5:
            a=int(input("Enter a number="))
            fact=1
            i=1
            for i in range(i,a+1):
                fact*=i
            print("Factorial=",fact)
        case 6:
            print("Program exited")
            break
        case _:
            print("Invalid choice")
