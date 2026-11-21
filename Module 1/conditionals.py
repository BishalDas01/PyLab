# if, elif, else, and, or, is, is not, nested.

money = input('your budget : ')

print(type(money))
int_money = int(money)

if int_money >= 500: 
    print('you can take kacchi briyani')
elif int_money >= 300 :
    print('you can take chiken biriyani')
elif int_money >= 100 :
    print('you can take egg biriyani')
else :
    print('you can take two parata and alur dom')

a = 5
b = 8

if a<b and b<10:
    print('a b er theke chuto and b 10 er theke chuto')
elif a>b or b>a:
    print('a b theke chuto or b a theke boro')

sir = True

if sir is True:
    print('sir eshechen')
else :
    print('sir ashen ni')

if sir is not True:
    print('sir ashen ni')
else:
    print('sir eshechen')

if sir is True:
    print('sir is true')
    if sir is not False:
        print('sir eshechen')