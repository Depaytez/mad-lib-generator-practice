fruits = ["apple", "banana", "cherry", "date", "elderberry", "orange", "lemon", "mango", "nectarine", "papaya"]
for fruit in fruits[::-1]:  # Iterate through the list in reverse order
 print(f"I can eat:{fruit}")
for fruit in fruits[2::]:  # Skip the first two fruits and iterate through the rest
 print(f"I hate:{fruit}")
for fruit in fruits[::2]:  # Iterate through every second fruit
 print(f"I like:{fruit}")
for fruit in fruits[0::3]:  # Iterate through every third fruit starting from the first
 print(f"I love:{fruit}")
for fruit in fruits[1:6]:  # Iterate through the second and sixth fruits
 print(f"I enjoy:{fruit}")