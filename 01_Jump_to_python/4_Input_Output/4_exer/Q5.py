f1 = open("test.txt","w")
f1.write("Life is too shrote")
f1.close()

f2 = open("test.txt","r")
print(f2.read())
f2.close()

with open("test.txt","w") as f1:
    f1.write("Life is too shrot")

with open("test.txt","r") as f1:
    print(f1.read())
