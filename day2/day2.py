def get_invalid_ids(ranges):
    invalids = []
    for range_string in ranges:
        start, end = range_string.split("-")
        start = int(start)
        end = int(end)

        # Anything with a leading 0 is an invalid id
        # Any number comprised of a repeating sequence of digits e.g: 4567845678, 55, 111, 333333
        for num in range(start, end+1):
            num_str = str(num)
            
            # starts with 0
            if num_str.startswith("0"):
                invalids.append(num)
                continue

            # check if comprised only of repeating digits
            double_num_str = num_str + num_str # double the string so 789789 becomes 789789789789
            double_num_str = double_num_str[1:-1] # remove first and last digit

            # if the original string is still in the doubled string after removing first and last digits, its comprised of only repeating digit sequence
            if num_str in double_num_str:
                invalids.append(num)

    return invalids

def main():
    with open("../input/day2_input") as f:
        input_string = f.read()
        ranges = input_string.split(",")
        print(ranges)
        invalid_ids = get_invalid_ids(ranges)
        answer = sum(invalid_ids)
        print(answer)

if __name__ == "__main__":
    main()