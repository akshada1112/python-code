def analyze_marks(*args):
    if len(args) == 0:
        print("No marks provided")
        return

    total = 0
    highest = args[0]
    passing_count = 0

    for mark in args:
        total += mark

        if mark > highest:
            highest = mark

        if mark >= 40:
            passing_count += 1

    average = total / len(args)

    print("Total:", total)
    print("Average:", average)
    print("Highest:", highest)
    print("Passing count:", passing_count)


analyze_marks(35, 72, 80, 45, 90, 30)