a = int(input())
print(2**a - 1)
def hanoi(n, source, temp, destination):
    global count
    if n == 1:
        print("{0} {1}".format(source, destination))
    else:
        hanoi(n-1,source, destination, temp)
        print("{0} {1}".format(source, destination))
        hanoi(n-1,temp, source , destination)

hanoi(a, '1', '2', '3')
    
