from aoc_input_call import get_aoc_input

data = get_aoc_input(2025, 2)
# print(data)

def is_doubleseq(n: int) -> bool:
    s = str(n)
    if len(s) % 2 != 0:
        return False
    half = len(s) // 2
    return s[:half] == s[half:]

def process_instruction(lines):
    for line in lines:
        for part in line.split(","):
            part = part.strip()
            if not part:
                continue
            start_str, end_str = part.split("-")
            yield int(start_str), int(end_str)


def find_doubleseq(lines):
    result = []
    for start, end in process_instruction(lines):
        for n in range(start, end + 1):
            if is_doubleseq(n):
                result.append(n)
    return result


doubleseq = find_doubleseq(data)
sum = sum(doubleseq)

print("Count:", len(doubleseq))
print("Sum:", sum)
