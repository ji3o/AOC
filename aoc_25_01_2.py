from aoc_input_call import get_aoc_input

def process_instructions(instructions):
    
    position = 50
    list_size = 100
    counter = 0
    
    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        
        if direction == 'L':
            for step in range(steps):
                position = (position - 1) % list_size
                if position == 0:
                    counter += 1
        elif direction == 'R':
            for step in range(steps):
                position = (position + 1) % list_size
                if position == 0:
                    counter += 1
    
    return position, counter

data = get_aoc_input(2025, 1)
instructions = [line.strip() for line in data if line.strip()]

final_position, count = process_instructions(instructions)
print(f"Final position: {final_position}")
print(f"Counter: {count}")
