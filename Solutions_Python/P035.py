# armazena os primos
primos = []


# Crivo de eratostenes para teste de primalidade
def lista_primos(end):
    global primos
    primality = [1 for x in range(end+1)]
    primality[0] = 0
    primality[1] = 0
    for indice in range(end+1):
        if primality[indice] == 1:
            primos.append(indice)
            delete = indice*2
            while delete<end+1:
                primality[delete] = 0
                delete += indice
    return primality


# roda uma vez o num
def one_circle(num):
    num_str = str(num)
    length = len(num_str)
    new_str = num_str[-1]
    for i in range(length-1):
        new_str += num_str[i]
    return int(new_str)


# testa a primalidade de todas as rotações de num
def circle(num, lista):
    num = str(num)
    for i in range(len(num)-1):
        num = one_circle(num)
        if lista[num] == 0:
            return False
    return True

# testa a circularidade de todos os primos até 1 milhão
primality = lista_primos(1000000)
count = 0
for number in primos:
    if circle(number, primality):
        count += 1
print(count)
