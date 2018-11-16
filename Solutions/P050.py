#Crivo de Eratostenes para conseguir a lista de primos e um teste de primalidade
def lista_primos(end):
    global is_prime
    is_prime = [1 for x in range(end+1)]
    is_prime[0] = 0
    is_prime[1] = 0
    for indice in range(end+1):
        if is_prime[indice] == 1:
            delete = 2*indice
            while delete < end + 1:
                is_prime[delete] = 0
                delete += indice
    lista_ans = [x for x in range(end+1) if is_prime[x] == 1]
    return lista_ans

# verifica se existe sequencia consecutiva de
# longest primos com soma prima
def summable(longest, lista):
    begin = 0
    sum = 0
    length = len(lista)
    while (begin + longest - 1) < length:
        if begin == 0:
            for i in range(longest):
                sum += lista[begin+i]
        else:
            sum -= lista[begin-1]
            sum += lista[begin+longest-1]
        if sum < lista[len(lista)-1]:
            if is_prime[sum] == 1:
                return sum
        begin += 1
    return -1

# pega a lista de primos até 1 milhão e condiciona o teste de primalidade
primos = lista_primos(1000000)

# calcula um limite superior size para o número de primos consecutivos na soma
# já que a soma que começa com 2 é a menor possível
size = 1
sum = 0
while sum < 1000000:
    sum = 0
    for i in range(size):
        sum += primos[i]
    size += 1


while True:
    possiblePrime = summable(size, primos)
    if possiblePrime != -1:
        print(possiblePrime)
        break
    size -= 1
