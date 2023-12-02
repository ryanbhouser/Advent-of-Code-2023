import re
import numpy

# Get games from day_2_input.txt
with open("day_2_input.txt", "r") as file:
    lines = file.readlines()
    games = [line.rstrip() for line in lines]

# Init answers
part_1_answer = 0
part_2_answer = 0

for game in games:
    reds = []
    greens = []
    blues = []
    split = re.split(":|;", game) # splits each game into its own list element
    
    # PART ONE
    for s in split:
        # Search for and append number of each color's cube to its respective list
        pattern = re.compile(r".*?(\d+)\s+red.*?")
        match = pattern.match(s)
        if match:
            reds.append(int(match.group(1)))

        pattern = re.compile(r".*?(\d+)\s+green.*?")
        match = pattern.match(s)
        if match:
            greens.append(int(match.group(1)))

        pattern = re.compile(r".*?(\d+)\s+blue.*?")
        match = pattern.match(s)
        if match:
            blues.append(int(match.group(1)))

    # If number of blocks satisifes game rules, then get game number and add it to the part_1_answer variable
    # Rules: Which games are possible if there are only 12 red cubes, 13 green cubes, and 14 blue cubes
    if max(reds, default=0) <=12 and max(greens, default=0) <=13 and max(blues, default=0) <= 14:
        part_1_answer += (int(split[0].replace("Game ", "")))

    # PART TWO
    # Get the max number of each color's cube and append it to a powers array
    powers = []
    powers.append(max(reds))
    powers.append(max(greens))
    powers.append(max(blues))

    # Add the product of powers to the part_2_answer variable
    part_2_answer += numpy.prod(powers)

print(part_1_answer) # 2149

print(part_2_answer) # 71274