''''arr=[2200,2350,2600,2130,2190]
print("Extra expenses comapare to jan",arr[1]-arr[0])
print("Total expenses in first quarter",arr[0]+arr[1]+arr[2])
arr.append(1980)
print("Expenses at the end of the june",arr)
arr[3]=arr[3]-200
print("Expenses after 200$ retun in april",arr)'''

"""def  expenses(arr):
    print("Extra exepsnes compare to jan",arr[1]-arr[0])
    print("Total expenses in the first quarter",arr[0]+arr[1]+arr[2])
    arr.append(1980)
    print("Expences at the end of the june",arr)
    arr[3]=arr[3]-200
    print("Expenses after 200$ return in april",arr)
    return arr
arr=[2200,2350,2600,2130,2190]
print(expenses(arr)) """




import numpy as np
arr=[1,2,3,4]
a=np.array(arr)
print(a)