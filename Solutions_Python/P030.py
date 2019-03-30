def sum_of_digits(n):
    n_str = str(n)
    sum = 0
    for digit in n_str:
        sum += int(digit)**5
    return sum


# n_digits <= number <= 9**5 * n_digits = 59049 -> 1= <n_digits <=6
# for n=6, number<=59049*6=354.294
sum = 0
for number in range(2, 354295):
    if number == sum_of_digits(number):
        sum += number

print(sum)

