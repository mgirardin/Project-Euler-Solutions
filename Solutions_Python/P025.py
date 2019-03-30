# tabulation
fibonaccis = [0]


# calcula o numero de digitos
def n_digits(num):
    num_str = str(num)
    return len(num_str)

# calcula o fibonacci
def fib(indice):
    global fibonaccis
    if indice == 1:
        fibonacci = 1
    elif indice == 2:
        fibonacci = 1
    else:
        fibonacci = fibonaccis[indice-2]+fibonaccis[indice-1]

    fibonaccis.append(fibonacci)
    return fibonacci


# loop pela sequencia até ter 1000 digitos
atual = 0
indice = 1
while n_digits(atual) < 1000:
    atual = fib(indice)
    indice += 1
print(indice-1)
