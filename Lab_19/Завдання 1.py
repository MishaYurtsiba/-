nambers=[]
with open("data.txt","r") as f:
    for row in f:
        nambers.append(int(row))
n=len(nambers)
sum=0
for i in range(n):
    sum+=nambers[i]
s=sum/n
print(s)