####READING

f = open("D:/abc.txt") # specifying full path
#f= open("abc.txt","w+")


file = open("D:/abc.txt", "r")
# a file named myfile, will be opened in reading mode
for data in file:
   print(data)# This will print every line one by one in the file
file.close()



#f = open("test.txt", mode='r', encoding='utf-8')


#CLOSE

f = open("D:/abc.txt")
f.close()


f = open("D:/abc.txt", "r")
print(f.readline())
f.close()


file = open("D:/myfile.txt","w")
file.write("Welcome to medium\n")
file.write("This tutorial is about file handling")
file.close()


#READING
file = open("D:/myfile.txt", "r")
1print (file.read())
print(file.readline())

#DELETION
import os
os.remove("D:/myfile.txt")
