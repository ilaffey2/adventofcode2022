file = open('input.txt', 'r')
lines = file.readlines()
top3 = [0, 0, 0]
current_count = 0

for line in lines:
    line = line.strip()
    lowest = top3[0]
    if len(line) == 0:
        if lowest < current_count:
            top3[0] = current_count
            top3.sort()
        current_count = 0

    else:
        current_count += int(line)
total = top3[0] + top3[1] + top3[2]
print(total)