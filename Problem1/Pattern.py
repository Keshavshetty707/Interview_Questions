
def print_pattern(n):
    edit_pattern=0
    for i in range(n, 0, -1):    
        for j in range(i, n + 1):
            print(j, end="")
        j=i
        while j-1 > 0:
            print(i+edit_pattern,end="")
            j-=1
        print()
        edit_pattern=edit_pattern+1

n = int(input("Enter number of rows: "))
print_pattern(n)





