def mean(numbers):
    return sum(numbers) / len(numbers)


def median(numbers):
    values = sorted(numbers)
    middle = len(values) // 2
    if len(values) % 2 == 0:
        return (values[middle - 1] + values[middle]) / 2
    return values[middle]


def mode(numbers):
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    return max(counts, key=counts.get)
