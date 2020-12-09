from random import randint
from math import fabs
n=int(input("Введіть кількість елементів"))
A=[randint(-100,100) for i in range(n) ]
print(A)
min_element=fabs(A[0])
for i in range(1,n):
    A[i]=fabs(A[i])
    if min_element>=A[i]:
        min_element=A[i]
print(min_element)

