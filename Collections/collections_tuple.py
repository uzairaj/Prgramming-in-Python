cars = ('BMW', 'Suzuki', 'Nissan',2)
print(cars)

#How to insert new item in a list?

cars.append(4)
print(cars)
# This will give us an error because we cant insert in tuple once it defined

#How to remove item from a list?

cars.remove('BMW')
print(cars)

# This will give us an error because we cant insert in tuple once it defined


#How to print a specific item of a tuple?
#We will use indexes for that…

print(cars[0]) # print first item of a tuple
print(cars[1]) # print second item of a tuple
print(cars[-1]) # print last item of a tuple
print(cars[-2]) # print second last item of a tuple
print(cars[1:])

#Check for a item in a tuple…
if "Honda" in cars:
    print("Found")
else:
    print("Not found")

print(len(cars)) # print length of a tuple


#Join two list
tup1 = ("a", "b" , "c")
tup2 = (1, 2, 3)

tup3 = tup1 + tup2
print(tup3)

cars.reverse() # this function will print tuple in reverse order
cars.sort() # this function will sort the tuple


cars.clear()  # will clear/remove all items in the tuple
print(cars)

del cars # will delete tuple
print(cars) # will give error
