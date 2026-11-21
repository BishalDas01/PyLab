size = int(input())
numbers = []

for i in range(size):
    x = int(input())
    numbers.append(x)

rev_numbers = numbers[::-1]

if rev_numbers == numbers:
    print("YES")
else:
    print("NO")
