def find_number(nums):
    n = len(nums)
    total = n * (n + 1) // 2
    list_sum = sum(nums)
    return total - list_sum


numb = int(input("Enter the number of elements in the list: "))
list = []
print("Enter list elements:")
for i in range(numb): 
    temp = int(input())
    list.append(temp)


missing_number = find_number(list)
print("The missing number is:", missing_number)