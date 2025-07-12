#iterating over lists
fruits = ["apple", "banana", "cherry", "date", "elderberry", "orange", "lemon", "mango", "nectarine", "papaya"]
for fruit in fruits:
 print(f"I like:{fruit}")
# for fruit in fruits[::-1]:  # Iterate through the list in reverse order
#  print(f"I can eat:{fruit}")
# for fruit in fruits[2::]:  # Skip the first two fruits and iterate through the rest
#  print(f"I hate:{fruit}")
# for fruit in fruits[::2]:  # Iterate through every second fruit
#  print(f"I like:{fruit}")
# for fruit in fruits[0::3]:  # Iterate through every third fruit starting from the first
#  print(f"I love:{fruit}")
# for fruit in fruits[1:6]:  # Iterate through the second and sixth fruits
#  print(f"I enjoy:{fruit}")

#iterating over turples in python
colors = ("red", "green", "blue", "yellow", "purple")
for color in colors:
 print(f"The color is: {color}")

#looping through characters in a string
message = "I love python"
for char_in_string in message:
 print(f"{char_in_string} is a character in the string '{message}'")

#iterating over ranges
for numbers in range(1, 20, 4): # Iterate from 1 to 20, stepping by 4
 print(f"Number: {numbers}")