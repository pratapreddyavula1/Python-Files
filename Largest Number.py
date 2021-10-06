def largest(num):
    largest=num[0]
    second_largest=num[0]
    for i in range(1,len(num)):
        if (num[i]>largest and num[i]%2!=0):

            second_largest=largest
            largest = num[i]
            print("Largest number is", largest)
        elif (num[i]>second_largest and num[i]%2!=0):
            second_largest=num[i]
            print(" second Largest number is", second_largest)






num=[32,45,78,98,65,78,67,88,39]
largest(num)