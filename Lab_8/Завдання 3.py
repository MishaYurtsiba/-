def next_el(a0,a1,a2,a3):
    a4=a3*(1+a2)+a1/a0
    return a4
n=int(input("n="))
x0=1
x1=7
x2=7
x3=7
for i in range(n):
    x4=next_el(x0,x1,x2,x3)
    x3=x4
    x2=x3
    x1=x2
    x0=x1
print(x3)