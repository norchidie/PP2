import os

p = r"C:\Users\TUF\Desktop\PP2\Lab6\Dir\copyfromhere.txt"

if os.path.exists(p):
    os.remove(p)
else:
    print("This file doesn't exist")
