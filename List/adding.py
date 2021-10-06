
s=0
list1=[]
for i in range(7):
    a=input("Enter a value:")
    list1.append(a)


print(list1)
s=0
for x in list1:
    s=s+int(x)
print(s)
list2=[]
for z in list1:
    list2.append(int(z)+100)
print(list2)
list3=[]
for y in list2:
    list3.append(int(x)+int(y))
print(list3)
