
DICT = {
'1' : ['B', 'W', 'N'],
'2' : ['L', 'Z', 'S', 'P', 'T', 'D', 'M', 'B'],
'3' : ['Q', 'H', 'Z', 'W', 'R'],
'4' : ['W', 'D', 'V', 'J', 'Z', 'R'],
'5' : ['S', 'H', 'M', 'B'],
'6' : [ 'L', 'G', 'N', 'J', 'H', 'V', 'P', 'B'],
'7' : ['J', 'Q', 'Z', 'F', 'H', 'D', 'L', 'S'],
'8' : ['W', 'S', 'F', 'J', 'G', 'Q', 'B'],
'9' : ['Z', 'W', 'M', 'S', 'C', 'D', 'J']
}

file = open('input.txt', 'r')
lines = file.readlines()

total_count = 0
for line in lines:
    line = line.strip()
    separated = line.split(' ')
    number_to_move = int(separated[1])
    from_stack = separated[3]
    to_stack = separated[5]
    for count in range(number_to_move):
            print(DICT[from_stack])
            print(DICT[to_stack])
            DICT[to_stack].append(DICT[from_stack].pop())
            print()
            print(DICT[from_stack])
            print(DICT[to_stack])
        

print(DICT)