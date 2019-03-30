# lista de primos até 20
primes = [x for x in range(2, 21)]
for indice in range(0, 19):
    if primes[indice] != 1:
        for next in range(indice+1, 19):
            while primes[next]%primes[indice] == 0:
                primes[next] /= primes[indice]

all_numbers = [x for x in range(2, 21)]                         # numeros de 2 a 20
primes = [primes[x] for x in range(0,19) if primes[x] != 1]     # primos de 2 a 20
multiplicities = [1 for x in range(len(primes))]                # maior multiplicidade dos primos na lista

# calculando as maiores multiplicidades
for indice in range(len(primes)):
    max = 0
    for number in all_numbers:
        temp = 0
        while number % primes[indice] == 0:
            number /= primes[indice]
            temp += 1
        if temp>max:
            max = temp
        multiplicities[indice] = max

ans = 1
for i in range(len(primes)):
    ans *= primes[i]**multiplicities[i]

print(ans)
