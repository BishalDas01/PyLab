# def doubled(num):
#     return num * 2

# double = doubled(43)
# print(double)

double = lambda num : num * 2
double_it = double(43)
print(double_it)

squared = lambda num : num ** 2
result = squared(8)
print(result)

add = lambda x, y : x + y
sum = add(43, 7)
print(sum)