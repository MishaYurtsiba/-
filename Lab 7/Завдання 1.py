from random import randint
n=int(input("Введіть кількість рядків і стовпців"))
matrix=[[randint(-100,100)for j in range(n)]for i in range(n)]
print(matrix)
positive_elements=0
i=0
j=0
for i in range(i+1,n):
    for j in range(n):
        if matrix[i][j]>0:
            positive_elements+=1
print("Кількість додатніх елементів:{0}".format (positive_elements))