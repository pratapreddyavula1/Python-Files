x=1
while x<=6:
    y=1
    while y<=6:
        if (x==1 or y==1)  or x==6 or y==6 :
            print("*",end=" ")
        else:
            print(end="  ")
        y=y+1
    print(end="\n")
    x=x+1
