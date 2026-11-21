n = input()
nn = int(n)
nb = nn
rev = 0

while nn != 0 :
    nm = int(nn % 10)
    rev = rev*10 + nm
    # if nm != 0:
    #     rev = rev*10 + nm
    nn //= 10

print(rev)
if rev == nb:
    print('YES')
else :
    print('NO')