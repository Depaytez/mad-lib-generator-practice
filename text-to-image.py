# create text-based arts by manipulating texts
rows = 5

for i in range(1, rows + 1):
  for j in range(1, i + 1):
    print(" * ", end="")
  print()  # Move to a new line after each row of asterisks