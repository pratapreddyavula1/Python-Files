des=input("enter Employee designation: ")
sal=int(input("enter Employee salary:"))

if des.upper()=="PM" :
    salary=((15/100)*sal)+sal

    print(" Hike of the  Enployee salary:", salary)

    print("Hike is 15%")

elif des.upper()=="TM" :
    salary=(17/100)+sal
    print(" Hike of the  Enployee salary:",salary)
    print("Hike is 17%")
elif des.upper()=="DEV" :
    salary=(15/100)+sal
    print(" Hike of the  Enployee salary:", salary)
    print("Hike is 14%")
else:
    print("Hike is 10%")

print("Employe designation is:",des)
print("Employee salary:",salary)
