n=int(input("введіть квльквсть значень: "))
A=[]
B=[]
for i in range(1,n+1):
    a=float(input("Введвть число: "))
    if i%2==0:
        A.append(a)
    else:
        B.append(a)
print(A+B)