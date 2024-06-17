import random

def guess_the_number():
  """Plays a number guessing game with the user."""

  number = random.randint(1, 100)
  guesses_left = 7
  print("I'm thinking of a number between 1 and 100.")

  while guesses_left > 0:
    try:
      guess = int(input("Take a guess: "))
    except ValueError:
      print("Invalid input. Please enter a number.")
      continue

    if guess < number:
      print("Too low!")
    elif guess > number:
      print("Too high!")
    else:
      print(f"Congratulations! You guessed the number in {7 - guesses_left} tries.")
      return

    guesses_left -= 1
    print(f"You have {guesses_left} guesses left.")

  print(f"You ran out of guesses! The number was {number}.")

guess_the_number()