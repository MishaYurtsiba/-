def next_el(n):
    if n==1:
        return 1
    elif n==2 or n==3 or n==4:
        return 7
    else :
        return next_el(n-1)*(1+next_el(n-2))+next_el(n-3)/next_el(n-4)
m=int(input("Введвть чилсо"))
s=next_el(m)
print(s)
