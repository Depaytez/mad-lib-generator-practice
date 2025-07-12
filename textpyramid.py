rows = 5
row = 0

while row < rows:
 # Print leading spaces to center the pyramid
 space = 0
 while space < rows - row - 1:
  print("  ", end="  ")
  space += 1
 
 star = 0
 while star < 2 * row + 1:
  print(" * ", end=" ")
  star += 1
 print()
 row += 1

 