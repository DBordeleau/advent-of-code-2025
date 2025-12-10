from z3 import *

def main():
    buttons = []
    joltage_counters = []

    with open("../input/day10_input") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            # parse buttons
            groups = []
            i = 0
            while i < len(line):
                if line[i] == '(':
                    j = line.index(')', i)
                    contents = line[i+1:j]
                    nums = tuple(int(n) for n in contents.split(','))
                    groups.append(nums)
                    i = j + 1
                # parse joltages
                elif line[i] == '{':
                    j = line.index('}', i)
                    contents = line[i+1:j]
                    joltages = [int(n) for n in contents.split(',')]
                    joltage_counters.append(joltages)
                    i = j + 1
                else:
                    i += 1

            buttons.append(groups)
    
    answer = solve_part2(joltage_counters, buttons)
    print(answer)
    
    #print(buttons)
    #print(indicator_lights)

def solve_part2(target_joltages, buttons):
    total_presses = 0
    for i, (target_joltages, buttons) in enumerate(zip(target_joltages, buttons)):
        presses = configure_joltage_counters(target_joltages, buttons)
        print(f"Machine {i}: solved with {presses} presses.")
        total_presses += presses
    return total_presses

# using z3 to solve as a linear system because none of my greedy BFS tricks were fast enough :(
def configure_joltage_counters(target_joltages, buttons):
    # count how many positions we have
    num_counters = len(target_joltages)
    num_buttons = len(buttons)
    
    # number of times each button is pressed
    button_presses = [Int(f'button_{i}') for i in range(num_buttons)]

    solver = Optimize()

    # button presses can't be negative
    for bp in button_presses:
        solver.add(bp >= 0)
    
    # for each counter sum of button presses must = target
    for counter_idx in range(num_counters):
        counter_sum = 0
        for btn_idx, button in enumerate(buttons):
            if counter_idx in button:
                counter_sum += button_presses[btn_idx]
        solver.add(counter_sum == target_joltages[counter_idx])
    
    total_presses = sum(button_presses)
    solver.minimize(total_presses)
    
    if solver.check() == sat:
        model = solver.model()
        result = sum(model[bp].as_long() for bp in button_presses)
        return result
    else:
        return -1  # if this happens I give up

if __name__ == "__main__":
    main()