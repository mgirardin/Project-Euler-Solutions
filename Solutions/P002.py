# Poderia usar programação dinâmica mas recursão funciona bem o suficiente para 4 milhões

#Calcula o n-ésimo fibonacci com recursão
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n-1)+fibonacci(n-2)

#Soma os fibonaccis pares menores que end
def sum_fib(end):
    sum = 0
    i = 2
    while fibonacci(i) < end:
        sum += fibonacci(i)
        i += 3  # Números de fibonacci só são pares nesses casos
    return sum

print(sum_fib(4000000))
