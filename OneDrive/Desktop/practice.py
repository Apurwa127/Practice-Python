# name = int(input("Please enter your age: "))

# if(name < 13):
#    print("you are a child")
# elif(name>=13 and name<=19):
#     print("you area a teenager")
# else:
#     print("you are an adult")

# number = int(input("Please enter your number: "))
# if(number % 2 == 0):
#     print("The number is even")
# else:
#     print("the number is odd")

# grades = int(input("Please enter your grade: "))
# if(grades>=90 and grades<=100):
#     print("A")
# elif(grades>=80 and grades<=89):
#     print("B")
# elif(grades>=70 and grades<=79):
#     print("C")
# elif(grades>=60 and grades<=69):
#     print("D")
# else:
#     print("F")

# day = int(input("Please enter your number "))
# if day>0:
#     print("Positive")
# elif day<0:
#     print("Negative")
# else:
#     print("Zero")

# year = int(input("Please enter the year: "))
# if year % 2 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("leap year")
# else:
#     print("Not leap year")

# inputUser = input("Please enter the password: ")
# password = "python123"

# if inputUser == password:
#     print("access granted")
# else:
#     print("access denied")

# inputUser = input("Enter your input: ")
# print("First Character", inputUser[0])
# print("Last Character", inputUser[-1])

# inputUser = input("Enter your input ")
# print("first three characters ", inputUser[0:3])
# print("last three character ", inputUser[-3:])
# print("all characters except the first and last ", inputUser[1:-1])

# num1 = input("number 1: ")


# print(num1.replace("a", "b"))
# print(num1.find("a"))

# days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# print([days])
# print(days[-1])
# print(days[-3])

# inputUser = input("Please enter your input ")

# charToFind = input("Please enter the character to find: ")

# find = inputUser.find(charToFind)

# if(find != -1):
#     print("found")
# else:
#     print("not found")

# number = [1,2,3,4,5,6,7,8,9,10]

# print(number[0:5])

# print(number[1::2])

# number.reverse()
# print(number)

# wordMeanings ={
#     "table" : ("a piece of furniture", "list of facts & figures"),
#     "cat" : "a small animal"

# }

# print(wordMeanings)

# classes= {
#     "Python", "Java", "C++", "Python", "Javascript", "Java", "Python", "Java", "C++", "C"
# }

# print(classes)
# print(len(classes))



# empyDict = {}

# x = int(input("Phy: "))
# empyDict.update({"phy": x})

# x = int(input("Chem: "))
# empyDict.update({"chem": x})

# x = int(input("Bio: "))
# empyDict.update({"Bio": x})

# print(empyDict)


# val = {9, '9.0'}

# print(val)

# dict = {
#     "name" : "Alice",
#     "Age" : 28,
#     "city" : "New York"
# }

# dict.update({"name": "Apu"})
# dict.update({"age": 27})

# print(dict)


# language = {"hello": "hola", 
#             "world": "mundo",
#             "thank you": "gracias",
#             "please": "por favor"}

# userInput = input("Please enter your Input: ")

# if userInput in language:
#     print("the tanslation is:", language[userInput] )
# else:
#     print("None")

# dict = {
#     "Harry" : 95,
#     "Mandy" : 85,
#     "Joseph" : 78,
#     "Steven" : 89,
#     "Kendra" : 87
# }

# dict.update({"Jamal": 58})
# dict.update({"Henry": 79})

# print(dict)



# fruits = [
#     "apple" ,
#     "Banana" ,
#     "Kiwi" ,
#     "Grapes" 
# ]
# defa = 50
# print(dict.fromkeys(fruits, defa))
# print(fruits)

# set1 = [1,2,3,4,5,6,6,1,2]
# print(set1)

# er = set1.copy()
# print(set(er))


# count = 1
# while count<5:
#     print("hello")
#     count +=1

# i = 1
# while i<=100:
#     print(i)
#     i+=1

# i = 100
# while i>=1:
#     print(i)
#     i-=1

# userInput = int(input("Pleaase enter your number: "))

# i = 1
# while i <=10:
#     print( userInput, "x ",i , "= ", i * userInput)
#     i += 1

# userList = [1,4,9,16,25,36,49,64,81,100]

# idx = 0
# while idx< len(userList):
#     print(userList[idx])
#     idx += 1

# tup = (1,4,9,16,25,36,49,64,81,100)

# x = 34

# i = 0

# while(i<=len(tup)):
#     if(x == tup[i]):
#         print("found1", i)
#     else:
#         print("finding")
#         i+=1


# i = 1

# while i <= 5:
#     if(i % 2 == 0):
#         i += 1
#         print(i)
#         continue
#     print(i)
#     i+= 1

# nums = [1,2,3,4,5,6]
# for val in nums:
#     print(val)

# nums = (1,4,9,16,25,36,49,64,81,100, 101)
# search = int(input("Please enter the number you would like to find: "))

# for val in nums:
#     if(search == val):
#         print(search," number found: ")
#         break
#     else:
#         print(val)


# numb = int(input("enter the number: "))
# i = 0
# sum = 0
# while i<= numb:
#     sum += i
#     i+=1
# print(sum)

# i =10
# while(i>=1):
#     i-=1
#     print(i)

# i = 1
# while(i<=20):
#     if(i%2 == 1):
#      i+=1    
#      continue
#     print(i)
#     i+=1


# i = 1 
# while(i<=10):
#     multiplication = 3 * i
#     print("3", "X", i, "=", multiplication)
#     i+=1

# userInput = int(input("Please enter your number: "))
# i=userInput
# while(0<=i):
#     print(i)
#     i-=1

# for i in range(1,11):
#  print(i)

# userInput = int(input("Please enter your number: "))
# x = 0
# for i in range(1, userInput+1):
#     x+=i
# print(x)

# string1 = "I love Programming"
# vowels = "aeiouAEIOU"
# i =1
# vlist = []
# for char in string1:
#     if char in vowels:
#         i += 1
#         vlist.append(char)
# print(vlist)

# numbers= [23, 56, 12, 89, 45, 67]
# x = numbers[0]
# for i in numbers:
#   if i > x:
#     x = i  
# print(x)


# string1 = "hello"
# rev = []
# for str in reversed(string1):
#     rev.append(str)
# print(rev)


# string1 = ["apple", "banana", "orange", "banana", "apple", "banana"]
# lst = input("Enter the fruit: ")
# count = 0
# for fruit in string1:
#     if fruit == lst:
#         count +=1
#         print(count)

# numbers = [23, 56, 12, 89, 45 , 67]
# x = numbers[0]
# for largest in numbers:
#     if largest > x:
#         x = largest
# print(x)

# nums = [1,2,3,4,5,6]
# for val in nums:
#     print(val)


# lst = [1,4,9,16,25,36,49,64,81,100]
# num = int(input("Enter your number: "))
# idx = 0
# for val in lst:
#     if(num == val):
#         print("Found ", val)
#     idx += 1


# for i in range(2,100,50):
#     print(i)

# for val in range(100, 0, -1):
#     print(val)

# userInput = int(input("Please enter your number: "))
# X = 0
# for val in range(1,11):
#     X = userInput * val
#     print("5 X ", val, "= ", X)


# i = 1
# factorial = 1
# n  = int(input("Enter your number: "))
# while(i<=n):
#     factorial *= i 
#     i+=1
# print("factorial", factorial)

# i = 1
# n = int(input("Please enter your number: "))
# for factorial in range (1, n + 1):
#     i*= factorial
# print(i) 

# info = {
#     "name": "Apurwa Bhattarai",
#     "age": 21,
#     "major": "Computer Science"
# }

# info["grade"] = "A"
# info["gpa"] = 3.8

# info.update({"age": 35})
# print(info)

# del info["age"]

# print(info)

# info = {
#     "name": "Apurwa Bhattarai",
#     "age": 21,
#     "major": "Computer Science"
# }

# if("major" in info):
#     print("Exists")
# else:
#     print("Don't Exist")

# contacts = {
#     "John": "1234",
#     "Alice": "5678",
#     "Bob": "91011"
# }
# for output in contacts.items():
#     print(output)

# fruits = {"apple", "banana", "orange", "apple", "grape"}

# if "orange" in fruits:
#     print("exists")
# else:
#     print("don't exists")
# print(fruits)

# set1 = {1,2,3,4}
# set2 = {3,4,5,6,}

# print(set2.difference(set1))

# colors = {"red", "blue", "green", "yellow"}
# for results in colors:
#     print(results)

# fruits = {"apple", "banana", "orange", "apple", "grape"}
# unique_items = len(fruits)
# print(unique_items)

# empDict = {}
# x = int(input("Phy "))
# empDict.update({"phy" : x})
# y = int(input("Chem "))
# empDict.update({"Chem" : y})
# z = int(input("Bio "))
# empDict.update({"Bio" : z})

# print(empDict)

# student_courses = {
#     "John": {"Math", "English", "History"},
#     "Alice": {"Math", "Science", "History"},
#     "Bob": {"English", "Art"}
# }

# student_courses["Bob"].add("Physics")

# inter = student_courses["John"].intersection(student_courses["Alice"])
# unique = student_courses["Bob"].union (student_courses["Alice"], student_courses["John"])

# print(unique)

# lst = [1,2,3,4,5,6,7,8,9,10]
# print(lst)

# print(lst[1])
# print(lst[3])

# fruits = ["apple", "banana", "cherry"]
# fruits[1] = "blueberry"
# print(fruits)

# numbers = [1,3,2,7]
# numbers.append(15)
# numbers[1] = 2
# numbers.sort(reverse=True)
# numbers.pop(1)
# numbers.reverse
# numbers.remove(2)
# print(numbers)

# numbers.insert(2,9)
# print(numbers)


# numbers1 = [10,20,30,40,50,60]
# numbers2 = [70,80,90,100]
# concatenate = numbers1 + numbers2
# print(concatenate)


# square= [x**2 for x in range(1,6)]
# print(square)

# userInput = input("Please enter your fruit's name: ")

# fruits = ['apple', 'banana', 'cherry', 'banana', 'apple']
# if (userInput in fruits):
#     print("Exists")
# else:
#     print("Don't Exist")

# nested = [[1,2],[3,4],[5,6]]
# print(nested[1][1])

# numbers = [1,2,3]
# result = [x * 3 for x in numbers]
# print(result)

# numbers = tuple(range(10, 20))
# print(numbers)

# fruits1 = ('apple', 'banana', 'cherry')

# print(len(fruits1))

# userInput = input("Please enter the name of animal: ")
# animals = ('dog', 'cat', 'rabbit')
# if userInput in animals:
#     print("exist")
# else:
#     print("don't exist")

# coordinates = (4,5)
# x, y = coordinates

# print("x", x)
# print("y" , y)

# nested = ((1,2), (3,4), (5,6))
# print(nested[1][0])

# nested = (1,2,3,2,1,2)

# print(nested.count(2))

# alphabet = ('a', 'b', 'c', 'd', 'e')
# change = list[alphabet]

# alphabet = ('a', 'b', 'c', 'd', 'e')
# print(alphabet[1:3])


# tuple = "Hello"

# multiply = [x * 3 for x in tuple]
# print(multiply)

# t1 = (1,2,3)
# t2 = (3,2,1)

# if(t1 == t2):
#     print("Equal")
# else:
#     print("Not Equal")


#     Swap Elements: Swap the first and last elements of the list my_list = [1, 2, 3, 4].

# Convert List to Tuple: Convert a given list my_list = ['apple', 'banana', 'cherry'] into a tuple.

# Create a Tuple with List Elements: Given a list numbers = [10, 20, 30], create a tuple where each element of the list is a separate element of the tuple.

# Filter Even Numbers from List: Given the list numbers = [1, 2, 3, 4, 5, 6], use a list comprehension to create a new list with only even numbers.

# List and Tuple Comparison: Given a list my_list = [1, 2, 3] and a tuple my_tuple = (1, 2, 3), compare them. Do they have the same values?


# def cal_sum(a ,b):
#     sum = a +b
#     return sum

# result = cal_sum(5,10)
# print(result)


# def average(a,b,c):
#     return (a + b+ c) /3

# ave = average(5,7,9)
# print(ave)


# def len_list():
#     numbers = [1,2,3,4,5,6,7,8,9]
#     return len(numbers)

# print(len_list())


# lst1 = [1,2,3,4,5]
# def element_list(list):
#     for item in list:
#         print(item, end = "")

# print(element_list(lst1))
  

# def fac1():
#     fac = 1
#     userInput  = int (input("please enter your number: "))
#     for i in range(1, userInput + 1):
#         fac *= i 
    
#     return fac
# print(fac1())


# def rev():
#     userInput = input("Please enter your word: ")
#     var = list(userInput)

#     var.reverse()
#     return ''.join(var)


# print(rev())


# def factorial():
#     userInput = (int(input("Please enter your number: ")))
#     fact =1
#     for items in range(1, userInput +1):
#         fact *= items
#     return fact

# print(factorial())


# def converter(usd):
#     inr = usd * 83
#     print(inr)

# converter("h")

# def userOutput(userInput):
#     if userInput % 2 == 1:
#         print("your number is odd")
#     else:
#         print("your number is even")

# userInput = int(input("Please enter your number: "))
# userOutput(userInput)


def for_loop(userInput):
    for i in range( userInput, 0, -1):
        i-=1
        print(i)

userInput = int(input("enter your number: "))
for_loop(userInput)