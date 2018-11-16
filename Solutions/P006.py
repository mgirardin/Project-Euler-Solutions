def sum_of_squares(end):
    return end*(end+1)*(2*end+1)/6 # Identidade facilmente provada por indução finita


def square_of_sum(end):
    sum = end*(end+1)/2            # 1+2+...+end = (1+end)+(2+(end-1))+... = end*(end+1)/2
    return sum*sum


print(int(square_of_sum(100) - sum_of_squares(100)))

