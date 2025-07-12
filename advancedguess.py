#guess the secrete number i am ihinking
import random
print(f"Welcome to the secret number advanced guessing game by Philip Depaytez")

def play_game(): 
 secret_number = random.randint(1, 10)
 print(f"I am thinking of a number between 1 and 10, can you guess what it is?")
 user_guess = int(input("What's the number? "))
 guess_count = 1

 while user_guess != secret_number:
  guess_count += 1
  if user_guess < secret_number:
   print(f"your guess is too low, try again!")
  elif user_guess > secret_number:
   print(f"your guess is too high, try again!")
  user_guess = int(input("What's the number? "))
 else:
  print(f"Congratulations! You've tried {guess_count} times to guess the secret number {secret_number} correctly.")
  play_again = input("Do you want to play again? (yes/no): ").lower()
  if play_again != 'yes':
   print("Alright, thank you for playing! Come back anytime, my brother.")
   return  # Exit the function to stop the game
  else:
   print("Thank you for coming back, my friend.")
   print("Let's play again!")
   play_game()

play_game()