from random import randint
class Matrix:
    def __init__(self,n,m):

        self.matrix=[[randint(-100,100)for j in range(n)]for i in range(m)]

    def print(self):
        matrix=self.matrix
        for i in range(len(matrix)):
            print(matrix[i])

    def max_element(self):
        self.max_el=0
        for i in range(self.n):
            for j in range(self.m):
                if self.matrix[i][j]>self.max_el:
                    self.max_el=self.matrix[i][j]
        print(self.max_el)
    def min_element(self):

        for i in range(self.n):
            for j in range(self.m):
                self.min_el =self.matrix[0][0]
                if self.matrix[i][j] <self.min_el:
                    self.min_el = self.matrix[i][j]
        print(self.min_el)
    def sum(self):
        self.sum_el=0
        for i in range(self.n):
            for j in range(self.m):
                self.sum_el+=self.matrix[i][j]
        print(self.sum_el)



d=Matrix(3,4)
d.print()
d.max_element()
d.sum()
d.min_element()




