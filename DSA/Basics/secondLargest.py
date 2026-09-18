def small_large_sum(arr):
    
    if(len(arr) <= 3):
        return 0
    
    arr1 = []
    arr2 = []
    
    
    for i in range(len(arr)):
        if(i % 2 == 0):
            arr1.append(arr[i])
        else:
            arr2.append(arr[i])
            
    arr1.sort(reverse = True)
    arr2.sort(reverse = True)
    
    sec1 = arr1[1]
    sec2 = arr2[1]
    
    sum = sec1 + sec2
    
    return sum

arr = [12,78,2,11,31,44,21,90]

sum = small_large_sum(arr)

print(sum)