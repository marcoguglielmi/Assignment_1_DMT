f = open("C:/Users/Marco/Desktop/leaderboard.txt", encoding='UTF')
s = 0
t = 0
for line in f:
    if '0.' in line:
        if 'Gold' in line:
            line = line.strip('Gold Medal')
        if 'Silver' in line:
            line = line.strip('Silver Medal')
        t += 1
        s += float(line)
average = s/t
print(average)