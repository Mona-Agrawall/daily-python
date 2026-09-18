def nonDuplicate(arr):
    freq = {}
    
    for num in arr:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1
            
    for num in freq:
        if(freq[num] == 1):
            return num
        
        
arr = [1,1,2,1,2,3,4,3,5,5,3]

new = nonDuplicate(arr)
print(new)