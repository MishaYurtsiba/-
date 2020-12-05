from random import randint
n=int(input("Введіть кількість рядків і стовпців"))
matrix=[[randint(-100,100)for j in range(n)]for i in range(n)]
print(matrix)
for j in range(n):
    for i in range(j+1,n):
        matrix[i][j]=0
print(matrix)




