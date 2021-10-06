list4 = [9, [1,[[[2,4,5],6]]],27,[3,[[["a","b","c"]]],6],45,[9,18],36]
n=str(list4).count('[')
print(n)

for x in range(n):
    flatten = []
    for i in list4:
        if type(i) == list:
            for j in i:
                flatten.append(j)

        else:
            flatten.append(i)
    list4=flatten.copy()

print(list4)