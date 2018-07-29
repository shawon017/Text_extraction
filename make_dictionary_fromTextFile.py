import os
os.chdir('c:/Shell')
intt = input()
if intt == '2':
    with open('dict.txt', 'r') as f:
        d = {}
        for line in f.readlines():
            line = line.split('x')
            key, value = (x.strip() for x in line)
            if key in d:
                d[key].append(value)
            else:
                d[key] = [value]

    print(d)
