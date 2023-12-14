import sys

s = sys.stdin.readline()
while s:
    if s == '':
        continue
    if s.strip():
        print(s.strip().replace('. ', '.\n'))

    s = sys.stdin.readline()
