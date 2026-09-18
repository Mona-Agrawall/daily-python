def missing_number(arr):
    n = len(arr)

    expected = (n + 1) * (n + 2) // 2

    actual = 0

    for num in arr:
        actual = actual + num

    return expected - actual


arr = [1, 2, 4, 5, 6]

print(missing_number(arr))