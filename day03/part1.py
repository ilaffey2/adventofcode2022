file = open('input.txt', 'r')
lines = file.readlines()
letter = None
compare = None
bag = None
total_count = 0

def get_priority(char :chr):
    if char.islower():
        char = char.upper()
        ordinal = ord(char)
    else:
        char = char.lower()
        ordinal = ord(char) -6

    subtract = ordinal - 64
    return subtract

def loop_fn():
    for letter in first_half:
        for compare in second_half:
            if letter == compare:
                return get_priority(letter)
for line in lines:
    line = line.strip()
    
    first_half = line[:int(len(line)/2)]
    second_half = line[int(len(line)/2):]
    print(first_half)
    print(second_half)
    total_count += loop_fn()
        
    
print(total_count)



