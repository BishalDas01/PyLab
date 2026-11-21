from functio import double_it # following this method we can import function from any file
from functio import sum as sm # by 'as' keyword we can also define the name of function that was imported from another file

rslt = double_it(50)
print(rslt)

total = sm(10,20)
print(total)