numbers = [12, 35, 1, 10, 34, 35]

largest = None
second_largest = None

for num in numbers:
    if largest is None or num > largest:
        second_largest = largest
        largest = num
    elif num != largest and (second_largest is None or num > second_largest):
        second_largest = num

if second_largest is None:
    print("No second-largest distinct value")
else:
    print(second_largest)