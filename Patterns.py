# --------------------------------------------PATTERNS---------------------------------------------

''' QUES1. Wap to print star pattern.'''
'''print("left hand side star pattern")
x = int(input("Enter any number : "))
for i in range(x):
    for j in range(0,i+1):
        print("*",end=" ")
    print()'''

''' QUES2. Wap to print a square using star pattern.'''
'''print("Square Star Pattern")
x = int(input("Enter any number: "))
for i in range(0,x):
    for j in range(0,x):
        print("*",end=' ')
    print()'''

''' QUES3. Wap to print a Hollow Pattern.'''

'''for i in range(0,5):
    for j in range(0,5):
        if i == 0 or i == 4 or j == 0 or j == 4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()'''

'''QUES4. Wap to print a "C" pattern using star pattern.'''
''' n = int(input("Enter the number: "))
m = int(input("Enter the number: "))
for i in range(0,n+1):
    for j in range(0,m+1):
        if i == 0 or i == n+1 or i == n or j == 0 or j == m+1 or i == m :
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()'''

''' QUES5. Wap to print Unique pattern using star pattern.'''
# n = int(input("Enter the number: "))
# m = int(input("Enter the number: "))
# for i in range(0,n+1):
#     for j in range(0,m+1):
#         if i == 0 or i == n+1 or i == n or i ==2 or j == 0 or j == m+1 or j== m or j==2 :
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

'''QUES6. Wap to print  another unique pattern using star pattern.'''
# n = int(input("Enter the number: "))
# m = int(input("Enter the number: "))
# for i in range(0,n+1):
#     for j in range(0,m+1):
#         if i == 0 or i ==2 or i == n  or j == 0 or j == 2 or j== m  :
#             print("*",end=' ')
#         else:
#             print(" ",end=" ")
#     print()

'''QUES6. Wap to print  another unique pattern using star pattern.'''

n = int(input("Enter the number: "))
m = int(input("Enter the number: "))
for i in range(0,n+1):
    for j in range(0,m+1):
        if i == 0 or i == n+1 and j == 0 or j == m+1:
            print("*",end=' ')
        else:
            print(" ",end=" ")
    print()