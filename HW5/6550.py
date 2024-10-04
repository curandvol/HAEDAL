try:
    while True:
        line = input().strip()
        if not line: 
            break
        
        a, b = line.split()  
           
        a_list_index = 0
        b_list_index = 0

        while a_list_index < len(a) and b_list_index < len(b):
            if a[a_list_index] == b[b_list_index]:
                a_list_index += 1
            b_list_index += 1

        if a_list_index == len(a):
            print("Yes")  
        else:
            print("No")
except EOFError:
    pass  