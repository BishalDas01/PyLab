# set : collection of uniqe items. Duplicate items cannot exist

numbers = [43, 46, 78, 34, 43, 78]
print(numbers)

number_set = set(numbers)
print(number_set)

number_set.add(90)
print(number_set)

number_set.remove(43)
print(number_set)

for item in number_set:
    print(item)

if 43 in number_set :
    print('43 exist')
elif 90 in number_set:
    print('90 exist')

A = {23, 64, 48, 60, 34}
B = {54, 78, 23, 60, 33}

print(A & B) # A intersection B
print(A | B) # A union B (A U B)