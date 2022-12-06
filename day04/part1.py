file = open('input.txt', 'r')
lines = file.readlines()

total_count = 0
for line in lines:
    line = line.strip()
    first_elf, second_elf = line.split(',')
    first_elf_lower_bound,first_elf_upper_bound = first_elf.split('-')
    second_elf_lower_bound,second_elf_upper_bound = second_elf.split('-')
    first_elf_lower_bound = int(first_elf_lower_bound)
    first_elf_upper_bound = int(first_elf_upper_bound)
    second_elf_lower_bound = int(second_elf_lower_bound)
    second_elf_upper_bound = int(second_elf_upper_bound)
    if (first_elf_upper_bound in range(second_elf_lower_bound, second_elf_upper_bound+1) and 
    first_elf_lower_bound in range(second_elf_lower_bound, second_elf_upper_bound+1)):
        total_count += 1
    elif (second_elf_upper_bound in range(first_elf_lower_bound, first_elf_upper_bound+1) and 
    second_elf_lower_bound in range(first_elf_lower_bound, first_elf_upper_bound+1)):
        total_count += 1

print(total_count)