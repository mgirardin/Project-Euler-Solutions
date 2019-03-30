# saving number as a string
number = str(2**1000)

# Calculating the sum of the digits
sum = 0
for digit in number:
    sum += int(digit)
print(sum)

