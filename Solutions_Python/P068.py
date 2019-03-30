from itertools import permutations

def isSolution(perm):
	sum1 = perm[order[0]]+perm[order[1]]+perm[order[2]]
	i=3
	for j in range(0,4):
		if(sum1 != perm[order[i]]+perm[order[i+1]]+perm[order[i+2]]):
			return False
		i+=3
	return True

def isValid(perm):
	for i in range(1,5):
		if(perm[0]>perm[i]):
			return False
	return True
	  
def create_group(perm):
	group = []
	for i in range(0,15):
		group.append(perm[order[i]])
		i += 1
	return group

def max_group(a, b):
	i=0
	while(i<15 and a[i]==b[i]):
		i+=1
	if(i==15):
		return a
	if(a[i]>b[i]):
		return a
	else:
		return b

def find_max(sol):
	max = sol[0]
	for i in range(0, len(sol)):
		if(max_group(sol[i],max)==sol[i]):
			max = sol[i]
	return max

order = [0,6,7,1,7,8,2,8,9,3,9,5,4,5,6]
permutationList = list(permutations(range(1,11)))
solutions = []
for perm in permutationList:
	if(isSolution(perm) and isValid(perm)):
		solutions.append(create_group(perm))

print(find_max(solutions))

