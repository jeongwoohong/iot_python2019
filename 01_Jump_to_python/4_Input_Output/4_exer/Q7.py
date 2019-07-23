with open("test.txt", "r") as f:
    body = f.read()

body= body.replace("jave","python")

with open("test.txt","w") as f:
    f.write(body)