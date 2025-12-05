from aoc_input_call import get_aoc_input

def unite_iv(lines):
    intervals = []
    for line in lines:
        line = line.strip()
        start_str, end_str = line.split("-")
        start = int(start_str)
        end = int(end_str)
        if start > end:
            start, end = end, start
        intervals.append((start, end))

    intervals.sort()
    merged = []
    for s, e in intervals:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            if e > merged[-1][1]:
                merged[-1][1] = e

    return [(s, e) for s, e in merged]

def parse_numbers(lines):
    nums = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        nums.append(int(line))
    return sorted(nums)

if __name__ == "__main__":
    data = get_aoc_input(2025, 5)
    split_data = data.index("")

    ranges = data[:split_data]
    numbers = data[split_data + 1:]

    intervals = unite_iv(ranges)
    numbers = parse_numbers(numbers)

    i = 0
    j = 0
    count = 0

    while i < len(intervals) and j < len(numbers):
        s, e = intervals[i]
        x = numbers[j]

        if x < s:
            j += 1
        elif x > e:
            i += 1
        else:
            count += 1
            j += 1

    print("ID's in ranges:", count)
