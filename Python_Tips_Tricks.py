#Create a single string from all the elements in list
a = ["My", "name", "is", "Uzair"] 
print(" ".join(a))


#Return Multiple Values From Functions
def x(): 
    return 1, 2, 3, 4
a, b, c, d = x() 
  
print(a, b, c, d)


#Find The Most Frequent Value In A List
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4] 
print(max(set(test), key = test.count))


#Swap Variables In-Place
x, y = 8, 10
print(x, y)
x, y = y, x
print(x, y)


#Assigning multiple values in multiple variables
x, y = 10, 20


#Concatenate Strings
print('Python' + ' Coding' + ' Tips')



#Removing duplicates items from a list

listNumbers = [1, 10, 10, 2, 2, 1, 5, 10, 20,30,50,20,100]
print("Original= ", listNumbers)
listNumbers = list(set(listNumbers))
print("After removing duplicate= ", listNumbers)
