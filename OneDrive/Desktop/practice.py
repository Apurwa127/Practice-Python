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


# def for_loop(userInput):
#     for i in range( userInput, 0, -1):
#         i-=1
#         print(i)

# userInput = int(input("enter your number: "))
# for_loop(userInput)


# def calc_sum(n):
#     if(n==0):
#         return 0
#     return calc_sum(n-1) + n

# sum = calc_sum(10)
# print(sum)

# def show(n):
#     if(n==0):
#         return
#     print(n)
#     print(n-1)
#     print("END")

# show(5)

# numbers = [1,2,2,3,4,4,5]

# squared = [x ** 2 for x in numbers]
 
# print(squared)

# set1 = {1,2,3}
# set2 = {2,3}

# print(set1.issubset(set2))
# print(set1.issuperset(set2))


# for i in range(1,20 +1):
#     if(i % 2 == 0):
#         print(i ,"even")
#     else:
#         print(i, "odd")
    
# number = [1,2,3,4,5,6]

# for i in number:
#     square = i ** 2
#     print(square)


# number = [10,5,30,15,25]

# max_num = number[0]

# for num in number:
#     if num>max_num:
#         max_num=num
# print(max_num)

# word = "education"

# for i in word:
#     if i in "aeiou":
#      print(i, "vowel")
#     else:
#         print(i, "not vowel")
    

# word = "hello"
# for i in reversed(word):
#    print(i)

# word = "banana"
# letter_count = {}  # Dictionary to store letter counts

# # Iterate through each letter in the word
# for letter in word:
#     if letter in letter_count:
#         letter_count[letter] += 1  # Increment count if the letter is already in the dictionary
#     else:
#         letter_count[letter] = 1  # Initialize count to 1 if the letter is not in the dictionary

# Print the results
# for letter, count in letter_count.items():
#     print(f"{letter} is repeated {count} times")


# word = "banana"
# vowel = {}

# for i in word:
#     if i in 'aeiou':
#         print(i, " is vowel")
#     else:
#         print(i, " not vowel")

# f = open("demo.txt", "a")
# f = open("sample.txt", "w")
# f.close()

# data = f.write("This is a test2")
 
# print(data)
# print(type(data))
# f.close()



# def file_no():
#     word = "learning"
#     data = True
#     line_no =1
#     with open("file.txt", "r") as f:
#      while data:
#         data = f.readline()
#         if word in data:
#            print(line_no)
           
#         line_no += 1

#     return -1

# print(file_no())

# with open("file.txt", "w") as f:
#     print(f.write("Hello! my name is Apurwa Bhattarai \n I am awesome. \n I live in Dallas"))

# with open("file.txt", "r") as f:
#     content = f.read()

#     find = content.find("name")

#     print(find)
    
#     word = "name"
#     line_no = 1
#     for word1 in f:
#         if word in word1:
#             print(line_no)
#         line_no += 1

 
# import os

# word = "Dallas"
# line_no = 1

# with open("abc.txt", "r") as f:
#     for wrd in f:
#         wrd = wrd.replace("\\n", "\n")
#         if word in wrd: 
#             print("Dallas foun in line ", line_no)
#         line_no+=1
    

# word = "awesome"
# line = 1

# with open("file2.txt", "r") as source_file:
#    for wrd in source_file:
#       if word in wrd:
#          print("found ", line)
#       line +=1
      
# count = 0
# with open("file2.txt", "r") as count_line:
#     for cou in count_line:
#         count+=1
# print(count)

# with open("file2.txt", "r") as count_line1:
#     with open("file.txt", "w") as count_line2:

#         data = count_line1.read()
#         count_line2.write(data)
# print("success")  


# class student():
#     def __init__(self, name):
#         self.name = name

#     def hello(self):
#         print("Hi", self.name)

# s1 = student("apu")

# s1.hello()

# class student():
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def methCall(self):
#         total = 0
#         for mark in self.marks:
#             total += mark
        
#         print("Hi ", self.name, "your marks is ", total/3)

# student1 = student("Apurwa", [8,9,10]) 

# student1.methCall()

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account = acc

#     def debit(self, amount):
#         self.balance -= amount
#         print(amount, " is") 

# bal1 = Account(1000, 1234)
# print(bal1.account, bal1.balance)

# bal1.debit(5000)


# class Student():
#     def __init__(self, name, grades):
#         self.name = name
#         self.grades = grades

#     def stu_Info(self):
#         i =0
#         for mark in self.grades:
#             i += mark
#         print("result", i/3)

# s1 = Student("Apu", [98, 99, 100])
# s1.stu_Info()


# class A:
#     print("Welcome to A")

# class B:
#     print("Welcome to B")

# class C(A,B):
#     print("Welcome to C")

# C1 = A()

# print(C1)

# class Person():
#     def __init__(self, name = "", age=0):
#         self.name = name
#         self.age = age

#     def set_name(self, name):
#         self._name = name

#     def set_age(self, age):
#         self._age = age

#     def get_name(self):
#         return self._name

#     def get_age(self):
#         return self._age


# s1 = Person()

# s1.set_name("apu")
# s1.set_age(27)

# print(s1.get_name())
# print(s1.get_age())


# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return  22/7 * self.radius ** 2

#     def perimeter(self):
#         return  2 * 22/7 * self.radius 

# c1 = Circle(21)
# print(c1.area())
# print(c1.perimeter())

# class Employee():
#     def __init__(self, role, dept, salary):
#         self.role = role
#         self.dept = dept
#         self.salary = salary

#     def showDetails(self):
#         print("role = ", self.role)
#         print("dept = ", self.dept)
#         print("salary = ", self.salary)


# emp = Employee("account", "Finance", "80000")
# emp.showDetails()

# class vehicle():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def display_info(self):
#         print("make ", self.make)
#         print("model ", self.model)
#         print("year ", self.year)

# class Car(vehicle):
#     def start_engine(self):
#         print("Engine started")


# car1 = Car("Toyota", "Camry", "2022")
# car1.display_info()
# car1.start_engine()

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(Person):
#     def new_attribute(self, student_id):
#         self.student_id = student_id
#         print("name ",self.name, "age ", self.age, "student_id ", self.student_id  )

# per1 = Student("apu", "27")

# per1.new_attribute("11393917")

# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# class Student(Person):
#     def __init__(self, name, age, student_Id):
#         super().__init__( name, age)
#         self.student_Id = student_Id

#     def output(self):
#         print("name ", self.name, "age ", self.age, "student id ", self.student_Id)

# per1 = Student("Apu", "27", "11393917")
# per1.output()


# class Animal():
#     def speak(self):
#         print("Animal makes a sound")

# class Dog(Animal):
#     def speak(self):
#         print("Bark")

# animal1 = Dog()
# animal1.speak()


# class Person():
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
    
#     def greet(self):
#         print("Hello, my name is ", self.name)
#         print("your age and address is ", self.age,", ", self.address, "respectively.")
    
# class Student(Person):
#     def __init__(self, name, age, address, student_id):
#         super(). __init__(name, age, address)
#         self.student_id = student_id

#     def study(self):
#         print("I am studying")

# person1 = Student("Apurwa", "27", "Denton", "11393917")

# person1.greet()
# person1.study()


# class Animal():
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species

# class Dog(Animal):
#     def __init__(self, name, species, breed):
#         super().__init__(name, species)
#         self.breed = breed

# d1 = Dog("bunny", "canine", "chihuahua")

# print("name: ", d1.name, "--species: ", d1.species, "--breed: ", d1.breed)

# class Vehicle():
#     def start_engine(self):
#         print("engine started")

# class Car(Vehicle):
#     def start_engine(self):
#         print("Car engine started")

# car1 = Car()
# car1.start_engine()
    
# class Person():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Teacher(Person):
#     def __init__(self, name, age, subject):
#         super().__init__(name, age)
#         self.subject = subject

#     def teach(self):
#         print(self.name, " is teaching", self.subject)

# class Student(Person):
#     def __init__(self, name, age, student_id):
#         super().__init__(name, age)
#         self.student_ID = student_id

#     def study(self):
#         print(self.student_ID, " is studying class taught by ", self.name)

# class TeachingAssistant(Teacher, Student):
#     def __init__(self, name, age, subject, student_id):
#         Teacher.__init__(self, name, age, subject)
#         Student.__init__(self, name, age, student_id)


#     def help_student(self):
#         print("Helping the student")


# c1 = TeachingAssistant("apu", 27,"Phy", "11393917")
# c1.help_student()


# f = open("demo.txt", "a+")

# data = f.write("this1234")
# print(data)


# f.close()


# with open("demo1.txt", "r") as f:
#     data = f.read()
#     new_line = data.splitlines()
#     result = len(new_line)
#     result2 = len(data.split())
#     result3 = len(data) 

# print("line: ", result)
# print("word", result2)
# print("character: ", result3)


# info = {
#     "Name" : "Alice",
#     "Age" : 25,
#     "Country" : "USA"
# }

# print(info)
# print(info["Name"])
# print(info["Age"])
# print(info["Country"])

# book = {
#     "Title" : "The Great Gatsby",
#     "Author" :  "F.Scott Fitzgerald",
#     "Year" : 1925
# }

# book["ISBN"] = 1234

# print(book["Author"])
# print(book)


# travel = {
#     "city" : "Paris",
#     "population" : 2148000,
#     "country" : "France"
# }

# print(travel["population"])


# person = {
#     "name" : "Sarah",
#     "age" : 30,
#     "city" : "New York"
# }

# person["age"] = 31
# person["job"] = "Engineer"

# print(person)


# car = {
#     "make" : "Toyota",
#     "model" : "Corolla",
#     "year" : 2020
# }

# print(car["model"],", ", car["year"])

# grades = {
#     "Math" : 90,
#     "English" : 85,
#     "History" : 88
# }

# grades["subject"] = 90
# print(grades["English"])
# print(grades)

# person={
#     "first_name" : "Emma",
#     "last_name" : "Brown",
#     "age" : 27
# }

# del person["age"]

# print(person)

# contacts = {
#     "name" : "Jake", 
#     "phone" : "555-1234",
#     "email" : "jake@example.com"
# }

# if "email" in contacts:
#     print("Exist")
# else:
#     print("don't exist")

# product = {
#     "name" : "Laptop",
#     "price" : 800,
#     "stock" : 25
# }

# product["stock"] = 30
# product["price"] = 750

# print(product)

# students_grades = {
#     "Alice" : [88,92,79],
#     "Bob" : [75,85,90],
#     "Charlie" : [95, 100, 98]
# }

# def average_grade():
#     name = input("please enter student's name: ")
#     if name in students_grades:
#         scores1 = students_grades[name]
#         average = sum(scores1)/ len(scores1)
#         print(average)

# average_grade()

# inventory = {
#     "apple" : (30, 1.2),
#     "banana" : (45, 0.5),
#     "orange" : (20, 0.8)
# }


# def total_value():
#     val = input("Please enter your value: "). lower()
#     if val in inventory:
#         quantity, price = inventory[val]
#         result = quantity * price
#         print(result)


# total_value()

# student = {
#     "name" : "Alex",
#     "age" : 21,
#     "grade" : "A"
# }

# print(student)

# car = {
#     "brand" : "Tesla",
#     "model" : "Model 3",
#     "year" : 2022
# }

# car["color"] = "red"
# car["year"] = 2023

# del car["brand"]
# print(car)
# print(car["model"])


# fruits = {
#     "apple" : 5,
#     "banana" : 3,
#     "orange" : 2
# }

# for ele in fruits:
#     print({ele}, ":", {fruits[ele]})

# if "banana" in fruits:
#     print("Exist")
# else:
#     print("Don't Exist")

# value = fruits.get("banana", 0)
# print(value)

# colors = ["red", "blue", "red", "green", "blue", "blue"]
# store = {}

# for frequency in colors:
#     if frequency in store:
#      store[frequency] +=1
# else:
#     store[frequency] = 1

# print(store)    

# classroom = {
#     "John" : {"math": 85, "science":92},
#     "Emily" : {"math": 78, "science":88},
#     "Michael" : {"math": 90, "science":85}

# }
# classroom["Sarah"] = {"math" : 95, "science" : 89}

# print(classroom)

# print(classroom["Emily"])

# numbers = {1,2,3,4,5}
# store = {}

# for squ in numbers:
#     val = squ ** 2
#     store[squ] = val

#     print(store[squ])
# print(store)

# grades = {
#     "John" : 85,
#     "Emily" : 92,
#     "Michael" : 78,
#     "Sarah"  :89
# }

# sort = dict(sorted(grades.items(), key = lambda ite: ite[1], reverse = True))
# print(sort)


# def greet():
#     name = input("Please enter your name: ")
#     print("Hello,", name)

# greet()

# def square():
#     userInput = int(input("Please enter your number: "))
#     result = userInput ** 2
#     print("the square of your number is: ", result)

# square() 


# def sum_of_numbers(a, b):

#     sum = a+b
#     print(sum)

# sum_of_numbers(5,9)


# def personal_info(name, age, city):
#     print("Name: ", name, "Age:", age, "City: ", city)

# personal_info("apu", 27, "Dallas")

# def multiplt(a, b=1):
#     multiply_number = a * b
#     return multiply_number

# print(multiplt(2))

# def average_number(*args):
#  if args == 0:
#     return 0
#  return sum(args) / len(args)
    

# print(average_number(8))

# numbers = [1,2,3,4,5]
# squared = map(lambda x: x **2, numbers)
# print(list(squared))

# multiplt = lambda a, b: a *b

# print(multiplt(4,5))

# def outer():
#     def inner():
#         print("This is inner function. ")
#     inner()

# outer()

# def add_n(n):
#     def add(x):
#         return n + x
#     return add


# print(add_n(4)(7))


# class Book:
#     def __init__(self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def display_info(self):
#         print("Title", self.title)
#         print("Author", self.author)
#         print("Price", self.price)


# book1 =Book("The Great Gatsby", "Mark", "29.99")
# book1.display_info() 

# class Car:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def car_details(self):
#         print("Make: ", self.make)
#         print("Model: ", self.model)
#         print("year: ", self.year)

# car1 = Car("Toyota", "Camry", "2022")
# car1.car_details()

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         answer =self.length * self.width
#         print(answer)

#     def perimeter(self):
#         per= 2 * (self.length + self.width)
#         print(per)

# ob1 = Rectangle(5, 6)
# ob1.area()
# ob1.perimeter()

# class Vehicle:
#     def __init__(self, brand, model, year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def vehicle_info(self):
#         print("Brand", self.brand)
#         print("Model", self.model)
#         print("year", self.year)

# class Car(Vehicle):
#     def __init__(self, brand, model, year, fuel_type):
#         super().__init__(brand, model, year)
#         self.fuel_type = fuel_type
    
#     def car_info(self):
#         print("Fuel_type", self.fuel_type)

# Car1 = Vehicle("Toyota", "Camry", "2022")
# Car1.vehicle_info()
# Car2 = Car("Toyota", "Camry", "2022","Highlander")
# Car2.car_info()

# class Employee:
#     def __init__(self, name, emp_id, salary):
#         self.name = name
#         self.emp_id = emp_id
#         self.salary = salary
    
#     def show_details1(self):
#         print("name", self.name)
#         print("emp_id", self.emp_id)
#         print("salary", self.salary)

# class Manager(Employee):
#     def __init__(self, name, emp_id, salary, management):
#         super().__init__(name, emp_id, salary)
#         self.management = management

#     def show_details(self):
#         super().show_details1()
#         print("management", self.management)

# s1 = Manager("Apurwa", "11230", "165000", "Manager")

# s1.show_details()

# class A:
#     def show(self):
#         print("Class A")

# class B:
#     def show(self):
#         print("Class B")

# class C(A,B):
#     def show(self):
#         print("Class C")

# OBJ1 = C()
# OBJ1.show()


# store = []
# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def sound(self):
#         pass

# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         return "bark"

# class Cat(Animal):
#     def __init__(self, name):
#         super().__init__(name)

#     def sound(self):
#         return "meow"

# Animal = [Dog("Honey"), Cat("Minny"), Dog("Husky"), Cat("sandra")]

# for animals in Animal:
#     print([animals.name], [animals.sound()])



# class User:
#     def __init__(self, name):
#         self.name = name
#         self.borrowed_books = []
    
#     def borrow_books(self, book_name):
#         if len(self.borrowed_books)< self.borrowing_limit:
#             print(self.name, "has borrowed ", book_name)
#         else:
#             print(self.name, "hasn't borrowed anything ")
    
#     def return_book(self, book_name):
#         if book_name in self.borrowed_books:
#             print(self.name, "has returned ", book_name)
#         else:
#             print(self.name, "hasn't returned anything yet")
    
#     def display_book(self):
#         if self.borrow_books:
#             print(self.name, "has checked out these books".join(self.borrowed_books) )
#         else:
#             print("nothing is checked out")
    
#     def regularuser(User):
#         def __init__(self, name):
#             super().__init__(name)
#             self.borrowing_limit = 3

#     def Premiumuser(User):
#         def __init__(self, name):
#             super().__init__(name)
#             self.borrowing_limit = 5

#     books_list = ["book1", "book2", "book3", "book4", "book5", "book6"]
#     regularUser = regularuser("Alice")
#     premium_user = Premiumuser("Mike")

#     for book in books_list:
#         regularUser.borrow_books(book)

#     regularUser.display_books()
#     print("Hello")
            

# class Employee:
#     def __init__(self, name, employee_id, salary):
#         self.name = name
#         self.employee_id = employee_id
#         self.salary = salary

#     def calculate_bonus(self):
#         bonus = (10/100) * self.salary
#         total = bonus + self.salary
#         print("Your salary is increased by 10% " , bonus, "Your total salary is ", total)

#     def display_info(self):
#         print("name", self.name, " employee_id" ,self.employee_id," salary", self.salary)

# class Manager(Employee):
#         def __init__(self, name, employee_id, salary, team_size):
#             super().__init__( name, employee_id, salary)
#             self.team_size = team_size
            
#         def manager_bonus(self):    
#             if self.team_size > 10:
#                 bonus = (15 /100) * self.salary
#             else:
#                 self.team_size < 10
#                 bonus = (10 / 100) * self.salary
#             total = self.salary + bonus
#             print("Your bonus is " , bonus, "your total is", total)

# class Developer(Employee):
#         def __init__(self, name, employee_id, salary, programming_language):
#             super().__init__( name, employee_id, salary)
#             self.programming_language = programming_language
            
#         def developer_bonus(self):    
#             bonus = (12/100) * self.salary
#             total = bonus + self.salary
#             print("Your salary is increased by 12% " , bonus, "Your total salary is ", total)

# class Intern(Employee):
#         def __init__(self, name, employee_id, salary, duration):
#             super().__init__( name, employee_id, salary)
#             self.duration = duration
            
#         def intern_bonus(self):    
#             if self.duration > 3:
#               bonus = (5/100) * self.salary
#               print("Bonus awarded", bonus)
#             else:
#              print("No bonus")


# obj1 = Employee("Apu", 1111, 102000)
# obj1.display_info()
# obj1.calculate_bonus()

# obj2 = Manager("mike", 2222, 105000, 9)
# obj2.manager_bonus()

# obj3 = Developer("Ashley", 333, 120000, "Python")
# obj3.developer_bonus()

# obj4 = Intern("Henry", 444, 55000, 2)
# obj4.intern_bonus()

# class LibraryItem:
#     def __init__(self, title, author, item_id, available):
#         self.title = title
#         self.author = author
#         self.item_id = item_id
#         self.available = available

#     def borrow(self):
#         if self.title in items_available:
#             print(self.title, "is Available")
#         else:
#             print(self.title, "is not Available")


# class Book(LibraryItem):
#     def __init__(self, title, author, item_id, available, num_pages):
#         super().__init__(title, author, item_id, available)
#         self.num_pages = num_pages

#     def get_summary(self):
#         if self.title in items_available:
#             print("Title:", self.title, "Author:", self.author, "Item ID:", self.item_id, "Available:", self.available)


# class DVD(LibraryItem):
#     def __init__(self, title, author, item_id, available, duration, region_code):
#         super().__init__(title, author, item_id, available)
#         self.duration = duration
#         self.region_code = region_code

#     def get_summary(self):
#         print("Title:", self.title, "Author:", self.author, "Duration:", self.duration)


# class SpecialCollection(Book, DVD):
#     def __init__(self, title, author, item_id, available, num_pages, duration, region_code, old):
#         Book.__init__(self, title, author, item_id, available, num_pages)  # Initialize Book part
#         DVD.__init__(self, title, author, item_id, available, duration, region_code)  # Initialize DVD part
#         self.old = old

#     def borrow(self):
#         print("Please check at the front desk")


# # Test
# obj2 = SpecialCollection("Chemistry", "Mike", 235, True, 58, 120, 5, 8)
# obj2.borrow()


class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        amount += self.balance
        print(amount)

    def withdraw(self, withdraw_amount):
        self.balance = self.balance - withdraw_amount
        print(self.balance)

    def get_balance(self):
        print("Your current balance is: ", self.balance, "Thank You for visiting." )

obj1 = BankAccount(112, 51000)

obj1.deposit(5)
obj1.withdraw(5)
obj1.get_balance()


        