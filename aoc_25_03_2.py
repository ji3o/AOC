from aoc_input_call import get_aoc_input

data = get_aoc_input(2025, 3)

def max_subsequence_number(line: str, k: int) -> int:

    digits = [int(c) for c in line.strip()]
    n = len(digits)

    chosen = []
    start = 0
    
    for pos in range(k):
        remaining_positions = k - pos
        last_start = n - remaining_positions

        best_digit = -1
        best_index = -1

        for i in range(start, last_start + 1):
            d = digits[i]
            if d > best_digit:
                best_digit = d
                best_index = i
                if best_digit == 9:
                    break

        chosen.append(best_digit)
        start = best_index + 1

    return int("".join(str(d) for d in chosen))


results = [max_subsequence_number(line, 12) for line in data]
total = sum(results)

print("Sum:", total)
