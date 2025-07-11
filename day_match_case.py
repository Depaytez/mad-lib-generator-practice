# Get an interesting word for the day
print("Today is what: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', or 'Sunday'?")
day = input("Enter the day of the week: ").lower()

match day:
 case "monday":
  message = "Beautiful monday! start the week with energy"
 case "tuesday":
  message = "Bright tuesday! You've got this, keep going"
 case "wednesday":
  message = "Oh, lovely! You cant stop now. Let's make wednesday great"
 case "thursday":
  message = "You are almost there! It's thursday, keep pushing"
 case "friday":
  message = "It's friday! The weekend is almost here, make sure to accomplish all goals for the week"
 case "saturday":
  message = "Happy saturday! Enjoy your weekend and relax"
 case "sunday":
  message = "It's sunday! A day to fellowship with the brethren and prepare for the week ahead"
 case _:
  message = "Invalid day. Please enter a valid day of the week."
print(message)

data_type = input("Type something to know it data type: ")
match data_type:
 case int():
  message = "You entered an integer."
 case float():
  message = "You entered a float."
 case str():
  message = "You entered a string."
 case bool():
  message = "You entered a boolean."
 case _:
  message = "Unknown data type."
print(message)