import sys

line = sys.stdin.readline()
counter = 1

while line:
    print('# sent_id = %d' % (counter))
    line = sys.stdin.readline()
    counter += 1
    print('# text = %s' % line.strip())

    for pun in ".,!?;:'":
        line = line.replace(pun, ' ' + pun)

    tokens = line.split()
    counter1 = 1

    for c in tokens:
        print('%d\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s' % (counter1, c, '_', '_', '_', '_', '_', '_', '_', '_'))
        counter1 = counter1 +1
 
    line = sys.stdin.readline()
    print()		
