def even(n):
    for i in range(n):
        if  i%2 == 0:
            yield i

n = int(input("n = "))
numbers = even(n)
print(','.join(map(str,numbers)))