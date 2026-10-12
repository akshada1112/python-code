def are_anagrams(first, second):
    if len(first) != len(second):
        return False

    frequency = {}

    for char in first:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    for char in second:
        if char not in frequency:
            return False

        frequency[char] -= 1

        if frequency[char] < 0:
            return False

    return True


first = "listen"
second = "silent"

print(are_anagrams(first, second))