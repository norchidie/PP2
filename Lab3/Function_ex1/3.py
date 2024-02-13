def solve(numhead, numlegs):
    krolik = numlegs/2 - numhead
    tauyq = numhead - krolik
    print("krolik sany =",krolik,"\ntauyq sany =",tauyq)
a = int(input("head = "))
b = int(input("legs = "))
solve(a,b)