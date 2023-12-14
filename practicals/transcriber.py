import sys

tran = {}
for line in open('scottsipa.tsv').readlines():
        line = line.strip('\n')
        if '\t' not in line:
           continue
        (letter,ipa) = line.split('\t')
        tran[letter] = ipa

for line in sys.stdin.readlines():
    line = line.strip('\n')

    if '\t' not in line:
        print(line)
    if '\t' in line:
        row = line.split('\t')
        form = row[1]
        transcription = form
        for character in tran:
            transcription = transcription.replace(character, tran[character])
        row[9] = 'IPA=' + transcription
        print('\t'.join(row))


