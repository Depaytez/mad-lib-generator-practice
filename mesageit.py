successful = False
for send in range(3):
 print(f"Attempt {send + 1}: sending message...")
 if successful:
  print("Message sucessfully sent!")
  break
else:
 print("failed to send message, retrying...")
 if send == 2:
  print("Message failed to send after 3 attempts.")
