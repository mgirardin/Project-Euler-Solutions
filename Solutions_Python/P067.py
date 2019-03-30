#Dynamic programming

file = open("P067.txt", "r")

numbers = []
sums = []
i = 1	
lines = file.readlines()
for line in lines:
	numbers.append([int(x) for x in line.split()])

for i in range(0, len(numbers)):
	sums.append([0]*len(numbers))

for i in range(len(numbers)-1, -1, -1):
	for j in range(0, i+1):
		if(i==(len(numbers)-1)):
			sums[i][j]=numbers[i][j]
			continue
		if(sums[i+1][j]>sums[i+1][j+1]):
			sums[i][j]=numbers[i][j]+sums[i+1][j]
		else:
			sums[i][j]=numbers[i][j]+sums[i+1][j+1]

print(sums[0][0])
