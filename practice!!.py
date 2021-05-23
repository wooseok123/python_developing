import re


text = open("hihi.txt")

total = 0

for line in text:
    line = line.rstrip()
    find_num = re.findall('[0-9]+',line)

    for x in find_num:
        x = int(x)
        total += x

print(total)

    
