# Python program to print
# duplicates from a list
# of integers
def Repeat(x):
    duplicate = []
    for i in range(len(x)):
        k=i+1

        for j in range(k, len(x)):
            if x[i] == x[j] and x[i] not in duplicate:
                duplicate.append(x[i])
    return duplicate


# Driver Code
list1 = [10, 20, 30, 20, 20, 30, 40,
         50, -20, 60, 60, -20, -20]
print(Repeat(list1))

# This code is contributed
# by Sandeep_anand

from collections import Counter

l1 = [1,2,1,2,3,4,5,1,1,2,5,6,7,8,9,9]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item]>1])
print(new_list)


import datetime
import time

a=datetime.datetime.now()
starttime=time.perf_counter()
print("Today date is:",a)
print("Year is:",a.strftime("%Y"))
print("Month  is:",a.strftime("%m"))
print("day is:",a.strftime("%d"))
print("Week Day is:",a.strftime("%A"))
print("Hour is:",a.strftime("%H"))
print("Minutes are:",a.strftime("%M"))
print("Seconds are:",a.strftime("%S"))
print("Micro Seconds are:",a.strftime("%f"))
print(a.today())
endtime=time.perf_counter()
print(starttime)
print(endtime)
print("Excution Time is :",endtime-starttime)
