def get_max_joltages(battery_banks):
    max_joltages = []
    for battery_bank in battery_banks:
        battery_bank = battery_bank.strip()
        max_seen = "0"
        max_seen_idx = 0
        first_digit = 0
        second_digit = 0
        broke_early = False

        # find the largest digit before the last, if we find 9 break immediately since 9 is the largest possible digit
        for i in range(len(battery_bank) - 1):
            if battery_bank[i] == '9':
                first_digit = '9'
                second_digit = max(battery_bank[i+1:])
                broke_early = True
                break
            if battery_bank[i] > max_seen:
                max_seen = battery_bank[i]
                max_seen_idx = i
            
        if not broke_early:
            first_digit = max_seen
            second_digit = max(battery_bank[max_seen_idx + 1:])
            
        max_joltages.append(int(first_digit + second_digit))
    return max_joltages

def get_max_joltages_part_2(battery_banks):
    max_joltages = []
    for battery_bank in battery_banks:
        digits = []
        battery_bank = battery_bank.strip()

        next_idx = 0

        # find 12 digits
        while len(digits) < 12:
            max_seen_digit = '0'
            broke_early = False
            digits_to_find = 11 - len(digits)
            for i in range(next_idx, len(battery_bank) - digits_to_find):
                if battery_bank[i] == '9':
                    digits.append('9')
                    next_idx = i + 1
                    broke_early = True
                    break

                if battery_bank[i] > max_seen_digit:
                    max_seen_digit = battery_bank[i]
                    next_idx = i + 1
            
            if not broke_early:
                digits.append(max_seen_digit)
        
        # print(battery_bank)
        # print(digits)
        max_joltages.append(int(''.join(digits)))
    
    return max_joltages

def main():
    with open("../input/day3_input") as f:
        battery_banks = f.readlines()
    
    max_joltages = get_max_joltages_part_2(battery_banks)
    print(sum(max_joltages))

if __name__ == "__main__":
    main()