def largest(num):
    largest=num[0]
    second_largest=num[0]
    for i in range(1,len(num)):
        if num[i]<largest:

            second_largest=largest
            largest = num[i]
        elif num[i]<second_largest:
            second_largest=num[i]

    print("Largest number is",largest)
    print(" second Largest number is", second_largest)


num=[32,45,6,65,324,66,78]
largest(num)