import math     # usar sqrt

# retorna o indice-ésimo número triangular
def triangular(indice):
    return int(indice*(indice+1)/2)

# loop por todos os números até um que tenha mais de 500 divisores
nDivisores = 0
indice = 1
while nDivisores <= 500:
    num = triangular(indice)
    indice += 1
    nDivisores = 0
    for i in range(1, int(math.sqrt(num))+1):
        if num % i == 0:
            nDivisores += 2
    if(int(math.sqrt(num))**2 == num):
        nDivisores -= 1

print(num)