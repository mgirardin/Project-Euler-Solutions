import math

# Em 40 escolhas de direita ou esquerda, devemos escolher 20 direitas -> 40 escolhe 20
ans = math.factorial(40)/(math.factorial(20)*math.factorial(20))
print(int(ans))

