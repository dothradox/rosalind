protein_to_possible_rna_dict = {
    "F": 2,
    "L": 6,
    "S": 6,
    "Y": 2,
    "C": 2,
    "W": 1,
    "P": 4,
    "H": 2,
    "Q": 2,
    "R": 6,
    "I": 3,
    "M": 1,
    "T": 4,
    "N": 2,
    "K": 2,
    "V": 4,
    "A": 4,
    "D": 2,
    "E": 2,
    "G": 4,
}
stop_codons = ["UGA", "UAA", "UAG"]
no_of_stop_codons = len(stop_codons)
f = open("rosalind_mrna.txt", "r")
file_content = f.read()
print(file_content)
value = 1
for amino_acid in file_content:
    value = value * protein_to_possible_rna_dict[amino_acid]
value = value * no_of_stop_codons
print(value % 1000000)
