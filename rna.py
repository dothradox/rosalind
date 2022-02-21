# sample = "GATGGAACTTGACTACGTAAATT"
u = ""

f = open("rosalind_rna.txt", "r")
file_content = f.read()

for i in range(len(file_content)):
    if file_content[i] == "T":
        u += "U"
    else:
        u += file_content[i]
print(u)
