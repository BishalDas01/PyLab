numbers = [54, 43, 76, 34, 53, 97]

doubled_nums = map(lambda x : x*2 , numbers)
print(numbers)
print(list(doubled_nums))

squared_nums = map(lambda x : x ** 2 , numbers)
print(list(squared_nums))

actors = [
    {'name' : 'Bishal', 'age' : '20'},
    {'name' : 'Nayon', 'age' : '21'},
    {'name' : 'Shakor', 'age' : '22'},
         ]

juniors = filter(lambda actor :  int(actor['age']) < 21, actors)

print(list(juniors))
 