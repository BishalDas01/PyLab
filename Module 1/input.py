print ('I need money')
input()

input ('i need money')

money = input('Give me some money: ')
print(money)

print (f'There is your money {money}')
print('THere is your money',     money)\

shakor_money = input('shakor kichu taka de : ')
nayon_money = input('noyon kichu taka de : ')

print('noyon and shakor amake diche',shakor_money+nayon_money, 'taka')

# by default python string input ney , tai mathematical add korar jonno amader age typecasting korte hobe

shakor_money_int = int(shakor_money) #typecasting for convert string to int
nayon_money_int = int(nayon_money) # type casting 

total = nayon_money + shakor_money

print ('nayon and shakor amake diche ',nayon_money_int + shakor_money_int , 'taka')