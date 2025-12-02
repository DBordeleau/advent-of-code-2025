def process_instructions(instructions):
    current = 50
    zero_count = 0

    for instruction in instructions:
        direction = instruction[0]
        steps = int(instruction[1:])
        print(direction)
        print(steps)

        # turning left
        if direction == 'L':
            to_zero = current

            # Check if we will reach zero
            if steps >= to_zero and to_zero > 0:
                zero_count += 1
                steps -= to_zero
                current = 0

            # Count how many times we can fully wrap back around to zero
            while steps >= 100:
                zero_count += 1
                steps -= 100

            # final position
            current = (current - steps) % 100
    
        # turning right
        elif direction == 'R':
            to_zero = (100 - current) % 100 # %100 so if current = 0, to_zero = 0

            # Check if we are going to reach zero (and aren't starting at 0)
            if steps >= to_zero and to_zero > 0:
                zero_count += 1
                steps -= to_zero
                current = 0

            # Count how many times we can fully wrap around to zero
            while steps >= 100:
                zero_count += 1
                steps -= 100

            # Final position
            current = (current + steps) % 100

        
    return zero_count
    

def main():
    with open("../input/day1_input") as f:
        instructions = f.readlines()
    
    password = process_instructions(instructions)
    print(password)

if __name__ == "__main__":
    main()