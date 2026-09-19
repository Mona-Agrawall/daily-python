def palindrome(s1):
    s1 = s1.lower()

    left = 0
    right = len(s1) - 1

    while left <= right:
        if s1[left] != s1[right]:
            return False

        left += 1
        right -= 1

    return True


s1 = "Nitin"

ans = palindrome(s1)
print(ans)