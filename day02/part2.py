file = open('input.txt', 'r')
lines = file.readlines()

table = {
    'A X' : 0 + 3, 'B X' : 0 + 1, 'C X' : 0 + 2,
    'A Y' : 3 + 1, 'B Y' : 3 + 2, 'C Y' : 3 + 3,
    'A Z' : 6 + 2, 'B Z' : 6 + 3, 'C Z' : 6 + 1
}
total_score = 0
for line in lines:
    line = line.strip()
    total_score+=table[line]
print(total_score)
