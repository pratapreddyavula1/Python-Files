for i in range(6):
    for j in range(i):
        print("*",end=" ")
    print(end="\n")

for i in range(6):
    for j in range(6):
        print("*",end=" ")
    print(end="\n")

for i in range(0,6,1):
    for j in range(6,i,-1):
        print("*",end=" ")
    print(end="\n")

for i in range(7):
    for j in range(7):
        if (i == 0 or j == 0) or i == 6 or j == 6 or i==3 and j==3:
            print("*",end=" ")
        else:
            print(end="  ")
    print("\n")

s=0

for i in range(1,101):
    for j in range(1,5):
        if j%i==0:
            s=s+i
    print(i)
    s=0

n=5
fact=1
for i in range(1,n+1):
    if i<=n:
        fact=fact*i
print(fact)


#BMI(Body Mass Index)
Height=7.8
Weight=76
Height1=Height*0.4536

BMI=Weight/Height1
print(BMI)

n = 5
for i in range(0, n + 1):
    for j in range(0, n - i - 1):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

n = 5
for i in range(n, 0, -1):
    for j in range(0, n - i):
        print(end=" ")
    for j in range(0, i + 1):
        print("*", end=" ")
    print()

n = input("Enter a String:")
length = len(n)
for i in range(0, length):
    for j in range(0, i + 1):
        print(n[j], end=" ")
    print(end=" ")
    print()


for i in range(0,6,1):
    k=ord("A")+i
    for j in range(0,i+1,1):
        print(chr(k),end=" ")
    print(end=" ")
    print(end="\n")

# Print Pascal's Triangle in Python

# input n
n = 5

for i in range(1, n+1):
    for j in range(1, n-i+1):
        print(" ",end='')
    c=1
    for j in range(1, i+1):
        print(c,end=" ")
        c=c*(i-j)//j
    print()






