# def addition_table(given_number):
#     iterated_number = 1
#     my_sum = 1
#     while iterated_number<= 5:
#         my_sum=given_number+iterated_number
#         if my_sum> 20:
#             break
        
         
#         print(str(given_number),"+",str(iterated_number),"=",str(my_sum))
#         iterated_number +=1

# addition_table(5)




# def addition_table(given_number):
#     iterated_number = 1
#     my_sum = 1
#     while iterated_number<= 16:
#         my_sum=given_number+iterated_number
#         if my_sum> 20:
#             break
        
         
#         print(str(given_number),"+",str(iterated_number),"=",str(my_sum))
#         iterated_number +=1

# print("Hello")



# name = "Sasha"
# color = 'Gold'

# place = "cambridge"

# Pet = ""
# name = "Sasha"
# color = 'Gold'
# print("Name: " + name  + ", Favourite color: " + color)

# "example" * 3


# pet = "loooooooooooooog cat"
# len(pet)

# name = "Pramod"
# print(name[1])
# print(name[3])
# print(name[5])

# text = "Random string with a lot of characters"
# print(text[-1])
# print(text[-2])
# print(text[-3])
# print(text[-4])

# print(text[1])
# print(text[2])
# print(text[3])
# print(text[4])




# color = "Orange"
# color[1:4]
# print(color[:+1])
# print(color[:+2])
# print(color[:+3])
# print(color[:+4])
# print(color[:+5])
# print(color[:+6])

# print(color[1:])
# print(color[2:])
# print(color[3:])
# print(color[:+4])
# print(color[:+5])
# print(color[:+6])
# fruit = "Mangosteen"
# print(fruit[0:10])
# print(fruit[:15])

# print(fruit[:5]+ fruit[5:])

# message = "A kong string with a silly type."
# print(message[2])

# new_message= message[0:2] + "l"+ message[3:]
# print(new_message)

# new_message= message[0:2] 
# print(new_message)

# new_message= message[0:2] + "l"
# print(new_message)

# new_message= message[3:]
# print(new_message)

# message= "This is a new message"
# print(message)
# message = "Add another one" 
# print (message)
# message= "This is real fun"
# print (message)

# pets = "Cats & Dogs "
# print (pets.index ("&"))

# print("Dragon" in pets)
# print ("Cats" in pets)

# pets="Cats & Dogs"
# "Dragons" in pets
# "Cats" in pets


# def replace_domain(email, old_domain, new_domain):
#   if "@" + old_domain in email:
#     index = email.index("@" + old_domain)
#     new_email = email[:index] + "@" + new_domain
#     return new_email
#   return email

# animals = "lions tigers and bears"
# print(animals.index("g"))
# print(animals.index("bears"))
# print("horses" in animals)
# print("tigers" in animals)

# print("Mountains".upper())
# print("Mountains".lower())

# print("p.g sadavarte".upper())
# print("P G SADAVARTE".lower())

# answer = "YES"
# if answer.lower() == "yes":
#   print("User said yes")

#   print(" yes ".strip())

#   print(" yes ".strip())
#   print(" yes ".lstrip())
#   print(" yes ".rstrip())

# print("The number of times e occurs in this string is 4".count("e"))
# print("Forest".endswith("rest"))

# print("12345".isnumeric())

# print(int("12345")+int("54321"))

# print(" ".join(["This", "is", "a", "phrase", "joined", "by", "spaces"]))
# print("..".join(["This", "is", "a", "phrase", "joined", "by", "double", "dots"]))
# print("This is another example".split())

# name = "Pramod Sadavarte"
# number = len(name) * 4
# print("Hello {}, your lucky number is {}".format(name,number))

# name = "Pramod Sadavarte"
# print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))

# price = 7.5
# with_tax = price * 1.09
# print(price, with_tax)
# print("Base price: Rs{:.2f}. With Tax: Rs{:.2f}".format(price, with_tax))

# def to_celsius(x):
#   return (x-32)*5/9

# for x in range(0,101,10):
  # print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))

# print(len("abcdefgh"))

# for c in "abcdefg":
#    print(c)
# print("abc" in "abcde") 
# print("def" in "abcde") 

# print("abcdef" [0:2])
# print("abcdefgh"[2:-4])

# print("AaBbCcDdEe".upper())
# print("AaBbCcDdEe".lower())

# print("  Hello  ".lstrip())
# print("  Hello  ".rstrip())
# print("  Hello  ".strip())

# test = "How much wood would a woodchuck chuck"
# # test = "How-much-wood-would-a-woodchuck-chuck"
# print(test.count("much"))


# print("12345".isnumeric())
# print("-123.45".isnumeric())
# print("xyzzy".isalpha())
# # print(test.split())
# print(test.split("-"))
# print(test.replace("wood", "plastic"))

# print("-".join(test.split()))

# basket = ("Peaches", 3.0, 2.99),("Pears", 5.0, 1.66),("Plums", 2.5, 3.99),("Apples",3,4.25)
# subtotal = 0.00
# for item in basket: 
#         fruit ,weight, unit_price = item
#         subtotal += (weight * unit_price)
# tax_rate = 0.06625
# tax_amt = subtotal * tax_rate
# total = subtotal + tax_amt

# print("Subtotal:", subtotal)
# print("Sales Tax:", tax_amt)
# print("Total:", total)

# print("Subtotal:  Rs{:10,.2f}".format(subtotal))
# print("Sales Tax: Rs{:10,.2f}".format(tax_amt))
# print("Total:     Rs{:10,.2f}".format(total))


# def mirrored_string(my_string):
#     forwards = ""
#     backwards = ""
#     for character in my_string:
#         if character.isalpha():
#             forwards += character
#             backwards = character + backwards
#     if forwards.lower() == backwards.lower():
#         return True
#     return False
# print(mirrored_string("12 Noon"))
# print(mirrored_string("Was it a car or  a cat I saw"))
# print(mirrored_string("'eve, Madam Eve")) 


# def convert_weight(ounces):
#     pounds = ounces/16
#     result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
#     return result
# print(convert_weight(12))
# print(convert_weight(50.5))
# print(convert_weight(16))

# def convert_height(cms):
#     inches = cms/2.54
#     result = "{} cms equals {:.2f} inches".format(cms,inches)
#     return result
# print(convert_height(25.4))

# def username(last_name, birth_year):
#     return("{}{}".format(last_name[0:5],birth_year))
# print(username("Avani Sadavarte", "2014"))
# print(username("Seema Sadavarte,", "1957"))
# print(username("Pramod Sadavarte", "1957"))

# def replace_date(schedule, old_date, new_date):
#     if schedule.endswith(old_date):
#         p = len(old_date)
#         new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)
#         return new_schedule
#     return schedule
# print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
 
# LIST STARTS 
# fruits = ["Pineapple", "Banana", "Apple", "Melon"]
# fruits.append("Kivi")
# print(fruits)
# fruits.insert(0,"orange")
# print(fruits)
# fruits.insert(25, "Peach")
# print(fruits)
# fruits.remove("Melon")
# print(fruits)
# fruits.pop(0)
# print(fruits)
# fruits[1]="Strawberry"
# print(fruits) 

# fullname = ('Grace', 'M', 'Hopper')
# print(fullname [0:3])
# first,middle,last = fullname
# print(last)
# full_name_string = ' '.join(fullname)
# print(full_name_string)

# def convert_seconds(seconds):
#   hours = seconds // 3600
#   minutes = (seconds - hours * 3600) // 60
#   remaining_seconds = seconds - hours * 3600 - minutes * 60
#   return hours, minutes, remaining_seconds
# result = convert_seconds(5000)
# print(result)
# type(result)

# def convert_seconds(seconds):
#   hours = seconds // 3600
#   minutes = (seconds - hours * 3600) // 60
#   remaining_seconds = seconds - hours * 3600 - minutes * 60
#   return hours, minutes, remaining_seconds
# result = convert_seconds(5000)
# hours, minutes, seconds = result
# print(hours, minutes, seconds)

# def convert_seconds(seconds):
#   hours = seconds // 3600
#   minutes = (seconds - hours * 3600) // 60
#   remaining_seconds = seconds - hours * 3600 - minutes * 60
#   return hours, minutes, remaining_seconds
# hours, minutes, seconds = convert_seconds(1000)
# print(hours, minutes, seconds)

# def file_size(file_info):
# 	___, ___, ___= file_info
# 	return("{:.2f}".format(___ / 1024))

# print(file_size(('Class Assignment', 'docx', 17875))) 
# print(file_size(('Notes', 'txt', 496))) 
# print(file_size(('Program', 'py', 1239))) 

# animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
# chars = 0
# for animal in animals:
#   chars += len(animal)

# print("Total characters: {}, Average length: {}".format(chars, chars/len(animals)))
    
# winners = ["Pramod","Sagar","Akash","Avani","Kaivalya"]
# for index, person in enumerate(winners):
#   print("{} - {}".format(index +1 , person))

# def full_emails(people):
#   result = []
#   for email, name in people:
#     result.append("{} <{}>".format(name, email))
#   return result
# print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))

# my_list = ['a', 'b', 'c']
# index = 0
# for item in my_list:
#     print(f"{index +1 }: {item}")
#     print("{}-{}".format(index+1,item))
#     print(f"index{index+1} -{item}")
#     index += 1

# fruits = ["apple", "banana", "cherry", "date"]

# # Using enumerate()

# for index, fruit in enumerate(fruits,start=1):
#     print(f"Index {index}:{fruit}")

# students = ["Alice", "Bob", "Charlie"]
# for rank, name in enumerate(students, start=1):
#     print(f"Rank {rank}: {name}")

# letters = list("python")
# indexed_letters = list(enumerate(letters))

# print(indexed_letters)

# multiples = []
# for x in range(1,11):
#   multiples.append(x*7)

# print(multiples)

# multiples = [x*7 for x in range(1,11)]
# print(multiples)

# languages = ["Python", "Perl", "Ruby", "Go", "Java", "C"]
# lengths = [len(language) for language in languages]
# print(lengths)

# z = [x for x in range(0,101) if x % 8 == 0]
# print(z)

# def odd_numbers(n):
# 	return [x for x in range (1,n+1) if x % 2!=0]

# print(odd_numbers(15)) # Should print [1, 3, 5]
# print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]

even_no = []
for x in range (1,11):
     even_no.append(x*2)
print(even_no)

even_no = [x * 2 for x in range(1, 11)]
print(even_no)

# List Comprehension examples
# numbers = [(1, 2, 3,4,5) for _ in range(3)]
# print (numbers)

# varying_nums = [(i, i * 2, i ** 2,i**2) for i in range(3)]
# print(varying_nums)

# varying_nums = [(i, i + 2, i+2+2,) for i in range(3)]
# print(varying_nums)

# for number in range(2, 100, 11):
#     answer = number+11 
#     print(f" {number }  +   11  :    {answer}") 

# print("List comprehension result:")
# print([x*2 for x in range(1,11)])

# print("Long form code result:")
# my_list = []
# for x in range(1,11):
#     my_list.append(x*2)
# print(my_list)

# print("List comprehension result:")
# print([x for x in range(1,101) if x % 10 == 0])

# print("Long form code result:")
# my_list = []
# for x in range(1,101):
#     if x % 10 == 0:
#         my_list.append(x)
# print(my_list)



# def squares(a ,b):
#     return(a**2,b**2)

# print(squares(2, 3))
# print(squares(1, 5)) 
# print(squares(0, 10)) 

# def cubes(a ,b):
#     return(a**3,b**3)
# print(cubes(2,5))

# def value(a,b):
#     return(a**4,b**3)
# print(value(2,4))

# Study Guide: list operations & method 


#  list[index] = x Replaces the element at index [n] with x.
# list.append(x) - Appends x to the end of the list.
# list.insert(index, x) - Inserts x at index position [index].
# list.pop(index) - Returns the element at [index] and removes it from the list.
#  If [index] position is not in the list, the last element in the list is returned and removed.
# list.remove(x) - Removes the first occurrence of x in the list.
# list.sort() - Sorts the items in the list.
# list.reverse() - Reverses the order of items of the list.
# list.clear() - Deletes all items in the list.
# list.copy() - Creates a copy of the list.
# list.extend(other_list) - Appends all the elements of other_list at the end of list
# map(function, iterable) - Applies a given function to each item of an iterable (such as a list) and returns a map object with the results
# zip(*iterables) - Takes in iterables as arguments and returns an iterator that generates tuples, where the i-th tuple contains the i-th element from each of the argument iterables.

# The tuple() operator

# my_list = [1, 2, 3, 4]
# my_tuple = tuple(my_list)

# print(my_tuple)  # Outputs: (1, 2, 3, 4)

# my_tuple = 1, 2, 3, 4
# print(my_tuple)

# my_tuple = (1, 2, ['a', 'b', 'c'])
# my_tuple[2][1] = 'x'
# print(my_tuple) 

# # Returning multiple values from functions
# def calculate_number(a , b ,c):
#     return a+b,a-b,a*b,a/b,a+c,a-c,a*c,a/c,b+c,b-c,b*c,b/c
# result = calculate_number(8 , 5, 2)
# print(result)

# my_list = [ x*2 for x in range(1,11) ]
# print(my_list)

# my_list = [ x for x in range(1,101) if x % 11 == 0 ] 
# print(my_list)

# Skill Group 1
# years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]
# updated_years = []
# for year in years:
#     if year.endswith("2023"):
#         new = year.replace("2023","2024")
#         updated_years.append(new)
#         # print(updated_years)
#     else:
#         updated_years.append(year)
# print(updated_years)

# # SKILL GROUP 2

# def squares(start, end):
#     return [n*n for n in range(start,end+1)]
# print(squares(2, 3))
# print(squares(1, 5))
# print(squares(0, 10))

# # SKILL GROUP 3
# years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]
# print(updated_years) 

# # SKILL GROUP 4
# def change_string(given_string):
#     new_string = ""
#     new_list = given_string.split()
#     for element in new_list:
#         new_string += element[1:] + "-" + element[0] + " "
#     return new_string
# print(change_string("1one 2two 3three 4four 5five")) # Should print "one-1 two-2 three-3 four-4 five-5"  

# # SKILL GROUP 5
# def list_elements(list_name, elements):
#     return "The " + list_name + " list includes: " + ", ".join(elements)
# print(list_elements("Printers", ["Color Printer", "Black and White Printer", "3-D Printer"]))

# # SKILL GROUP 6

# def add_one(number):
#     return number + 1
# numbers = [1, 2, 3, 4, 5]
# result = map(add_one, numbers)
# print(list(result))

# # SKILL GROUP 7

# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]
# # Use zip to combine the lists
# combined = zip(names , ages)
# print(list(combined))









