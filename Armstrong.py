def check_armstrong(num):
    order = len(str(num))

    sum = 0

    # use temp to find each digit. Then power it
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** order
        temp //= 10
    return num == sum
