# https://adventofcode.com/2023/day/1

### PART 1 ###
# for each line take first and last digit to form 2-digit number.
# sum of values?
# ex.
# 1abc2 -> 12
# pqr3stu8vwx -> 38
# a1b2c3d4e5f -> 15
# treb7uchet -> 77
# sum = 142

### PART 2 ###
# some digits are spelled with letters, "one", "two", etc. (no "zero")
# which count as valid digits.
# sum of values?
# ex.
# two1nine -> 29
# eightwothree -> 83
# abcone2threexyz -> 13
# xtwone3four -> 24
# 4nineeightseven2 -> 42
# zoneight234 -> 14
# 7pqrstsixteen -> 76
# sum = 281

# pip3 install advent-of-code-data
from aocd import data

year = 2023
day = 1

