def func(a,b):
    if a == b:
        return f'{a}'
    if a > b:
        return f'{a}, {func(a-1, b)}'
    if a < b:
        return f'{a}, {func(a+1, b)}'

print (func(10,1))
print ('Hello, world!')

def Test(t):
    return t