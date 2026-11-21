# list , array, collection are almost same

# index =  0   1   2   3   4   5
numbers = [23, 45, 76, 87, 34, 56]
# index =  -6  -5  -4  -3  -2  -1    # python has reverse index

print(numbers[4] , numbers[-2])

# list[start : end]   # start from start index and stops before end index
print(numbers[1 : 5]) # it start from index 1 and run untill it reach 4th index
print(numbers[0 : 4]) # it start from index 0 and stops to index 4

#list[start : end : step]
print(numbers[1 : 5 : 2]) # it move forward by adding 2 with the index like : 1,3
print(numbers[1 : 5 : -1]) # it does not return any value, because by adding -1 with index value it cannot reach 1 to 5 index
print(numbers[5 : 1 : -1]) # it's the valid way, because by adding -1 with index value it can reach index 5 to index 1
print(numbers[5 : 1 : -2]) # it move foreward by adding -2 with index value

print(numbers[2:]) # by default it start from 2nd index and print to the last index(run untill reach last index)
print(numbers[:4]) # by default it start from index 0 and run untill it reach 4th index
print(numbers[:])  # it will print the whole list , it's a shortcut to copy full list 
print(numbers[::-1]) # it will reverse the list , it's shortcut for reverse list
