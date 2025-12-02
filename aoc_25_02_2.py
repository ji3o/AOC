from aoc_input_call import get_aoc_input

data = get_aoc_input(2025, 2)


def is_repeated_pattern(n: int) -> bool:
    s = str(n)
    length = len(s)
    for k in range(1, length // 2 + 1):
        if length % k != 0:
            continue
        block = s[:k]
        if block * (length // k) == s:
            return True
    return False


def process_instruction(lines):
    for line in lines:
        for part in line.split(","):
            part = part.strip()
            if not part:
                continue
            start_str, end_str = part.split("-")
            yield int(start_str), int(end_str)


def find_repeated_patterns(lines):
    result = []
    for start, end in process_instruction(lines):
        for n in range(start, end + 1):
            if is_repeated_pattern(n):
                result.append(n)
    return result


numbers = find_repeated_patterns(data)
total = sum(numbers)

print("Count:", len(numbers))
print("Sum:", total)
