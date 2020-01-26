lst = ["one", 2, "three"]
print(lst)

#How to insert new item in a lst?

lst.append(4)
print(lst)

#How to remove item from a lst?

lst.remove(2)
print(lst)

#How to print a specific item of a lst?
#We will use indexes for that…

print(lst[0]) # print first item of a lst
print(lst[1]) # print second item of a lst
print(lst[-1]) # print last item of a lst
print(lst[-2]) # print second last item of a lst
print(lst[1:])

#Check for a item in a lst…
if "one" in lst:
    print("Found")
else:
    print("Not found")

print(len(lst)) # print length of a lst


#Join two lst
lst1 = ["a", "b" , "c"]
lst2 = [1, 2, 3]

lst3 = lst1 + lst2
print(lst3)

lst.reverse() # this function will print lst in reverse order
lst.sort() # this function will sort the lst


lst.clear()  # will clear/remove all items in the lst
print(lst)

del lst # will delete lst
print(lst) # will give error
