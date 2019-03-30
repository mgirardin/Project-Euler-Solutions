def is_pal(number):
    number = str(number)
    length = len(number)
    start = 0
    while start<=length-1:
        if number[start]!=number[length-1]:
            return False
        start += 1
        length -= 1
    return True


produtos = []
for a in range(100, 1000):
    for b in range(a, 1000):
        produtos.append(a*b)

produtos.sort(reverse=True)
for number in produtos:
    if is_pal(number):
        print(number)
        break

