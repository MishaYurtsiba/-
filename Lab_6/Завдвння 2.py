import math
n=int(input("Введіть кількість елементів"))
x=float(input("x="))
A=[]
i=1
a1=i*(math.sin(i*x)+math.cos(i*x))
A.append(a1)
for i in range(1,n):
    a2=a1+(i+1)*(math.sin((i+1)*x)+math.cos((i+1)*x))
    A.append(a2)
    a2=a1
print(max(A))