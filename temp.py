from math import floor, ceil, modf
def func1():
    A = -650
    div = A / 200
    # print(div)        -3.25
    r = abs(modf(div)[0])
    print(r)
    if A < 0:
        if r >= 0.5:
            return floor(div)
        else:
            return ceil(div)
    else:
        if r >= 0.5:
            return ceil(A/200)
        else:
            return floor(A/200)
        
print(func1())