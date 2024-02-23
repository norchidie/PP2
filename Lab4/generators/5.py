def ddd(n):
    for i in range(n,-1,-1):
        yield i
a = int(input("N = "))
number = ddd(a)
print(','.join(map(str,number)))