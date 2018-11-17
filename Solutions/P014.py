records = [-1 for x in range(0, 1000000)]       # guarda tamanhos de chains já conhecidos


class collatz:                                  # classe para guardar o número analisado e o tamanho de sua chain
    iterations = 0
    number = 0

    def apply(self):
        apply_collatz(self, self.number)
        return 1


def apply_collatz(init, num):                   # processo de collatz
    global records
    if num < 1000000 and records[num] != -1:
        init.iterations += records[num]
        records[init.number] = init.iterations
        return 1

    init.iterations += 1
    if num == 1:
        records[init.number] = init.iterations
        return 1
    elif num % 2 == 0:
        return apply_collatz(init, int(num/2))
    else:
        return apply_collatz(init, 3*num + 1)


max_length = 0
biggest_chain_number = 0
for number in range(1, 1000000):                 #loop pelos números até 1 milhão para calcular tamanho da chain
    collatz_inst = collatz()
    collatz_inst.number = number
    collatz_inst.apply()
    size = collatz_inst.iterations
    if size > max_length:
        max_length = size
        biggest_chain_number = number

print(biggest_chain_number)

