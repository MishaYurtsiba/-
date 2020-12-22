class Student:

    def __init__(self,name,surname,second_name,age,addres,rating):
        self.name=name
        self.surname=surname
        self.second_name=second_name
        self.age=age
        self.addres=addres
        self.rating=rating

    def __str__(self):
        return f"{self.name}{self.surname}{self.second_name}{self.age}{self.addres}{self.rating}"
    def  __repr__(self):
        return str(self)

class First_course:
    def __init__(self,file_name):
        self.list=[]
        self.file_name = file_name

    def __repr__(self):
        return self.list

    def __str__(self):
        return str(self.list)

    def add(self,i):
        self.list.append(i)


    def save_to_file(self):
        with open("First_course","w") as f:
            for i in self.list:
                f.write(f"{i.name}{i.surname},{i.second_name},{i.age},{i.addres},{i.rating}")

    def load_from_file(self):
        self.list.clear()
        with open("First_course.txt", "r") as f:
            for row in f:
                name,surname,econd_name,age,addres,rating=row.split(";")
                self.list.append(Student(name,surname,econd_name,age,addres,rating))

    def find_by_age(self,age):
        for i in self.list:
            if i.age == age:
                return i
        return None
fc=First_course
fc.add(Student("Юрциба","Михайло","Юрійович","17","Вул...","А"))
