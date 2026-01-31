# Python Learning Journey - Code Documentation

This document contains comprehensive documentation of all Python code written in this workspace.

---

## Table of Contents
1. [practice.py - Dictionary Operations & Sequence Generation](#practicepy)
2. [test.py - Basic Python Fundamentals](#testpy)
3. [test1.py - Functions, Conditionals & Operators](#test1py)
4. [test3.py - Loops, Strings & String Operations](#test3py)
5. [test4.py - Advanced Strings, Lists & Comprehensions](#test4py)
6. [texttovoice.py - Text-to-Speech Implementation](#texttovoicepy)
7. [Gann_Square_7x7.csv - Data File](#data-files)

---

## practice.py

### Dictionary Operations

**Purpose**: Learning and practicing Python dictionary manipulation and iteration.

#### Key Concepts Covered:

1. **Basic Dictionary Iteration**
   - Iterating over dictionary keys
   - Iterating over key-value pairs using `.items()`
   - Accessing `.keys()` and `.values()` methods

2. **Letter Counter Function**
   ```python
   def count_letters(text):
       result = {}
       for letter in text:
           if letter not in result:
               result[letter] = 0
           result[letter] += 1
       return result
   ```
   - Creates a frequency dictionary of characters in a string
   - Used on examples: "aaaaa", "tenant", "a long string with a lot of letters"

3. **Commented Out: Sequence Generation**
   - Code for generating unique arithmetic sequences
   - Parameters: START_MIN=1, START_MAX=9, INCREMENT_MIN=2, INCREMENT_MAX=15
   - Would generate sequences up to MAX_END_VALUE=100

**Learning Outcomes**: Understanding dictionary operations, iteration patterns, and character counting algorithms.

---

## test.py

### Basic Python Fundamentals

**Purpose**: Introduction to Python basics including I/O, arithmetic operations, and string manipulation.

#### Programs Included:

1. **User Input and Output**
   ```python
   NAME = input("P G Sadavarte")
   print("entered name is", NAME)
   ```

2. **Geometric Calculations**
   - **Triangle Area Calculator**
     - Formula: area = (base × height) / 2
     - Example: base=6, height=3 → area=9
   
   - **Rectangle Area Calculator**
     - Formula: area = base × height
     - Example: base=10, height=8 → area=80

3. **String Operations**
   - String concatenation: `"a"+"b"+"c"`
   - Mixed data type printing
   - Type conversion using `str()`

**Learning Outcomes**: Basic I/O operations, arithmetic calculations, type conversion, and string concatenation.

---

## test1.py

### Functions, Conditionals & Operators

**Purpose**: Advanced functions, conditional logic, comparison operators, and control flow.

#### Major Sections:

### 1. Commented Examples (Learning Archive)

Includes various commented code blocks covering:
- Hotel room cost splitting calculations
- Name formatting with salutation and suffix
- Greeting functions with parameters
- Type checking and conversions
- List operations (sorted, min, max, sum)
- Time conversion functions
- Volume conversion (fluid ounces to milliliters)
- Circle area calculations
- Distance conversions (km to meters)
- Comparison operators
- Logical operators (and, or, not)
- If-elif-else conditionals
- Error code translation functions
- Number rounding functions
- Task reminder systems

### 2. Active Functions

**Mathematical Operations:**
```python
def product(a, b):
    return (a * b)

def difference(a, b):
    return (a - b)

def sum(a, b):
    return (a + b)
```

**Modular Arithmetic:**
```python
def get_remainder(x, y):
    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder
```

### 3. Logical Expressions

Examples of complex boolean expressions:
- `(5 >= 2*4) & (5 <= 4*3)`
- Conditional branching with multiple conditions
- Nested function calls: `product(product(2*2, 4), product(3, 5))`

**Learning Outcomes**: Function definition, parameter passing, return values, conditional logic, boolean algebra, and operator precedence.

---

## test3.py

### Loops, Strings & String Operations

**Purpose**: Mastering loops (while and for), string manipulation, and iteration patterns.

#### Major Sections:

### 1. While Loops (Commented Examples)

- Counter loops with increments
- Attempt tracking functions
- Sum and product calculations
- Countdown functions
- Division by 2 patterns
- Range printing
- Multiplier tables
- Factor counting functions
- Addition tables with break conditions

### 2. For Loops

**Range-based Iteration:**
```python
for x in range(5):
    print(x)
```

**List Iteration:**
```python
friends = ['Akash', 'Pramod', 'Sagar']
for friend in friends:
    print("Hi " + friend)
```

**Statistical Calculations:**
- Sum and average calculations
- Product of range
- Temperature conversion (Fahrenheit to Celsius)

**Advanced Range Usage:**
- `range(start, stop, step)` patterns
- Reverse iterations: `range(2, -2, -1)`
- Even number generation: `range(0, 11, 2)`

### 3. Nested Loops

```python
for left in range(7):
    for right in range(left, 7):
        print("[" + str(left) + "!" + str(right) + "]", end=" ")
```

### 4. String Operations

**String Indexing and Slicing:**
```python
string1 = "Greetings,Earthlings"
# Indexing: string1[0], string1[1], etc.
# Slicing: string1[4:21], string1[10:], string1[:21]
# Negative indexing: string1[-10:]
```

### 5. List Comprehensions

```python
numbers = [1, 2, 3]
squared_number = [x**2 for x in numbers]
```

**Learning Outcomes**: While loops, for loops, nested loops, range function, string indexing/slicing, list comprehensions.

---

## test4.py

### Advanced Strings, Lists & Comprehensions

**Purpose**: Advanced string methods, list operations, tuples, and functional programming concepts.

#### Major Sections:

### 1. String Methods (Commented Examples)

- `.upper()` and `.lower()` - Case conversion
- `.strip()`, `.lstrip()`, `.rstrip()` - Whitespace removal
- `.count()` - Character counting
- `.endswith()` - Suffix checking
- `.isnumeric()`, `.isalpha()` - Type checking
- `.join()` and `.split()` - String/list conversion
- `.format()` - String formatting
- `.index()` - Finding substrings
- `.replace()` - String replacement

### 2. String Formatting Examples

**Basic Formatting:**
```python
name = "Pramod Sadavarte"
number = len(name) * 4
print("Hello {}, your lucky number is {}".format(name, number))
```

**Named Placeholders:**
```python
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))
```

**Decimal Formatting:**
```python
print("Base price: Rs{:.2f}. With Tax: Rs{:.2f}".format(price, with_tax))
```

**Aligned Formatting:**
```python
print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
```

### 3. Practical Functions

**Palindrome Checker:**
```python
def mirrored_string(my_string):
    forwards = ""
    backwards = ""
    for character in my_string:
        if character.isalpha():
            forwards += character
            backwards = character + backwards
    if forwards.lower() == backwards.lower():
        return True
    return False
```

**Unit Converters:**
- `convert_weight(ounces)` - Ounces to pounds
- `convert_height(cms)` - Centimeters to inches

**Username Generator:**
```python
def username(last_name, birth_year):
    return("{}{}".format(last_name[0:5], birth_year))
```

### 4. Lists and Tuples

**List Operations:**
```python
fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.append("Kivi")
fruits.insert(0, "orange")
fruits.remove("Melon")
fruits.pop(0)
fruits[1] = "Strawberry"
```

**Tuple Unpacking:**
```python
fullname = ('Grace', 'M', 'Hopper')
first, middle, last = fullname
```

**Time Conversion with Tuples:**
```python
def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
```

### 5. Enumerate Function

**Basic Usage:**
```python
winners = ["Pramod", "Sagar", "Akash", "Avani", "Kaivalya"]
for index, person in enumerate(winners):
    print("{} - {}".format(index + 1, person))
```

**Email Formatting:**
```python
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{} <{}>".format(name, email))
    return result
```

### 6. List Comprehensions

**Basic Comprehension:**
```python
multiples = [x*7 for x in range(1, 11)]
```

**With Conditions:**
```python
z = [x for x in range(0, 101) if x % 8 == 0]
```

**Odd Numbers Function:**
```python
def odd_numbers(n):
    return [x for x in range(1, n+1) if x % 2 != 0]
```

### 7. Active Code - Even Numbers

**Long Form:**
```python
even_no = []
for x in range(1, 11):
    even_no.append(x*2)
print(even_no)
```

**List Comprehension:**
```python
even_no = [x * 2 for x in range(1, 11)]
print(even_no)
```

### 8. Advanced Functions

**Tuple Generation:**
```python
def squares(a, b):
    return (a**2, b**2)

def cubes(a, b):
    return (a**3, b**3)
```

**Multiple Return Values:**
```python
def calculate_number(a, b, c):
    return a+b, a-b, a*b, a/b, a+c, a-c, a*c, a/c, b+c, b-c, b*c, b/c
```

### 9. Skill Groups (Practice Exercises)

**Group 1 - Year Replacement:**
```python
years = ["January 2023", "May 2025", ...]
updated_years = []
for year in years:
    if year.endswith("2023"):
        new = year.replace("2023", "2024")
        updated_years.append(new)
    else:
        updated_years.append(year)
```

**Group 2 - Squares Function:**
```python
def squares(start, end):
    return [n*n for n in range(start, end+1)]
```

**Group 3 - Comprehension with Conditionals:**
```python
updated_years = [year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years]
```

**Group 4 - String Manipulation:**
```python
def change_string(given_string):
    new_string = ""
    new_list = given_string.split()
    for element in new_list:
        new_string += element[1:] + "-" + element[0] + " "
    return new_string
```

**Group 5 - String Joining:**
```python
def list_elements(list_name, elements):
    return "The " + list_name + " list includes: " + ", ".join(elements)
```

**Group 6 - Map Function:**
```python
def add_one(number):
    return number + 1
numbers = [1, 2, 3, 4, 5]
result = map(add_one, numbers)
```

**Group 7 - Zip Function:**
```python
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
combined = zip(names, ages)
```

**Learning Outcomes**: String methods, formatting, list/tuple operations, enumerate, comprehensions, map/zip functions, and functional programming patterns.

---

## texttovoice.py

### Text-to-Speech Implementation

**Purpose**: Convert text to speech using Google Text-to-Speech (gTTS) library.

#### Implementation:

```python
from gtts import gTTS
import os

text = "Hello, Hi kaivalya welcome and how are you?"
tts = gTTS(text=text, lang='en')
tts.save("welcome.mp3")
os.system("start welcome.mp3")  # Plays the file on Windows
```

#### Components:

1. **Import Libraries**
   - `gTTS`: Google Text-to-Speech library
   - `os`: Operating system interface for file operations

2. **Text Definition**
   - Greeting message: "Hello, Hi kaivalya welcome and how are you?"

3. **TTS Conversion**
   - Language: English ('en')
   - Output format: MP3 audio file

4. **File Operations**
   - Saves audio as "welcome.mp3"
   - Automatically plays the file on Windows using `os.system()`

**Learning Outcomes**: External library usage, text-to-speech conversion, file I/O, and OS command execution.

---

## Data Files

### Gann_Square_7x7.csv

**Purpose**: Numerical data storage in CSV format.

**Structure**: 7x7 matrix of floating-point numbers

**Sample Data:**
```
1227.81, 1219.07, 1210.35, 1201.67, 1193.02, 1184.4, 1175.81
1236.59, 1058.86, 1050.74, 1042.65, 1034.6, 1026.57, 1167.26
...
```

**Characteristics**:
- Contains 49 numerical values (7 rows × 7 columns)
- Values range approximately from 932 to 1335
- Appears to follow a specific pattern (possibly Gann Square analysis data)
- Could be used for financial/trading analysis or mathematical pattern study

---

## Summary of Skills Learned

### Core Python Concepts:
1. ✅ Variables and Data Types
2. ✅ Input/Output Operations
3. ✅ Arithmetic and Logical Operators
4. ✅ String Manipulation and Formatting
5. ✅ Lists, Tuples, and Dictionaries
6. ✅ Functions and Return Values
7. ✅ Conditional Statements (if/elif/else)
8. ✅ While Loops
9. ✅ For Loops and Range
10. ✅ Nested Loops
11. ✅ List Comprehensions
12. ✅ Built-in Functions (len, sum, min, max, sorted, enumerate, map, zip)
13. ✅ String Methods (upper, lower, strip, split, join, replace, format, etc.)
14. ✅ List Methods (append, insert, remove, pop, etc.)
15. ✅ Dictionary Operations
16. ✅ External Libraries (gTTS, os)
17. ✅ File Operations
18. ✅ Type Conversion

### Programming Patterns:
- Counter patterns
- Accumulator patterns
- String building
- Palindrome checking
- Unit conversions
- Data formatting
- Functional programming basics

---

## Next Steps for Learning

1. **File I/O**: Reading and writing files (CSV, JSON, text)
2. **Exception Handling**: Try-except blocks
3. **Object-Oriented Programming**: Classes and objects
4. **Advanced Data Structures**: Sets, deque, defaultdict
5. **Regular Expressions**: Pattern matching
6. **Database Operations**: SQLite, PostgreSQL
7. **Web Development**: Flask/Django
8. **Data Analysis**: Pandas, NumPy
9. **Visualization**: Matplotlib, Seaborn

---

*Documentation generated on: January 28, 2026*
*Workspace: c:\python*