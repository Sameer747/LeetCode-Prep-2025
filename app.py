# first pyhton code
print('Hello World')

# variables: Use to temporarily store data into computer
age  = 20 #int
price = 19.95 #double
firstName = 'Sameer' #string
isOnline = False #boolean
print(firstName + " " + str(age) + " " + str(price) + " " + str(isOnline))

# user input with type casting 
# by default python takes input as strings and later it is converted
name = str(input("Name: "))
age = str(float(input('Age: ')))
print(name + " \n" +age)
# Exercise
firstNo = float(input("First: "))
secondNo = float(input("Second: "))
sum = str(firstNo + secondNo)
print('total sum is: '+ sum)