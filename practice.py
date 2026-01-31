# DICTIONARY


file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for extension in file_counts:
    print(extension) 
  
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for ext, amount in file_counts.items():
  print("There are {} files with the .{} extension".format(amount, ext))

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
file_counts.keys()
file_counts.values()
print (file_counts.keys())
print (file_counts.values())

file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
for value in file_counts.values():
    print(value)

def count_letters(text):
  result = {}
  for letter in text:
    if letter not in result:
      result[letter] = 0
    result[letter] += 1
  return result
count_letters("aaaaa")
count_letters("tenant")
count_letters("a long string with a lot of letters")


























    















# UNIQUE SEQUENCES    

# MAX_END_VALUE = 100
# START_MIN = 1
# START_MAX = 9
# INCREMENT_MIN = 2
# INCREMENT_MAX = 15
# sequence_count = 0
# for start_num in range(START_MIN, START_MAX + 1):
#     for increment in range(INCREMENT_MIN, INCREMENT_MAX + 1):
#         sequence_count += 1
#         print("=" * 70)
#         sequence = [i for i in range(start_num, MAX_END_VALUE + 1, increment)]
#         print(", ".join(map(str, sequence)))
# print("\n" + "#" * 30)
# print(f"Successfully generated {sequence_count} unique sequences.")
# print("#" * 30)
