class Graphic_file:

    def __init__(self,name=0,date=0,size=0):
        self.name=name
        self.date=date
        self.size=size
        print(f"{name},{date},{size}")


    def name_change(self,new_name):
        self.new_name=new_name
        self.name=new_name
        print(self.name)
    def new_size(self,new_size):
        self.size=new_size
        print(self.size)

f=Graphic_file("fije_1","20.12.2020",3)
f.name_change("file_2")
f.new_size(6)


