"""
bulls_and_cows.py: druhý projekt do Engeto Online Python Akademie
author: Tereza Trojanová
email: trojanovate@gmail.com
discord: tereza4859
"""

import random
import time

print("Hi there!")
print("-"*50)
print("I've generated a random 4 digit number for you.\nLet's play a bulls and cows game.")

#generate secret number
def generate_secret():
    digits = random.sample(range(0, 10), 4)
    print(digits)

    #if the first digit == 0, shuffle the list, else return the list as a number
    while digits[0] == 0:
        random.shuffle(digits)
        continue
    else:
        number = int(''.join(map(str, digits)))
        return number

#define bulls and cows game
def count_bulls_and_cows(secret, guess):
    secret = str(secret)
    bulls = 0
    cows = 0
    for i in range(len(secret)):
        if secret[i] == guess[i]:
            bulls += 1
        elif guess[i] in secret:
            cows += 1
    return {"bulls":bulls,"cows":cows}

#generate the random number
random_number = generate_secret()

#user attempts/time counter
attempts = 0
start_time = time.time()

#ask the user for input and check its formal structure
while True:
  print("-"*50)
  user_input = input("Enter a number:")
  #prepare duplicates check
  duplicates = [x for n, x in enumerate(str(user_input)) if x in str(user_input)[:n]]
  duplicates_check = len(duplicates)
  #check if the user's input if valid, if not, ask the user to try again
  if user_input.isdigit() == False:
      print("Your guess contains non numeric symbols, please try again.")
      continue
  elif len(user_input) != 4:
      print("This is not a 4 digit number, please try again.")
      continue
  elif int(user_input[0]) == 0:
      print("The first character should not be null.")
      continue
  elif duplicates_check != 0:
      print("Your input contains duplicates, please try again.")
      continue
  #in case the input is valid, call the bulls and cows function
  else:
      result = count_bulls_and_cows(random_number,user_input)
      #if the user's guess is correct, stop the timer and print the result report
      if result["bulls"] == 4:
          attempts += 1
          end_time = time.time()
          duration = int(end_time - start_time)
          print("-"*50)
          print("Correct, you've guessed the right number\nin " + str(duration) + " seconds and " + str(attempts) + " attempts!")
          break
      #if the user's guess does not match the generated number, add the number of the attempt and continue the game
      else:
          attempts += 1
          print("Bulls: " + str(result["bulls"]) + "\nCows: " + str(result["cows"]))
          continue
