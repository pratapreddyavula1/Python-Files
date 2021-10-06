with open("a.txt","r+") as f:
	d=f.read()
	print(d)
	i=d.index("Russia")
	f.seek(i)
	f.write("Japan")
with open("a.txt","r") as f:
	d=f.read()
	print(d)

with open("abc.txt","r+") as f:
    print("Cursor location after opening :",f.tell())
    input()
    d=f.read()
    print(d)
    print("Cursor location after reading the data:", f.tell())
    input()

    print("###############")
    f.write("\n 222 mahi tm 36722")
    print("Cursor location after writing  :", f.tell())
    input()
    f.seek(0)
    print("Cursor location after seek function :", f.tell())
    input()
    print("********************")
    d1=f.read()
    print("afetr extracting the data:",d1)
print("Succcesfully Done")



#Adding two numbers...
f=open("one.txt","r")
f1=open("two.txt","r")
d=int(f.read())
d1=int(f1.read())
d4=d+d1
f2=open("c.txt","w")
f2.write(str(d4))

f.close()
f1.close()
f2.close()

#Merging two Files into new file...
f=open("one.txt","r")
d=f.read()
f1=open("two.txt","r")
d=d+",\n"
d1=f1.read()
d=d+d1
f2=open("c.txt","w+")
f2.write(d)
f2.read()
f.close()
f1.close()
f2.close()

