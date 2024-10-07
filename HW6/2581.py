start = int(input())
stop = int(input())
num_list = []
tmp = 0
def prime_num(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

for i in range(start, stop+1):
    if prime_num(i):
        num_list.append(i)
##end = len(num_list)-1
if not num_list:
    tmp = -1
    print(tmp)
else:
    for i in range(len(num_list)):
        tmp += num_list[i]
    print(tmp)
    print(num_list[0])