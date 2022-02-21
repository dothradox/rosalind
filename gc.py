from numpy import amin


count = 0
count = len(open("rosalind_gc.txt").readlines())

f = open("rosalind_gc.txt", "r")
great = {}
for i in range(0, count, 2):
    gc_count = 0
    string_id = f.readline().strip()
    string = f.readline().strip()
    for amino_acids in string:
        if amino_acids == "C" or amino_acids == "G":
            gc_count += 1
    great[string_id] = gc_count / len(string) * 100
max_key = max(great, key=great.get)
print(max_key[1:])
print(great[max_key])
