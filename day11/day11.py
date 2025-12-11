from collections import deque

def main():
    # machine -> list of machines it outputs to
    machine_map = {}
    with open("../input/day11_input") as f:
        for line in f:
            machines = line.split()
            machines[0] = machines[0].rstrip(":")
            machine_map[machines[0]] = machines[1:]

    # paths = find_paths(machine_map)

    count = count_paths_p2(machine_map)    
    print(count)

def count_paths_p2(machine_map):
    # get nodes that can reach fft/dac/out
    can_reach_fft = get_reachable(machine_map, "fft")
    can_reach_dac = get_reachable(machine_map, "dac")
    can_reach_out = get_reachable(machine_map, "out")

    # store all seen states: state -> number of valid paths
    seen_states = {}

    def count(node, has_fft, has_dac, visited):
        # create key for this state
        # DONT INCLUDE THE VISITED SET IN THE DICT KEY ONLY USE IT TO PREVENT RECURSION INTO CYCLES
        state = (node, has_fft, has_dac)

        if state in seen_states:
            return seen_states[state]

        # store whether this is a valid path as the value in the dict
        if node == "out":
            result = 1 if (has_fft and has_dac) else 0  # 1 valid path or 0 not true/false
            seen_states[state] = result
            return result
        
        # if it can't reach out, or it cant reach dac/fft when we need it, that shit is dead to us
        if node not in can_reach_out:
            seen_states[state] = 0
            return 0
        if not has_dac and node not in can_reach_dac:
            seen_states[state] = 0
            return 0
        if not has_fft and node not in can_reach_fft:
            seen_states[state] = 0
            return 0
        
        total = 0
        for output in machine_map[node]:
            if output not in visited: # don't recurse into a cycle
                # there is probably a better way to write this but idc
                new_has_fft = has_fft or (output == "fft")
                new_has_dac = has_dac or (output == "dac")
                new_visited = visited | {output}
                total += count(output, new_has_fft, new_has_dac, new_visited)

        # dont forget to store the result christ
        seen_states[state] = total
        return total
    
    return count("svr", False, False, set(["svr"]))

# bfs that returns a set of all nodes that can reach fft and dac using a reversed graph
def get_reachable(machine_map, target):
    reverse_map = {}
    # build the reversed graph
    for node, outputs in machine_map.items():
        for output in outputs:
            if output not in reverse_map:
                reverse_map[output] = []
            reverse_map[output].append(node)

    # bfs backward from target
    reachable = set()
    queue = deque([target])
    visited = {target}

    while queue:
        node = queue.popleft()
        reachable.add(node)
        
        if node in reverse_map: # some nodes have no incoming edges in reverse map
            for output in reverse_map[node]:
                if output not in visited:
                    visited.add(output)
                    queue.append(output)
    
    return reachable

# this was still too slow have to try something else
# # optimized bfs that kills branches early if they can't reach fft/dac
# def find_paths_p2(machine_map):
#     # find all nodes that can reach fft, dac and out
#     can_reach_fft = get_reachable(machine_map, "fft")
#     can_reach_dac = get_reachable(machine_map, "dac")
#     can_reach_out = get_reachable(machine_map, "out")

#     paths = []
#     queue = deque([["svr"]])

#     while queue:
#         current_path = queue.popleft()
#         last_node = current_path[-1]

#         if last_node == "out":
#             if "fft" in current_path and "dac" in current_path:
#                 paths.append(current_path)
#             continue

#         # check if fft/dac/out are reachable
#         # ONLY CHECK FOR FFT/DAC IF WE NEED IT
#         if last_node not in can_reach_out:
#             continue
#         if "fft" not in current_path and last_node not in can_reach_fft:
#             continue
#         if "dac" not in current_path and last_node not in can_reach_dac:
#             continue

#         for output in machine_map[last_node]:
#             if output not in current_path:
#                 new_path = list(current_path)
#                 new_path.append(output)
#                 queue.append(new_path)
    
#     return paths

# bfs to find all paths from 'you' to 'out' for p1
def find_paths(machine_map):
    paths = []

    queue = deque([["you"]])
    
    while queue:
        current_path = queue.popleft()
        last_node = current_path[-1]

        if last_node == "out":
            paths.append(current_path)
            continue

        for output in machine_map[last_node]:
            if output not in current_path:
                new_path = list(current_path)
                new_path.append(output)
                queue.append(new_path)
    
    return paths

if __name__ == "__main__":
    main()