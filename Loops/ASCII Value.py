x=int(input("Enter a Value:"))
while x<=122:
    if (x>=65or x<=91):
        print(chr(x))
    elif (x >= 97 or x <=123):
        print(chr(x))
    elif (x>=48 or x<=58):
        print(x)
    else:
        print("Symbols")
    x=x+1



