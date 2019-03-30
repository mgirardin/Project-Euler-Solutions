# precisa de otimização, leva alguns minutos
def triangular(n):
    return int(n*(n+1)/2)


def is_pentagonal(number):
    n = 1
    while int(n*(3*n-1)/2) <= number:
        if int(n*(3*n-1)/2) == number:
            return 1
        n += 1
    return 0


def is_hexagonal(number):
    n = 1
    while n*(2*n-1) <= number:
        if n*(2*n-1) == number:
            return 1
        n += 1
    return 0

ind = 286

while True:
    print(ind)
    triang = triangular(ind)
    if is_hexagonal(triang) and is_pentagonal(triang):
        print(triang)
        break
    ind += 1

