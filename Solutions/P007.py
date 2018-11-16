#Crivo de Eratóstenes
def lista_primos(end):
    lista = [1 for x in range(end+1)]
    lista[0] = 0
    lista[1] = 0

    for indice in range(end+1):
        if lista[indice] == 1:
            nao_primo = 2*indice
            while nao_primo < end+1:
                lista[nao_primo] = 0
                nao_primo += indice
    numbers = [x for x in range(end+1) if lista[x]==1]
    return numbers

# finding size such that (2,size) has 10001 primes
size = 1000000
while len(lista_primos(size))<10001:
    size += 100000

print(lista_primos(size)[10000])

