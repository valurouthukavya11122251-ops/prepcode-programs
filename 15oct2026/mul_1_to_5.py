def mul(n):
    if n<=1:
        return 1
    return mul(n-1)*n
print(mul(5))        