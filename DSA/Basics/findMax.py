def findMax(arr):
    max_value = arr[0]
    max_index = 0
    
    for i in range(len(arr)):
        if(arr[i] > max_value):
            max_value = arr[i]
            max_index = i
            
    return max_value, max_index


arr = [12,18,3,14,90,81,72]

result = findMax(arr)

print(result[0])
print(result[1])