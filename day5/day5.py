def count_fresh_ingredients_part1(ranges: list[tuple[int, int]], ingredient_ids: list[int]) -> int:
    fresh_ingredient_count = 0

    for id in ingredient_ids:
        for start, end in ranges:
            if start <= id <= end: # inclusive check
                fresh_ingredient_count += 1
                break
    return fresh_ingredient_count

def combine_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
    # start with just the first range
    combined_ranges = [list(ranges[0])]

    # check every range against the last combined range
    for start, end in ranges[1:]:
        last_combined_end = combined_ranges[-1][1]

        # if the next range begins with a smaller number, combine the ranges
        if start <= last_combined_end + 1:
            combined_ranges[-1][1] = max(last_combined_end, end) # ONLY OVERWRITE THE END OF THE LAST RANGE IF THIS ONE ACTUALLY EXTENDS IT DUMMY
        else: # otherwise just add this as a new range
            combined_ranges.append([start, end])

    # convert back to tuples so I don't have to modify the solve function
    return [(start, end) for start, end in combined_ranges]

def count_fresh_ingredients_part2(ranges: list[tuple[int, int]]) -> int:
    # we have to combine ranges that overlap otherwise we will overcount
    ranges = sorted(ranges)
    combined_ranges = combine_ranges(ranges)
    
    fresh_ingredient_count = 0

    for start, end in combined_ranges:
        fresh_ingredient_count += end - start + 1 # +1 cause inclusive

    return fresh_ingredient_count

def main():
    with open("../input/day5_input") as f:
        lines = f.read().splitlines()

    blank_line_idx = lines.index("")

    range_lines = lines[:blank_line_idx]
    id_lines = lines[blank_line_idx + 1:]

    # Map ranges to tuples where first entry is start and second entry is end
    ranges = [tuple(map(int, line.split("-"))) for line in range_lines]

    # Convert ingredient IDs to numbers
    ingredient_ids = [int(n) for n in id_lines]

    fresh_ingredient_count = count_fresh_ingredients_part2(ranges)
    print(fresh_ingredient_count)

if __name__ == "__main__":
    main()