from aoc_input_call import get_aoc_input
from aoc_25_05 import unite_iv

data = get_aoc_input(2025, 5)

split_data = data.index("")

ranges = data[:split_data]

intervals = unite_iv(ranges)

total_in_intervals = sum(e - s + 1 for s, e in intervals)

print("Quantity of fresh ID's:", total_in_intervals)