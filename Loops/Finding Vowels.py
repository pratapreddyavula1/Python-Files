#Finding Number of Vowels in word
word=input("Enter a word:")
vowels={"a","e","i","o","u"}
result={}
for i in word:
    if i in vowels:
        result[i]=result.get(i,0)+1
for k,m in result.items():
    print(k,"present  in ",m ,"Times")



#own way to find vowels in a given word
word = input("Enter a string Word:")
list = ["a", "e", "i", "o", "u"]
for j in range(len(list)):
    a = word.count(list[j])
    print(list[j], "present in Word", a, "Times")


