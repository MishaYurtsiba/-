n=int(input("введіть квльквсть значень: "))
A=[]
B=[]
C=[]
S=[]
for i in range(1,n+1):
    a=float(input("Введвть значення вектора A: "))
    A.append(a)
    b=float(input("Введвть значення вектора B: "))
    B.append(b)
    c=float(input("Введвть значення вектораC : "))
    C.append(c)
    s=2*(a+c)-b
    S.append(s)
print("C=",S)


