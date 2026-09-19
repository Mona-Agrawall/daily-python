def find_peak(arr):
    n = len(arr)

    for i in range(n):
        if i > 0 and arr[i] < arr[i-1]:
            continue
        if i < n-1 and arr[i] < arr[i+1]:
            continue
        return i;

    return -1


arr = [5, 10, 20, 15, 7]

print(find_peak(arr))