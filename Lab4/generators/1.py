def square(a):
    for i in range(n):
        yield i**2
n = int(input("N = "))
number = square(n)
print(' '.join(map(str,number)))