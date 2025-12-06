def main():
    with open("../input/day6_input") as f:
        lines = [line.rstrip("\n") for line in f]
    
    # the last line contains operators and the first 4 lines contain numbers
    operator_line = lines[-1]
    number_lines = lines[:-1]

    # track the current column we're at
    col = 0
    answer = 0

    # continue until all problems are processed
    while col < len(operator_line):
        # skip spaces in operator line to find next operator
        while col < len(operator_line) and operator_line[col] == ' ':
            col += 1
        # check if we are done
        if col >= len(operator_line):
            break

        # remember where this problem starts for when we parse the next operator
        problem_start_col = col

        # parse numbers for this problem
        problem_numbers = []

        # continue reading columns until we hit a separator (column of all spaces)
        while col < len(operator_line):
            is_separator = all(col >= len(number_lines[row]) or number_lines[row][col] == ' ' 
                             for row in range(len(number_lines))) and operator_line[col] == ' '
            
            if is_separator:
                break
            
            # read number vertically from this column
            num_str = ""
            for row in range(len(number_lines)):
                if col < len(number_lines[row]) and number_lines[row][col] != ' ':
                    num_str += number_lines[row][col]
            
            # add the number to the current list of numbers for this problem
            if num_str:
                problem_numbers.append(int(num_str))
            
            col += 1

        # get operator from the start of this problem
        operator = operator_line[problem_start_col]

        # calculate current problem
        if operator == '+':
            result = sum(problem_numbers)
        elif operator == '*':
            result = 1
            for num in problem_numbers:
                result *= num
        elif operator == '-':
            result = problem_numbers[0]
            for num in problem_numbers[1:]:
                result -= num
        else:
            result = 0
        
        answer += result

    print(answer)

if __name__ == "__main__":
    main()