def TF(n1,n2):
    f = 0
    while n1>0 or n2>0:
        t1  = (n1&1)
        t2  = (n2&1)
        if t1 != t2:
            f = f + 1
        n1>>=1
        n2>>=1
    return f
n1 = int(input("Enter a number : "))
n2 = int(input("Enter a number : "))
print(TF(n1,n2))

        