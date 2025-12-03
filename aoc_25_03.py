from aoc_input_call import get_aoc_input

data = get_aoc_input(2025, 3)

def highest_two_digit(line: str) -> int:

    digits = [int(c) for c in line]
    n = len(digits)
    best = -1

    for i in range(n - 1):
        tens = digits[i]

        max_right = -1
        for j in range(i + 1, n):
            if digits[j] > max_right:
                max_right = digits[j]

        if max_right >= 0:
            number = tens * 10 + max_right
            if number > best:
                best = number

    return best


results = [highest_two_digit(line) for line in data]
total = sum(results)

print("Sum:", total)