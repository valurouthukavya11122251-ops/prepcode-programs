def add(n):
    if n<=15:
        return 15
    return add(n-1)+n
print(add(25))        