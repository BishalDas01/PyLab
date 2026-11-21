numbers = [43, 54, 75, 73, 34, 54, 87, 89, 34, 65, 74]

even_numbers = []
for number in numbers:
    if number % 2 == 0 and number % 6 == 0:
        print(number)
        even_numbers.append(number)

print(even_numbers)

even_nums = [nums for nums in numbers if nums % 2 == 0 if nums % 6 == 0] # it is python comprehension, it's means and work same as 3 to 7 lines
print(even_nums)