numbers_to_words = {
    0: 0,
    1: 3,
    2: 3,
    3: 5,
    4: 4,
    5: 4,
    6: 3,
    7: 5,
    8: 5,
    9: 4,
    10: 3,
    11: 6,
    12: 6,
    13: 8,
    14: 8,
    15: 7,
    16: 7,
    17: 9,
    18: 8,
    19: 8,
    20: 6,
    30: 6,
    40: 5,
    50: 5,
    60: 5,
    70: 7,
    80: 6,
    90: 6,
    100: 13,
    200: 13,
    300: 15,
    400: 14,
    500: 14,
    600: 13,
    700: 15,
    800: 15,
    900: 14
}

sum = 0
for number in range(1, 1000):
    if number < 20:
        sum += numbers_to_words[number]
    elif number < 100:
        first_dig = number % 10
        second_dig = number - first_dig
        sum += numbers_to_words[first_dig]
        sum += numbers_to_words[second_dig]
    else:
        if number % 100 < 20:
            second_dig = number % 100
            third_dig = number - second_dig
            sum += numbers_to_words[second_dig]
            sum += numbers_to_words[third_dig]
        else:
            first_dig = number % 10
            second_dig = number % 100 - first_dig
            third_dig = number - second_dig - first_dig
            sum += numbers_to_words[first_dig]
            sum += numbers_to_words[second_dig]
            sum += numbers_to_words[third_dig]

#somando one thousand e tirando os and's de one hundred, two hundred, ..., nine hundred
print(sum + 3 + 8 - 27)

