file = open('input.txt', 'r')
line = file.readline()
line = line.strip()

index = 0
for char in line:
    if len(list(set(line[index:index+14]))) == 14:
        print (index + 14)
        break
    index += 1