nambers=[]
with open("data1.txt","r") as f:
    for row in f:
        nambers.append(int(row))
positive_nambers=0
negative_nambers=0
for i in range(len(nambers)):
    if nambers[i]>0:
        positive_nambers +=1
    elif nambers[i]<0:
        negative_nambers +=1
if positive_nambers>negative_nambers:
    print ("Додатніх чисел більше")
elif negative_nambers>positive_nambers:
    print("Відємних чисел більше")
else:
    print("Їх кількість однакова")


