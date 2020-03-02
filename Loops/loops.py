'''
While Loop
'''

i = 1
while i < 6:
  print(i)
  i += 1


n = 5

# initialize sum and counter
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


computer_brands = ["Apple", "Asus", "Dell", "Samsung"]
i = 0

while i < len(computer_brands):
    print (computer_brands[i])
    i = i + 1          	




'''
For Loop
'''

# Dictionary
my_data = {'Name': 'Uzair', 'Age': 24, 'Education': 'Masters'}

for key in my_data.keys():
  print(key)
  
for value in my_data.values():
  print(value)

for x, y in my_data.items():
  print(x, y)




# List
lst = ["grapes", "apple", "banana"]
for item in lst:
    print(item)


# Tuple
cars = ("UK", "Cricket", "Football","Paris")

for car in cars:
    print(car)

# Sets

cars_set = {"Nissan", "BMW", "Honda"}
for car in cars_set:
    print(car)


###  BREAK & CONTINUE  ###

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


for x in range(6):
  print(x)
