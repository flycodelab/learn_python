def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

flist = [plus, minus]
print(flist[0](1, 2))
print(flist[1](1, 2))

