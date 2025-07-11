# mad lib story generator
print("Choose any of the following to create a story: noun, verb")
user_input = input("Enter your choice here: ")

if user_input.lower() == "noun":
    noun = input("Enter a noun word:")
    story = f"Once upon a time, there was a {noun} that lived in a magical forest. Every day, {noun} would go on adventures and meet new friends. One day, {noun} discovered a life changing hidden treasure."
elif user_input.lower() == "verb":
    verb = input("Enter an action word:")
    story = f"Once upon a time, there was a creature that loved to {verb}. Every day, it would {verb} through the magical forest, making friends along the way."
else:
    story = "Invalid choice. Please choose either 'noun' or 'verb'."
print(story)
