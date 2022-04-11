
# # username = input("Enter your username: ").lower()
# # password = input("Enter your password: ")

# # if username in user and password == user_data[username]:
# #     print(f"Welcome {username}")
# # else:
# #     print("Wrong credentials")

# # username = input("Enter your username").lower()
# # if username in user:
# #     password = input("Enter your password")
# #     if password==user_data[username]:
# #         print(f"Welcome {username}")
# #     else:
# #         print("Wrong password")
# # else:
# #     print("Wrong username")

# user = ['john','sam','mac']
# user_data = {'john':'123456','sam':'147','mac':'abcd'}
# user_depth ={'HR':['john'],'PUR': ['sam','mac']}
# username = input("Enter your username : ").lower()
# if username in user:
#     password = input("Enter Your Password : ")
#     print("Departments -->\n 1. HR \n 2. PUR \n 3. ACC")
    
#     if password == user_data[username]:
#         print(f"Welcome {username} choose your department-->")
#         dept = input("Enter your department : ").upper()
      
        
#         if dept == "HR"and username in user_depth[dept]:
#             print(f"Welcome {username} in HR department")
        
        

#         elif dept == "PUR" and username in user_depth[dept]:
#              print(f"Welcome {username} in PURCHASE department")
        

        

#         elif dept == "ACC" and username in user_depth[dept]:
#              print("Welcome in ACCOUNT department")
        
#         else:
#             print(f" {username} not a valid user")
        
# #     else:
# #        print("Wrong password")
# # else:
# #     print("Wrong Username")
# sum =0.5
# for i in range(5):
#     if i %2 ==0:
#         sum=int(sum+i)
#         print("even",sum)
#     else:
#         sum+=i
#         print("odd",sum)
# print(sum)
# 
# n=0
# while n!=12:
#     print(n,end='')
#     n+=5

# for i in range(5):
#     print(sum,"+","sum","=",(sum+sum))
#     sum=sum+sum
# x='abcd'
# for i in range(len(x)):
#     x='a'
#     print(x)

# i=1
# while True:
#     print(i)
#     i+=2
sum=0
al =True
for number in range(101):
    if number%2==0:
        continue
    if al==True:
        sum+=number
        al=False
        continue
    al = True
print(sum)