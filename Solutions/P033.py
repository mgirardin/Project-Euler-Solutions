import math

# retorna o primeiro digito de num
def first_digit(num):
    num_str = str(num)
    return int(num_str[0])

# retorna o segundo digito de num
def second_digit(num):
    num_str = str(num)
    return int(num_str[1])

# classe para armazenar uma fração de numerador num e denominador denum
class Fraction():
    num = 0
    denum = 0

    # apply verifica se o numerador e denominador contem digitos iguais
    # se sim, testa a regra de corte
    def apply(self):
        # denominador não pode virar 0
        if second_digit(self.denum) != 0:
            if first_digit(self.num) == first_digit(self.denum):
                num_n = second_digit(self.num)
                denum_n = second_digit(self.denum)
                if self.num/self.denum == num_n/denum_n:
                    return True
            if second_digit(self.num) == first_digit(self.denum):
                num_n = first_digit(self.num)
                denum_n = second_digit(self.denum)
                if self.num/self.denum == num_n/denum_n:
                    return True
        if first_digit(self.num) == second_digit(self.denum):
            num_n = second_digit(self.num)
            denum_n = first_digit(self.denum)
            if self.num/self.denum == num_n/denum_n:
                return True
        if second_digit(self.num) == second_digit(self.denum):
            num_n = first_digit(self.num)
            denum_n = first_digit(self.denum)
            if self.num/self.denum == num_n/denum_n:
                return True
        return False


prod_a = 1
prod_b = 1
for a in range(10,100):
    for b in range(a+1, 100):
        numero = Fraction()
        numero.num = a
        numero.denum = b
        if numero.apply() and (second_digit(numero.num) and second_digit(numero.denum)):
            prod_a *= a
            prod_b *= b

# tira o máximo divisor comum e printa o denominador
gcd = math.gcd(prod_a, prod_b)
prod_a = int(prod_a/gcd)
prod_b = int(prod_b/gcd)
print(prod_b)

