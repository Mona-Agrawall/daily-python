def is_anagram(s1, s2):
    freq1 = {}
    freq2 = {}

    for i in s1:
        if i in freq1:
            freq1[i] += 1
        else:
            freq1[i] = 1

    for i in s2:
        if i in freq2:
            freq2[i] += 1
        else:
            freq2[i] = 1

    if freq1 == freq2:
        return True

    return False


print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))    # False