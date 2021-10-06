
#Printing Odd/Even numbers Between Two numbers:
a=2
b=8
listEven=[]
listOdd=[]
while a<=b:
    if a%2==0:
        listEven.append(a)
    else:

       listOdd.append(a)

    a=a+1
print("These are Even numbers",listEven)
print("These are Even numbers",listOdd)
