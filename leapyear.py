''' QUES 1.)Write a program to check that given year is leap year,
or not'''

# year = int(input("Enter the year --->  "))
# if year%4==0 and year%400==0 or year%100!=0:
# 	print(f"[--> {year} is a leap year <--]")
# else:
# 	print(f"[--> {year} is not a leap year <--]")

# ----------------------------------------------------------------------------------------------------------
''' QUES 2.) Write a program to check that a given integer is prime number or not '''

# n = int(input("Enter any integer --> "))
# if n%n==0 :
#      print(f"{n} is not a prime number")
# else:
#      print(f"{n} is a prime number")

# -------------------------------------------------------------------------------------------------------------
''' QUES 3.) Write a program to output : x + xx + xxx + xxxx , x(digit) is given by user'''
n = input()
series = int(n) + int(n)*10 + int(n) + int(n)*100 + int(n)*10 + int(n)
print(series)

