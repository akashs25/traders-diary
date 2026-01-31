# hotel_room = 100
# tax = hotel_room *0.08
# total = hotel_room + tax
# room_guest = 4
# share_per_person = total/room_guest
# print("Each person need to pay: " + str(share_per_person))

# salutation ="Dr"
# first_name ="Prisha"
# middle_name = "Jai"
# last_name = "Agarwal"
# suffix = "Ph.D"
# print(salutation,first_name, middle_name ,last_name," ,",suffix)

# salutation ="Mr"
# first_name = "Pramod"
# middle_name = "Govind"
# last_name = "Sadavarte"
# suffix = "B.E.civil"
# print(salutation,first_name, middle_name ,last_name," ,",suffix)

# salutation ="Mrs"
# first_name = "Seema"
# middle_name = "Pramod"
# last_name = "Sadavarte"
# suffix = "B.Com"
# print(salutation,first_name, middle_name ,last_name," ,",suffix)


# def greeting(name):
#     print("Welcome, " + name )
# greeting ("Pramod")
# greeting ("Akash")
# greeting ("Sagar")

# def greeting(name, departmant):
#     print("Welcome, " +name)
#     print("you are part of " + departmant)
# greeting("Veena", "Civil engineering")
# greeting("Prachi", "Software engineering")

# def greeting(name, designation,department):
#     print("Welcome, " +name)
#     print("You are " +designation)
#     print("you are part of " + department)
# greeting("Veena","Professor","Civil Engineering")

# month = "December"
# print("Investigate failed log in attempts during", month, "if more than", 100)
# type("security")
# type("7")
# print(type("this is a string"))
# number =12
# string_representation = str(number)
# print(string_representation)

# time_list =[12,2,32,18,57,22,14]
# print(sorted(time_list))
# print(time_list)
# print(min(time_list))
# print(max(time_list))
# print("The sum of both the areas is:" + str(sum))

# def convert_seconds(seconds):
#     hours = seconds//3600
#     minuits = (seconds-hours*3600)//60
#     remaining_seconds =seconds-hours*3600-minuits*60
#     return hours,minuits,remaining_seconds

# hours, minuits,seconds = convert_seconds(5000)
# print(hours, minuits, seconds)

# def greeting(name):
#     print("Welcome,  " +name)
# result = greeting("Pramod")

# def find_total_days(years,months,days):
#     my_days = (years*365)+ (months*30)+ days
#     return my_days
# print(find_total_days(2,5,23))


# def convert_volume (fluid_ounce):
#     ml = fluid_ounce* 29.5
#     return ml
# print("The volume in mililitres is" + str(convert_volume(2)))
# print("The volume in mililitres is" + str(convert_volume(2)*2))

# def circle_area(radius):
#     pi =3.14
#     area = pi *(radius**2)
#     print(area)
# circle_area(5)

# def convert_distance(Km):
#     meters = Km * 1000
#     return meters
# my_trip_kilometers = 55
# my_trip_meters =1000*(my_trip_kilometers)
# print("The distance in meters is  " +str(convert_distance(55)))

# def seconds(hours,minuits,seconds):
#     seconds=(hours*3600)+(minuits*60)+seconds
#     return seconds
# print(seconds(1,2,3))

# print(10>1)
# print(3<5)
# print(10*5>5*5)
# print("cat"=="dog" )
# print(1 !=2)

# print(1<"1")
# print("yellow">"cyan"& "red"<"orange")
# print(25>50 or 1!=2)
# print(not 42 =="Answer")

# my_variable = 3*5
# print(my_variable)
# print(my_variable==3*5)
# print("M">"A")
# print("A"<"M")
# print("Sunday">"Friday")

# print("pramod">="pramod")
# print("pramod" > "pramod")

# var1 ="my computer">="my chair"
# var2 ="spring"<="winter"
# var3="pramod">="pramod"


# print("Is\"my computer\"greater than or equal to \"my chair\"? result: ", var1) 
# print("Is\"spring\"less than ot equal to \"winter\" ? Result: ", var2 )
# print("Is \"pramod\" more than or equal to \"pramod\" ? Result: " ,var3)

# x =2*3>6
# print("The value of x is : ")
# print(x)
# print("")
# print("The inverse value of x is : ")
# print(not x)

# x =2*3>=6
# print("The value of x is : ")
# print(x)
# print("")
# print("The inverse value of x is : ")
# print(not x)

# today = "Monday"
# print(not today =="Tuesday")

# def hint_username(username):
#     if len(username)<3:
#         print("Invalid username.must be at least 3 characters long")
#         print("valid username")

# def is_even(number):
#     if number / 2 ==0:
#         return True
#     return false

# def hint_username(username):
#     if len(username) < 3:
#         print("Invalid username.Must be at least 3 characters long")
#     elif len(username) >15:
#         print("Invalid username.Must be at least 15 characters long")
#     else:
#         print("valid username")
#
# print(10*4>14+23)
# print("tall"<"short")

# def translate_error_code(error_code):
#     if error_code == "401 Unauthorized":
#         traslation="Server received an unauthenticated request"
#     elif error_code == "404 Not Found":
#         traslation ="Requested web page not found on server"
#     elif error_code == "408 Request Timeout":
#         traslation = "Server request to close unused connection"
#     else:
#         traslation ="Unknown error code"
#     return traslation
# print(translate_error_code("408 Request Timeout"))
        
# number =25
# if number <=5:
#     print("The no is 5 or smaller.")
# elif number == 33:
#     print("The number is 33")
# elif number <32 & number >=6:
#     print("The number is less than 32 & greater than 6")
# else:
#     print("The number is " +str (number))

# def round_up(number):
#     x=10
#     whole_number = number//x
#     print(whole_number)
#     remainder = number% x
#     print(remainder)
#     if remainder >=5:
#         return x*(whole_number+1)
    
#     return x*whole_number
# print(round_up(55))

# def task_reminder(time_as_string):
#     if time_as_string =="8:00 a.m.":
#         task = "Check overnight backup images"
#     elif time_as_string == "11:30 a.m.":
#         task = "Run TPS report"
#     elif time_as_string == "5:30 p.m.":
#         task = "Robot servers"
#     else:
#         task = "Provide IT Support to employees"
#     return task
# print(task_reminder("10:00 a.m."))

#Example 1
def product(a,b):
    return(a*b)
print(product(product(2*2,4),product(3,5)))

def difference(a,b):
    return(a-b)


def sum(a,b):
    return(a+b)
print(difference(sum(2,2),sum(4,4)))

print((5>=2*4)&(5<=4*3))

x=3
if x+5>x**2 or x % 4 !=0:
    print("This comparision is true")

number = 6
if number *2 < 14:
    print(number *6%3)
elif number > 7:
    print(100 / number)
else:
    print(7 -number)

def get_remainder (x, y):
    if x==0 or y == 0 or x ==y:
        remainder = 0
    else:
        remainder = (x % y)/y
    return remainder
print(get_remainder(10, 3))




  



 