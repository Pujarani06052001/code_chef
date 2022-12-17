for i in range(int(input("enter a number:"))):
    x=int(input("enter a number::"))
    y=int(input("enter a number::"))
    a=2*x
    b=5*y
    if a>b:
        print("Chocolate")
    elif a==b:
        print("Either")
    else:
        print("Candy")