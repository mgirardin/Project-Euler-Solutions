# a recorrencia do problema é dada por s_{2n+1} = s_{2n-1} + 4(2n-1)^2 + 10(2n-1) + 10
def diag_sum(n):
    if n%2 == 0:
        return -1
    elif n==1:
        return 1
    else:
        return diag_sum(n-2) + 4*(n-2)**2 + 10*(n-2) + 10


print(diag_sum(1001))
