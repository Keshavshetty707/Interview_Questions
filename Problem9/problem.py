list = []
flag = 1
numb = int(input("Enter the number of elements in the list: "))
print("Enter list elements:")
for i in range(numb): 
    temp = int(input())
    list.append(temp)
print("Enter a target value: ")
target = int(input())
for i in range(0,numb,1):
    if target == list[i]:
        print(i+1)
        flag = 0
if flag == 1:
    for i in range(0,numb,1):
        if target < list[i]:
            print(i+1)
        