des=input("enter Employee designation:")
years=int(input("Enter Number of years:"))
if des.upper()=="PM":
    if years>5:
        print("Hike is 20%")
    elif 3>=years<5:

        print("Hike is 17%")
    elif 1>=years<3:
        print("Hike is 14%")
    else:
        print("Freshers")
elif des.upper()=="TM":
    if years>5:
        print("Hike is 18%")
    elif 3 >= years < 5:
        print("Hike is 16%")
    elif 1>=years<3:
        print("Hike is 12%")
    else:
        print("Freshers")
if des.upper()=="DEVLOPER":
    if years>=5:
        print("Hike is 17%")
    elif 3 >= years < 5:
        print("Hike is 15%")
    elif 1>=years<3:
        print("Hike is 13%")
    else:
        print("Freshers")
if des.lower()=="tester":
    if years>=5:
        print("Hike is 16%")
    elif 3 >= years < 5:
        print("Hike is 14%")
    elif 1>=years<3:
        print("Hike is 10%")
    else:
        print("Freshers")
print("Designation is:",des)
print("Number of years:",years)

