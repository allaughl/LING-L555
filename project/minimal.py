import sys
#overall it works for the most part. I just wish i had more time to have it be able to delete the numbers and puncation used in the frequency. 

minimal = []


f = 'freq.txt'

with open(f) as file:
    p = [line.strip() for line in file]

for n1, word1 in enumerate(p):
    for n2 in range(n1 + 1, len(p)):
        word2 = p[n2]

        if len(word1) == len(word2):
            differences = sum(c1 != c2 for c1, c2 in zip(word1, word2))
            if differences == 1:
                minimal.append((word1, word2))


for pair in minimal:
    print(pair)
