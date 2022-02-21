# sample = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
# A C G T
count_list = [0] * 4
f = open("rosalind_dna.txt", "r")
file_content = f.read()
for i in file_content:
    if i == "A":
        count_list[0] += 1
    if i == "C":
        count_list[1] += 1
    if i == "G":
        count_list[2] += 1
    if i == "T":
        count_list[3] += 1
print(count_list)
