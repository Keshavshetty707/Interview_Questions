list = []
new_list = []
print("Enter number of array elements: ")
numb = int(input())
print("Enter array elements: ")
for i in range(numb):
    temp = int(input())
    list.append(temp)

for i in range(0,numb,1):
    if list[i] != 0:
        new_list.append(list[i])
    
for i in range(0,numb,1):
    if list[i] == 0:
        new_list.append(0)  

print(new_list) 