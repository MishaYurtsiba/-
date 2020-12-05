#Побудувати прямокутну матрицю А, елементи якої задаються формулою:
n=int(input("Введіть кількість рядків"))
m=int(input("Введіть кількість стовпців"))
matrix=[]
for i in range(n):
    matrix.append([])
    for j in range(m):
        a=(i**j)-(j**i)
        matrix[i].append(a)
print(matrix)
#Обчислити суму елементів матриці А, сума індексів яких непарна.
sum=0
for j in range(m):
    for i in range(n):
        if (i+j)%2==1:
            sum+=matrix[i][j]
print(sum)
