f=open(r"C:\Users\TUF\Desktop\PP2\Lab6\Dir\sometext.txt")
cnt=0
for lines in f:
    cnt+=1
print("files has {} lines".format(cnt))