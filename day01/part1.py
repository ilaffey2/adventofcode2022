file = open('input.txt', 'r')
lines = file.readlines()
max_count = 0
current_count = 0

for line in lines:
    line = line.strip()
    if len(line) == 0:
        if max_count < current_count:
            max_count = current_count
        current_count = 0

    else:
        current_count += int(line)

print(max_count)