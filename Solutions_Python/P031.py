#brute force
ways = 0
for hundred in range(0, 2):
    for fifty in range(0, 4):
        for twenty in range(0, 10):
            for ten in range(0, 20):
                for five in range(0, 40):
                    for two in range(0, 100):
                        for one in range(0, 200):
                            sum = 100*hundred+50*fifty+20*twenty+10*ten+5*five+2*two+one
                            if sum > 200:
                                break
                            elif sum == 200:
                                ways += 1
ways += 8       #two hundred*1, hundred*2, fifty*4,...,one*200
print(ways)