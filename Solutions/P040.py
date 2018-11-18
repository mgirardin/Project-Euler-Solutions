# calcula o numero de digitos do numero
def length_num(num):
    num_str = str(num)
    return len(num_str)


prod = 1
comprimento = 0
numero = 0
for i in [1, 10, 100, 1000, 10000, 100000, 1000000]:    #para cada indice do d
    while comprimento < i:                              #soma o comprimento dos inteiros até
        numero += 1                                     #passar do comprimento desejado
        comprimento += length_num(numero)
    prod *= int(str(numero)[i-comprimento-1])           #quando passa, volta o número de casas necessário e faz a mult

print(prod)
