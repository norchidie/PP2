import os
p = os.listdir(r"C:\Users\TUF\Desktop\PP2\Lab6\Dir")
for i in p:
    if os.path.isdir(i):
        print(i)
for i in p:
    if os.path.isdir(i) or os.path.isfile(i):
        print(i)
for i in p:
    if os.path.isfile(i):
        print(i)
