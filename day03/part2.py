file = open('input.txt', 'r')
lines = file.readlines()
letter = None
compare = None
bag = None
total_count = 0
line1 = None
line2 = None 
line3 = None

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
    for char1 in line1:
        for char2 in line2:
            if char1 == char2:
                for char3 in line3:
                    if char3 == char1:
                        return get_priority(char3)
            

ghetto_skip_tracker = 0
for line1,line2,line3 in zip(lines,lines[1:],lines[2:]):
    if ghetto_skip_tracker != 0:
        ghetto_skip_tracker = (ghetto_skip_tracker + 1) % 3
        continue
    ghetto_skip_tracker += 1
    line1 = line1.strip()
    line2 = line2.strip()
    line3 = line3.strip()
    
    
    total_count += loop_fn()
        
    
print(total_count)



