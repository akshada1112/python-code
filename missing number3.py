numbers = [1, 2, 4, 6, 3, 7, 8]
n = 8

expected_sum = n * (n + 1) // 2

actual_sum = 0

for num in numbers:
    actual_sum += num

missing = expected_sum - actual_sum

print(missing)
