num = int(input("Enter a Value : "))
x = 1
while x <= num :
  i = 1
  c = 0
  while i<=x:
    if x%i == 0:
      c = c + 1
    i = i + 1
  if c == 2 :
    print(x,end=" ")


  x = x + 1