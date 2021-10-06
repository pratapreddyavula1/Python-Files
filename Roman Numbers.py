def Roman(x):
    roman = {'I': 1, 'IV': 4,'V': 5,'IX': 9, 'X': 10, 'XL': 40,'L': 50,'XC': 90, 'C': 100,'CD': 400, 'D': 500, 'M': 1000,'CM': 900
              }
    i=0
    num=0
    while i <len(x):
        if i+1<len(x) and x[i:i+2] in roman:
            num+=roman[x[i:i+2]]
            i+=2
        else:
            num+=roman[x[i]]
            i+=1
    return num

print(Roman("IV"))
print(Roman("XLL"))