while True:
    print("\n--calculator--")
    print("1.Addition")
    print("2.Subtraction")
    print("3.multiplication")
    print("4.division")
    print("5.exit")
    choice=input("enter choice:")
    if choice=="5":
        print("thank you")
        break
    num1=float(input("enter first number:"))
    num2=float(input("enter second number:"))
    if choice=="1":
        print("result=",num1+num2)
    elif choice=="2":
        print("result=",num1-num2)
    elif choice=="3":
        print("result=",num1*num2)
    elif choice=="4":
        if num2==0:
            print("cannot divide by zero")
    else:
        print("result=",num1/num2)
else:
    print("invalid choice")