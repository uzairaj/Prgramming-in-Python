
empty_dict = {} #empty dictionary

my_data = {'Name': 'Uzair', 'Age': 24, 'Education': 'Masters'}

print(my_data)

# Print dictionary element using key
print(my_data['Name'])
print(my_data['Age'])

# Print dictionary element using get() function 
edu = my_data.get('Education')
print(edu)


# Change a key value
my_data['Age'] = 20

print(my_data)

#insert new item

my_data['Country'] = 'Karchi'

print(my_data)

# delete element from dictionry using key and del 

print(my_data.items())
print(my_data.values()) #print all values of dictionary

if "model" in my_data:
    print('Key found')
else:
    print('Not found')

print(len(my_data))


del my_data['Name']; # remove entry with key 'Name'
print(my_data)
#my_data.clear();     # remove all entries in dict
#del my_data ;        # delete entire dictionary
