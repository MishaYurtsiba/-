class Pularl:

    def __init__(self,n=0):
        self.n=n
        self.array=[0]*n

    def push(self,el):
        self.el=el
        self.array.append(el)

    def print_to_screen(self):
        print(self.array)

    def max_namber(self,):
        print(max(self.array))
    def sum(self):
        print(sum(self.array))
f=Pularl()
f.push(5)
f.push(4)
f.print_to_screen()
f.max_namber()
f.sum()








