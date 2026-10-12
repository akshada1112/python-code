numbers = [1, 1, 2, 2, 2, 3, 3, 1, 1, 1, 1]

if len(numbers) == 0:
    print(0)
else:
    current_count = 1
    maximum_count = 1

    for i in range(1, len(numbers)):
        if numbers[i] == numbers[i - 1]:
            current_count += 1
        else:
            current_count = 1

        if current_count > maximum_count:
            maximum_count = current_count

    print(maximum_count)