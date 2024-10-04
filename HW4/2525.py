hour, min = input().split()
c = int(input())
a = int(hour)
b = int(min)

if b+c>=60:
    d = ((b+c)%60)
    e = ((b+c)//60)
    if a+e>=24:
        print((a+e)%24, d)
    else:
        print(a+e, d)
else:
    print(a, b+c)




