from aoc_input_call import get_aoc_input

def process_instructions(instructions, start=50, list_size=100):
    
    position = start
    counter = 0
    
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        
        if direction == 'L':
            position = (position - steps) % list_size
        elif direction == 'R':
            position = (position + steps) % list_size
        
        if position == 0:
            counter += 1
    
    return position, counter

data = get_aoc_input(2025, 1)

final_position, count = process_instructions(data)
print(f"Final position: {final_position}")
print(f"Counter (times at 0): {count}")
