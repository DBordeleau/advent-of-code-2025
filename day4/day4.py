def walk_and_count(grid: list[list], answer: int) -> int:
    moved_tp = False
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '.':
                continue
            if grid[row][col] == '@':
                if count_adjacent(grid, row, col) < 4:
                    grid[row][col] = 'x'
                    moved_tp = True
                    answer += 1
                    continue
    
    if moved_tp:
        return walk_and_count(grid, answer)
    return answer


def count_adjacent(grid: list[list], row: int, col: int) -> int:
    directions = [(1,0), (1,1), (1,-1), (-1,0), (-1,1), (-1,-1), (0,1), (0,-1)]
    count = 0

    for dr, dc in directions:
        new_row, new_col = row + dr, col + dc
        if check_bounds(grid, (new_row, new_col)):
            if grid[new_row][new_col] == '@':
                count += 1
                continue
    return count


def check_bounds(grid: list[list], coords: tuple[int, int]) -> bool:
    return 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])

def main():
    with open("../input/day4_input") as f:
        grid = [list(line.rstrip("\n")) for line in f] # parse as a list of lists so we can modify individual characters
    
    answer = walk_and_count(grid, 0)
    print(answer)

if __name__ == "__main__":
    main()