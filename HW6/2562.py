a = []
def find_max(n):
    maximum = n[0]
    for i in range (len(n)):
        if n[i] > maximum:
            maximum = n[i]
    return (maximum, n.index(maximum)+1)

for i in range(9):
    b = int(input())
    a.append(b)

con = find_max(a)
print(con[0])
print(con[1])
