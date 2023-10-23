def first3largest(arr,n):
    first = second = third = -1
    if n < 3:
        print("Invalid")
        return -1
    for i in arr:
        if i > first:
            third = second
            second = first
            first = i
        elif i>second and i != first:
            third = second
            second = i
        elif i>third and i!= second and i != first:
            third =i
    print(f"First = {first}\nSecond = {second}\nThird = {third}")
arr = [12,10,30,40,12]
n = len(arr)
first3largest(arr,n)
