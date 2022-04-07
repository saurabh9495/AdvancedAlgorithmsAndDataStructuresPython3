def find_minimum(arr):
    if (len(arr) <= 0):
        return None
    minimum = arr[0] 
    for i in arr:
        if minimum > i:
            minimum = i
    return minimum

print(find_minimum([100, 12, 34, 40]))