def squares(a , b):
    for x in range (a , b+1):
        yield x**2
a= 3
b = 7
for i in squares (a,b):
    print(i)