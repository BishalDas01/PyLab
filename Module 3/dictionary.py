person1 = ['Shakor', 'Gogra', '20', 'Photographer']
print(person1)

# Structure : [key : value, key : value, key : value, key : value]
# key value pair
# dictionary
# using third bracket

person = {'name' : 'Shakor', 'address' : 'Gorgra', 'age' : '20', 'proffession' : 'Photographer'}
print(person)

print(person["name"])

print(person['proffession']) # we can access single key value

person['hobby'] = 'facebooking' # adding
print(person)

person['name'] = 'Shakor Debnath' # modifying
print(person)

print(person.keys())

print(person.values())

del person['age'] # deleting
print(person)

# special dictionary looping
for key, value in person.items():
    print(key, value)