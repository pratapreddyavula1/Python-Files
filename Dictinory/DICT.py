list1=[[5,6],4,(4,5,6),7,65,"India"]
list2=[]
for i in list1:
    if type(i)==list:
        list2.append(i)
        for j in i:
            if type(j)==tuple:
                list2.append(j)
                for k in j:
                    if type(k)==str:
                        list2.append(k)
    else:
        list2.append(i)
print(list2)

