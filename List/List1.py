list=["apple","bat","cat","mango"]
new_list=[]
print(list[0])
list.append("bhy")
list.insert(1,"bdj")
list.pop()
list.remove("bdj")
list2=["apple","bat","cat","mango"]
list.extend(list2)
for x in list:
    if "a" in x:
        new_list.append(x)


print(new_list)

list.reverse()
list.sort()
print(list)