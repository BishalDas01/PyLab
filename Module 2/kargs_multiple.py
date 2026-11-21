def full_name(first, last):
    print(f'{first} {last}')

full_name('modon', 'ali')

full_name(last = 'ali', first = 'modon')

def do_something(first, last, **kargs):
    print(f'{first}, {last}')
    print(kargs)
    for key, value in kargs.items():
        print(kargs)

name = do_something(first = 'chondon', last = 'datta', key = 'chabiborsike', ahso = 'halar po')
def a_lot(num1, num2):
    sum = num1 + num2
    mul = num1 * num2
    rem = num1 % num2
    return sum, mul, rem

result = a_lot(30, 10)
print(result)

def result(n1, n2, n3):
    total = n1 + n2 + n3
    return total
