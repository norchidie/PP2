def square(n,m):
    for i in range(n,m+1):
        yield i*i
a,b = map(int,input().split())
number = square(a,b)
print(','.join(map(str,number)))