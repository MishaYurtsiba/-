def nsd(n,m):
    while n!=m:
        if n>m:
            n=n-m
        else :
            m=m-n
    return n
a=float(input("a="))
b=float(input("b="))
nsd1=nsd(a,b)
nsd2=nsd(a,4)
nsd3=nsd(24,b)
s=nsd1+nsd2+nsd3
print(s)