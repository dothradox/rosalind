# sample = "AAAACCCGGT"
# reverse = sample[::-1]

new_string = ""

f = open("rosalind_revc.txt", "r")
file_content = f.read()
reverse = file_content[::-1]

for i in range(len(reverse)):
    if reverse[i] == "A":
        new_string += "T"
    if reverse[i] == "T":
        new_string += "A"
    if reverse[i] == "G":
        new_string += "C"
    if reverse[i] == "C":
        new_string += "G"

print(new_string)
