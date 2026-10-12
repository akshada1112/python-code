def process_numbers(numbers):
    total = 0
    count = 0
    largest = None

    for num in numbers:
        if num >= 0 and num % 2 == 0:
            square = num * num

            total += square
            count += 1

            if largest is None or square > largest:
                largest = square

    if count == 0:
        return total, count, None

    return total, count, largest


numbers = [-2, 1, 2, 3, 4, 6, -8]

total, count, largest = process_numbers(numbers)

print("Total:", total)
print("Count:", count)
print("Largest squared value:", largest)