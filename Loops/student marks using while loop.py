
while True:
    StudentName =input("Enter  a student name:")
    RollNumber=int(input("enter Roll Number:"))
    j=1
    Total=0
    while j<=5:
        list=["Maths","Science","DSP","Social","M1"]
        Marks=int(input("Enter "+list[j-1]+" marks :"))
        j=j+1
        Total=Total+Marks
        avg=Total/len(list)
        Grade = "A+" if avg >= 90 else "A" if avg >= 60 and avg < 90 else "B" if avg >= 50 and avg < 60 else "F"
    print("Student Name:",StudentName)
    print("Roll Number is:",RollNumber)
    print("total marks :",Total)
    print("Average Marks is:",avg)
    print("Grade:",Grade)
    ch=input("Do you want to continue(yes/no):")
    if ch.lower()=="no":
        print("Data sufficiently stored ")
        print("Thank you")
        break








