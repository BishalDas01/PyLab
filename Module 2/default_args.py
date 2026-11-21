def sum(num1, num2, num3=0, num4=0):  # num3=0 deyay amra jodi num3 er parameter na o patai tahole kuno problem hobe na, num3=0 dhore kaj calai dibe, 
    total = num1 + num2 + num3 + num4 
    return total
total = sum(12, 34, 45)
print(total)

def summation(*args): # * dile joto iccha parameter pathano jay, abr na pathale o problem hoy na. ata basically arrayr moto kaj kore , ta amra etate loop o chalate pari
    print(args)
    summ = 0
    for num in args:
        print(num)
        summ += num
    return summ

result = summation(21, 34, 65, 67, 34)

print(result)

re = summation()
print(re)