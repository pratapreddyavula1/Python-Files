def palindrome(num):
    num2=num[::-1]
    if num==num2:
        print("It's a Palindrome")
    else:
        print("Not")

palindrome("123.321")