# Brute force solution
def verify(a, b, c):
    if a*a + b*b == c*c:
        return True
    return False


# loop through all a, b, c such that a+b+c=1000
for a in range(1,1001):
    for b in range(a, 1001):
        if verify(a, b, 1000-a-b): # verifies if it is a pythagorean triplet
            print(a*b*(1000-a-b))
            


