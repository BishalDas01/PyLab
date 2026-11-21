
st = input()

count_L = 0
count_R = 0
splits = []
current = ""

for x in st:
    current += x
    if x == 'L':
        count_L += 1
    elif x == 'R':
        count_R += 1

    if count_L == count_R and count_L != 0:
        splits.append(current)
        current = ""
        count_L = 0
        count_R = 0

print(len(splits))
for part in splits:
    print(part)
