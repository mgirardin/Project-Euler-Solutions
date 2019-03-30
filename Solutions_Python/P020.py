# function to calculate n!
def factorial(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n*factorial(n-1)


# function that calculate the sum of digits of n
def sum_of_digits(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += int(i)
    return sum


print(sum_of_digits(factorial(100)))
