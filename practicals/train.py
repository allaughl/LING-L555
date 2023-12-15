import sys

tokens = 0

wcount = {}
t = {}

fd = open('wiki.conllus', 'r')

for line in fd.readlines():

        line = line.strip('\n')
        if '\t' not in line:
                continue
        row = line.split('\t')
        form = row[1].strip()
        tag = row[3]
        if form not in t:
                t[form]= {}
        if tag not in t[form]:
                t[form][tag] = 0
        t[form][tag] += 1
        tokens += 1

        if form not in wcount:
                wcount[form] = 0
        wcount[form] += 1

print("# P\tcount\ttag\tform")
for form in t:
    for tag, count in t[form].items():
        freq = count / wcount[form]
        print(f"{freq:.2f}\t{count}\t{tag}\t{form}")
