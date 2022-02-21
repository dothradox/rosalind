sample1 = "GAGCCTACTAACGGGAT"
sample2 = "CATCGTAATGACGGCCT"

f = open("rosalind_hamm.txt", "r")
first_line = f.readline().strip()
second_line = f.readline().strip()

count = 0

for i in range(len(first_line)):
    if first_line[i] != second_line[i]:
        count += 1
print(count)
