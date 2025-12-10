from collections import deque

def main():
    indicator_lights = []
    buttons = []
    with open("../input/day10_input") as f:
        for line in f:
            line = line.strip()

            # parse indicator lights as tuplies indicating the positions we need turned on
            # so [..#.#] becomes (2, 4)
            start = line.index('[') + 1
            end = line.index(']')
            pattern = line[start:end]

            positions = tuple(i for i, ch in enumerate(pattern) if ch == '#')
            indicator_lights.append(positions)

            # parse button lists so that buttons[n] = all buttons for the nth machine
            groups = []
            i = end + 1
            while i < len(line):
                if line[i] == '(':
                    j = line.index(')', i)
                    contents = line[i+1 : j] 
                    nums = tuple(int(n) for n in contents.split(','))
                    groups.append(nums)
                    i = j + 1
                # ignore curly brackets for now
                elif line[i] == '{':
                    j = line.index('}', i)
                    i = j + 1
                else:
                    i += 1

            buttons.append(groups)
    
    answer = solve_part1(indicator_lights, buttons)
    print(answer)
    
    #print(buttons)
    #print(indicator_lights)

def solve_part1(indicator_lights, buttons):
    total_presses = 0
    for i, (target, machine_buttons) in enumerate(zip(indicator_lights, buttons)):
        presses = solve_machine(target, machine_buttons)
        print(f"Machine {i}: solved with {presses} presses.")
        total_presses += presses
    return total_presses

# bfs finds minimum num of button presses to light exactly the target lights
def solve_machine(target_lights, buttons):
    # start with all lights off
    queue = deque([(tuple(), 0)]) 
    visited = {tuple()}
    
    while queue:
        current_state, presses = queue.popleft()
        
        # done
        if current_state == target_lights:
            return presses
        
        # try every button and add it to the queue if not already seen
        for button in buttons:
            new_state = set(current_state)
            for pos in button:
                if pos in new_state: # toggle off
                    new_state.remove(pos)  
                else: # toggle on
                    new_state.add(pos)     
            
            new_state = tuple(sorted(new_state))
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, presses + 1))
    
    return -1  # this should never happen if I did this right

if __name__ == "__main__":
    main()