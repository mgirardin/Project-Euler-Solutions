# Soma dos multiplos de base entre start e end
def sum_multiples(start, end, base):
    sum = 0
    for number in range(start, end):
        if number%base==0:
            sum += number
    return sum

#Calculando a soma dos múltiplos de 3 e 5 e depois tirando a interseção
threeX = sum_multiples(1, 1000, 3)
fiveX = sum_multiples(1, 1000, 5)
fifteenX = sum_multiples(1, 1000, 15)

print(threeX + fiveX - fifteenX)

