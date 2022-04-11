# def reverse(str):
#     stack = []
#     for word in str:
#         stack.append(word[::-1])
#     y = ' '.join(stack)
#     return y

    
 
# str = input().split()
# print(reverse(str))

# input = 'learning python is very easy'
# otp = easy very is python Learning
# str = input().split()
# l1  = str[::-1]
# x = '--> '.join(l1)
# print(x)

# str = input().split()
# stack = []
# for i in str:
#     stack.append(i[::-1])
# y = ' '.join(stack)
# print(y)

# input --> one two three four five six
# output --> one owt three ruof five xis

# s =input().split()
# stack = []
# i = 0
# while i<len(s):
#     if i%2==0:
#         stack.append(s[i])
#     else:
#         stack.append(s[i][::-1])
#     i+=1
# y = ' '.join(stack)
# print(y)

''' QUES * Wap to print the char present at even index and odd index separately
for the given index. '''

def string_operation(str):
    print('For the even index ')
    i = 0
    while i<len(str):
        print(str[i])
        i+=2
    
    print('For the odd index')
    i = 1
    while i<len(str):
        print(str[i])
        i+=2
    

str = input('Enter the string: ')
print(string_operation(str))