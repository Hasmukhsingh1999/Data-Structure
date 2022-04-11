'''' Given a single string from two given string,
a space and swap thre first two characters of each string.'''
# otp1 -> 'ebch'
# otp2 -> 'afgd' 

# def swap_string(str1,str2):
#     res = str2[0] + str1[1:-1] + str2[-1]
#     res1 = str1[0] + str2[1:-1] + str1[-1]
#     return res , res1

# str1 = input("Enter the string1:")
# str2 = input("Enter the string2:")
# print(swap_string(str1,str2))

# ----------------------------------------------------------------------------------------------
'''Given a single string from a given string concatenate the second string into first string'''
# otp -> abcghdef
# def concatenate(str1,str2):
#     x = len(str1)//2
#     res = str1[0:x] + str2 + str1[x::] 
#     return res

# str1 = 'abcdef'
# str2 = 'gh'
# print(concatenate(str1,str2))
# str1 = "Ault"
# str2 = "kelly"
# x = len(str1)//2
# res = str1[0:x] + str2 + str1[x::]
# print(res) 
# -------------------------------------------------------------------------------------------------
# # otp -> AJrpan
# str1 = "America"
# str2 = "Japan"
# x = len(str1)//2
# y = len(str2)//2
# res = str1[0] + str2[0] + str1[x] + str2[y::]
# print(res) 

# ----------------------------------------------------------------------------------------------------
# otp -> AzbycX

# str1 = 'Abc'
# str2 = 'Xyz'
# x = len(str1)//2
# y = len(str2)//2
# res = str1[0] + str2[-1] + str1[x] + str2[y] + str1[-1] + str2[0]
# print(res)

#---------------------------------------------------------------------------------------------------------

# otp -> azxcft

# str1 = 'abcdef'
# str2 = 'xyzst'
# x = len(str1)//2
# y = len(str2)//2
# res = str1[0] + str2[y] +str2[0] + str1[x] + str1[-1] + str2[-1]
# print(res)

# ------------------------------------------------------------------------------------------------------------
# Reverse a list
# l1 = [100, 200, 300, 400, 500]
# print(l1[::-1])

#-------------------------------------------------------------------------------------------------------------
#Add item 70 after 60 in the following List
# li = [10, 20, [30, 40, [50, 60], 80], 90, 100]
# li[2][2].append(70)
# print(li)
#-------------------------------------------------------------------------------------------------------------
# Given a nested list extend it with adding sub list ["h", "i", "j"] 
# in a such a way that it will look like the following list.
# #			Test Case: 
#                 Given List
#                     list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
#                 SubList to Add: 
#                     ["h", "i", "j"]
#                 Expected Output:
#                     ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
n = ["h","i","j"]
list1[2][1][2].extend(n)
print(list1)


# -----------------------------------------------------------------------------------------------------------------
# Q4. Given a Python list, find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value
# 			Test Case:
#                 Input : [5, 10, 15, 20, 25, 50, 20]
#                 Expected Output : [5, 10, 15, 200, 25, 50, 20]

# list1 = [5, 10, 15, 20, 25,[1,2,3]]
# print(list1[5])

# str = " Hasmukh"
# x = len(str)//2
# res = str[x-1] + str[x] +str[x+1]
# print(res)
# a = [1,2,8,9]
# b = [9,1]

# print(a<b)
a= int(1011,2)
print(a)