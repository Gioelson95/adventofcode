# 2/12/2023

import re

win_red = 12
win_green = 13
win_blue = 14

sum_1 = 0
sum_2 = 0

with open("2-12-23.txt") as f:
    lines = f.readlines()
    for s in lines:
        blue, red, green = 0, 0, 0
        game_id = int(re.search(r'\d+', s.split(":")[0]).group())
        games = s.split(":")[1].split(";")
        for game in games:
            game = game.split(",")
            for g in game:
                if "blue" in g:
                    b = int(re.search(r'\d+', g.split("blue")[0]).group())
                    if b > blue: blue = b
                if "red" in g:
                    r = int(re.search(r'\d+', g.split("red")[0]).group())
                    if r > red: red = r
                if "green" in g:
                    gr = int(re.search(r'\d+', g.split("green")[0]).group())
                    if gr > green: green = gr
        # part 1
        if blue <= win_blue and red <= win_red and green <= win_green: sum_1 = sum_1 + game_id
        # part 2
        sum_2 = sum_2 + blue*red*green

print(sum_1)
print(sum_2)
