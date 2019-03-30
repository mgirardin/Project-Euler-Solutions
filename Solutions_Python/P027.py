# function x**2 + ax + b
def quadratic(value, a, b):
    return value*value + value*a + b


# Crivo de eratostenes para teste de primalidade
def lista_primos(end):
    lista = [1 for x in range(end+1)]
    lista[0] = 0
    lista[1] = 0
    for number in range(end+1):
        if lista[number] == 1:
            delete = number*2
            while delete < end+1:
                lista[delete] = 0
                delete += number
    return lista


# criando o teste de primalidade
lista = lista_primos(1000000)

# testando todos os a's e b's
max = 0
prod = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while True:
            if lista[quadratic(n, a, b)] == 0:
                break
            n += 1
        if n > max:
            max = n
            prod = a*b
print(prod)
