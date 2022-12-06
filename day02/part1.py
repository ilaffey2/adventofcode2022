file = open('input.txt', 'r')
lines = file.readlines()

table = {
    'A X' : 3 + 1, 'B X' : 0 + 1, 'C X' : 6 + 1,
    'A Y' : 6 + 2, 'B Y' : 3 + 2, 'C Y' : 0 + 2,
    'A Z' : 0 + 3, 'B Z' : 6 + 3, 'C Z' : 3 + 3
}
total_score = 0
for line in lines:
    line = line.strip()
    total_score+=table[line]
print(total_score)
