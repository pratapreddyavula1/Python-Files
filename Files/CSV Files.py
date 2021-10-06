import csv
f=open("a.csv","w+",newline="")
objw=csv.writer(f)
objw.writerow(["Sname","SID","Syear"])
while True:
    a=input("enter Student name:")
    b=int(input("enter Student ID:"))
    c=int(input("enter Student Passing Year:"))
    objw.writerow( [a,b,c] )

    ch=input("DO You want to continue (yes/No):")
    if ch.lower()=="no":
        break


f.close()


import csv
f=open("a.csv","r")
objr=csv.reader(f)
list1=list(objr)
f2=open("Copy.csv","w",newline="")
objw=csv.writer(f2)
objw.writerows(list1)
f.close()
f2.close()



import csv
f=open("a.csv","r")
objr=csv.reader(f)
list1=list(objr)

f3=open("copy.csv","r")
objr1=csv.reader(f3)
next(objr1)

list2=list(objr1)
f2=open("b.csv","w",newline="")
objw=csv.writer(f2)
objw.writerows(list1)
objw.writerows(list2)
f.close()
f3.close()

f2.close()


import os
Filename=input("Enter File name:")
a=os.path.isfile(Filename)
if a==True:
    print("File is Exist")
else:
    print("File Not exist")



import os
import csv
Filename=input("Enter File name:")
a=os.path.isfile(Filename)
if a==True:
    print("File is Exist")
    ch=input("Do you want to read the data (yes/no):")
    if ch.lower()=="no":
        print("Thanks for using ")
        exit()
    else:
        f=open(Filename,"r")
        objr=csv.reader(f)
        for i in objr:
            print(i)
else:
    print("File Not exist")


