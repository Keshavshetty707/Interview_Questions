# def Pattern(n):
#     for i in range ( 1,n,1):
#         for j in range(1,n,1):
#             k=0
#             temp=[]
#             if i==1:
#                 print(j, end="")
#             elif  i==2 and n==2:
#                 print(i+1, end="")
#             elif i>2:
#                 ele = n*2+j-k
#                 temp.append(ele)
#                 print(ele,end="")
#                 k=k+1
#                 size=len(temp)
#             elif i<n-1:
#                 temp1=temp[size-1]
#                 print(temp1,end="")
#                 temp1 += 1
#             else:
#                 print(i+j,end="")

# numb = int(input("Enter number of rows: "))
# Pattern(numb)


def Pattern(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i == 1:
                print(j, end="")
            elif i == 2 and n == 2:
                print(i+1, end="")
            elif i > 2:
                print(n*(i-1) + j, end="")
        print()  # Add a newline after each row

numb = int(input("Enter number of rows: "))
Pattern(numb)