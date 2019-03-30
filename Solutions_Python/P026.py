# Calcula o tamanho do ciclo do número
# A parte infinita da fração corta quando fazemos 10**n/number - 1/number, restando um inteiro
# Logo, number | 10**n - 1
def cicle(number):
    if number == 1:
        return 0
    else:
        n = 1
        while True:
            if (10**n - 1) % number == 0:
                break
            n += 1
        return n

# Tira todos os fatores 2 e 5 do denominador (não influenciam no ciclo)
def retirar(number):
    while number % 5 == 0:
        number = int(number/5)
    while number % 2 == 0:
        number = int(number/2)
    return number


# Calcula o ciclo máximo, percorrendo todos os d's até 999
max = 0
for frac in range(2,1000):
    print(frac)
    cicle_frac = cicle(retirar(frac))
    if cicle_frac>max:
        max = cicle_frac
        value = frac

print(value)