import string

with open("input.txt", "r") as f:
    data = f.read().splitlines()

digits = [
    [
        num
        for num in map(lambda x: x if x in string.digits else None, line)
        if num is not None
    ]
    for line in data
]
print("Part 1:", sum([int(dlist[0] + dlist[-1]) for dlist in digits]))

p2_valid_digits = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    **{digit: int(digit) for digit in string.digits}
}

calibration_values = []
for line in data:
    first_orders = [(digit, line.find(digit)) for digit in p2_valid_digits.keys() if line.find(digit) != -1]
    last_orders = [(digit, line.rfind(digit)) for digit in p2_valid_digits.keys() if line.rfind(digit) != -1]
    first = p2_valid_digits[sorted([digit for digit in first_orders], key=lambda x: x[1])[0][0]] * 10
    last = p2_valid_digits[sorted([digit for digit in last_orders], key=lambda x: x[1], reverse=True)[0][0]]
    calibration_values.append(first + last)

print("Part 2:", sum(calibration_values))
