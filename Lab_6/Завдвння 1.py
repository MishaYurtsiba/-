n=int(input("введіть квльквсть значень: "))
A=[]
B=[]
for i in range(1,n+1):
    a=float(input("Введвть число: "))
    if i%2==0:
        B.append(a)
print(max(B))