
import re

# Get codes from day_1_input.txt
with open("day_1_input.txt", "r") as file:
    lines = file.readlines()
    codes = [line.rstrip() for line in lines]

# PART ONE
# ========
digits_part1 = []
for code in codes:
    # strip non-numeric characters
    digit_strip = re.sub("[^0-9]", "", code)

    # append converted int of first and last numeric string character
    digits_part1.append(int(digit_strip[0] + digit_strip[-1]))

print(sum(digits_part1))  # 55621

# PART TWO
# ========
digits_part2 = []
for code in codes:
    # convert string numbers into a modified string containing first char, number, and last char. This preserves letters if two numbers share characters (ex: eightwo)
    code = code.replace("one", "o1e")
    code = code.replace("two", "t2o")
    code = code.replace("three", "t3e")
    code = code.replace("four", "f4r")
    code = code.replace("five", "f5e")
    code = code.replace("six", "s6x")
    code = code.replace("seven", "s7n")
    code = code.replace("eight", "e8t")
    code = code.replace("nine", "n9e")
    # strip non-numeric characters
    code = re.sub("[^0-9]", "", code)

    # append converted int of first and last numeric string character
    digits_part2.append(int(code[0] + code[-1]))

print(sum(digits_part2))  # 53592
