#interger
number = 123
print(number)

#string

word = 'Uzair Adamjee'
print(word)

#float
x= 20.16
print(x)

#complex

y = 1j
print(y)


#get type of variable

print(type(word))
print(type(number))
print(type(x))

'''
convert data type from of a variable
'''
a = '123'

print(type(a))

#changing type
b = int(a)

print(type(b))


#Boolean

flag = True
print(type(flag))

flag = False
print(type(flag))

#Datatime
#we need to use the datetime library
from datetime import datetime

current_date = datetime.now()
# The now function returns current date and time as a datetime object

# converting the datetime object to a string
print('Today is: ' + str(current_date))
