def main():
    with open("../input/day6_input") as f:
        lines = [line.rstrip("\n") for line in f]
    
    # the last line contains operators and the first 4 lines contain numbers
    operator_line = lines[-1]
    number_lines = lines[:-1]

    # track the last index we parsed at for each line
    indices = [0, 0, 0, 0]
    operator_idx = 0
    answer = 0

    # continue until all problems are processed
    while operator_idx < len(operator_line):
        # skip spaces in operator line to find next operator
        while operator_idx < len(operator_line) and operator_line[operator_idx] == ' ':
            operator_idx += 1
        # check if we are done
        if operator_idx >= len(operator_line):
            break

        # parse one number from each of the 4 lines for the current problem
        problem_numbers = []

        for line_idx in range(4):
            # skip leading spaces
            while indices[line_idx] < len(number_lines[line_idx]) and number_lines[line_idx][indices[line_idx]] == ' ':
                indices[line_idx] += 1
            
            # parse the number, if we see a space now we are done
            cur_num_str = ""
            while indices[line_idx] < len(number_lines[line_idx]) and number_lines[line_idx][indices[line_idx]] != ' ': 
                cur_num_str += number_lines[line_idx][indices[line_idx]]
                indices[line_idx] += 1
            
            # add the number to the current list of numbers for this problem
            if cur_num_str:
                problem_numbers.append(int(cur_num_str))

        # get operator
        operator = operator_line[operator_idx]
        operator_idx += 1

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
        
        answer += result

    print(answer)

if __name__ == "__main__":
    main()