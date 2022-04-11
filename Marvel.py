def marvel(arr):
    l=len(arr)
    print(arr)
    arr.append("Black panther")
    print(arr)
    arr.remove("Hulk")
    print(arr)
    arr.remove("Black panther")
    print(arr)
    arr[1:3]=["Doctor Strange"]
    print(arr)
    
arr=["Spider man","Thor","Hulk","Iron man","Captain America"]
print(marvel(arr))
    