numbers = [34, 53, 65, 34, 67, 23]

numbers.append(100) # add an item to the end of the list 
print(numbers)

numbers.insert(len(numbers), 90) #equivalent to append method
print(numbers)

numbers.insert(3,101) # insert 101 at index 3
print(numbers)

if 23 in numbers:
    numbers.remove(23) # remove the first item from the list whose value is equal to 23, it can rises valueError if there is no such item

pop_number = numbers.pop() # it will remove the last element and return the element
print(pop_number)
print(numbers)

removed_number = numbers.pop(4) # it will remove the 4th index element and it can also return the removed value
print(numbers)
print(removed_number)

# numbers.clear() # it will remove all the elements from the list
# print(numbers)

idx = numbers.index(101) # it will return the index of 101 according to 0 based index
print(idx)

# list.index(value, start_index, end_index) # if want to give a index range for search the value
index = numbers.index(101, 1, 4)
print(index)

count = numbers.count(65) # return the number of times 65 appears in the list
print(count)

numbers.sort() # sort the values of the list
print(numbers)

numbers.reverse() # reverse the values of the list
print(numbers)

array = numbers.copy() # return a shallow copy 
print(array)