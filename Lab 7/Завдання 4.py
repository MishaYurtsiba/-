from random import randint
n=int(input("Введіть кількість рядків і стовпців"))
matrix=[[randint(-100,100)for j in range(n)]for i in range(n)]
print(matrix)
spad=[]
i=0
j=0
for i in range(j,n):
    for j in range(i,n):
        if i==j:
            spad.append(matrix[i][j])
print(spad)
for i in range(len(spad)):
    v=spad[i]
    j=i
    while(spad[j-1] < v) and (j > 0):
        spad[j]=spad[j-1]
        j=j-1
    spad[j]=v
print(spad)