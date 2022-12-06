file = open('input.txt', 'r')
line = file.readline()
line = line.strip()

index = 0
for char in line:
    if len(list(set(line[index:index+4]))) == 4:
        print (index + 4)
        break
    index += 1