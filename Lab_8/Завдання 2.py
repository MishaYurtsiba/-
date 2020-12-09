def progres(x1,x2,x3,x4):
    if x2/x1==x3/x2==x4/x3 :
        s=1
    else :
        s=0
    return(s)
sum=0
n=int(input("введіть квльквсть значень: "))
A=[]
for i in range(1,n+1):
    a = float(input("Введвть число: "))
    A.append(a)
for i in range(n-3):
    a1=A[i]
    a2=A[i+1]
    a3=A[i+2]
    a4=A[i+3]
    progres1=progres(a1,a2,a3,a4)
    sum=sum+progres1
print(sum)