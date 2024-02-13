def filter_prime(n):
    ok = False
    for j in range(2,n):
        if n%j == 0 :
            break
        else:
            ok = True
    return ok

x = int(input("x = "))
list = []
for i in range(x):
    i = int(input())
    if i == 2:
        list.append(i)
        continue
    if filter_prime(i) == True:
        list.append(i)
print(list)