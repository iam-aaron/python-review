import re
fh = open("sum2.txt")
num_list = list()

for line in fh:
    line = line.strip()
    num_finds = re.findall('([0-9]+)',line)
    if len(num_finds) < 1: continue
    for num in num_finds:
        num_list.append(int(num))

Sum = sum(num_list)
print(Sum)
