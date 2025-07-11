# guess a secret number chosen by the program.
import random
print("Welcome to the Secret Number Guessing Game by Philip Depaytez!")

while True: #main game loop starts
 secret_number = random.randint(1, 20)
 print(f"\nI am thinking of a number between 1 and 20, can you guess what it is?")

 attempts = 0
 while True:
  attempts += 1

  guess = int(input(f"Attempt {attempts}: What's the number? "))
 
  # Use match case to compare the guess with the secret number
  match guess:
   case _ if guess == secret_number:
    print(f"Congratulations! You guessed the secret number. The secret number was {secret_number}.")
    print(f"It took you {attempts} attempts to guess correctly, my brother!")
    break # Exit the 'attempts' loop (inner while True) because the guess is correct
   case _ if guess < secret_number:
    print("Your guess is too low. Try again!")
   case _ if guess > secret_number:
    print("Your guess is too high. Try again!")

  # Offer to play again after a round is completed
  play_again_input = input("\nDo you want to play again? (yes/no): ").lower()
  if play_again_input != 'yes':
   print("Alright, thank you for playing! Come back anytime, my brother.")
   break # Exit the main game loop
