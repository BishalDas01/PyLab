n = int(input())

numbers = []
numbers = list(map(int, input().split()))
count = 0
num = []
for i in numbers:
    if i in num:
        continue
    if i == 0:
        continue
    num.append(i)
    same = numbers.count(i)
    if same > i:
        count += same - i
    elif i > same:
        count += same
print(count) 
