#Crivo de Eratostenes
def list_of_primes(end):
    list = [1 for x in range(end+1)]
    list[0] = 0
    list[1] = 0
    for i in range(end+1):
        if list[i] == 1:
            j = 2*i
            while j < (end+1):
                list[j] = 0
                j += i
    list_ans = []
    for i in range(end+1):
        if list[i] == 1:
            list_ans.append(i)
    return list_ans

# Somando os valores da lista de primos
ans = 0
for prime in list_of_primes(2000000):
    ans += prime
print(ans)
