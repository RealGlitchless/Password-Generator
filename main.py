from random import randint, choice
from string import ascii_letters
import pyperclip

def rnd_letters():
  # Generate a random letter
  randLetter = choice(ascii_letters)
  return randLetter

def rnd_numbers():
  randNumber = randint(0, 9)
  return randNumber

def rnd_symbols():
  # Generate a random symbol
  symbols = "!@#$%^&*()_+{|}[]<>?/.,;:~`"
  randSymbol = choice(symbols)
  return randSymbol

def randomizer(lenght, numbers, symbols):
  password = ""
  for _ in range(lenght):
    if numbers and symbols:
      randInt = randint(0, 2)
      if randInt == 0: password += rnd_letters()
      elif randInt == 1: password += str(rnd_numbers())
      else: password += rnd_symbols()

    elif numbers:
      randInt = randint(0, 1)
      if randInt == 0: password += rnd_letters()
      else: password += str(rnd_numbers())

    elif symbols:
      randInt = randint(0, 1)
      if randInt == 0: password += rnd_letters()
      else: password += rnd_symbols()
      
    else: password += rnd_letters()
        
  return password

if __name__ == "__main__":
  choices = 1
  toggle = True
  while toggle:
    lenght = input("How many characters shall the password have?\n")
    try:
      lenght = int(lenght)
      toggle = False
    
    except ValueError: print("Please enter a valid input")

  while True:
    numChoice = input("Shall the password contain numbers? y/n\n")
    if numChoice == 'y':
      numChoice = True
      break
    
    elif numChoice == 'n':
      numChoice = False
      break

    else: print("Please press a valid key")

  while True:
    symChoice = input("Shall the password contain symbols? y/n\n")
    if symChoice == 'y':
      symChoice = True
      break

    elif symChoice == 'n':
      symChoice = False
      break

    else: print("Please press a valid key")

  finalPassword = ""
  for character in randomizer(lenght, numChoice, symChoice):
    finalPassword += character

  pyperclip.copy(finalPassword)
  print(f"Your password is: {finalPassword}\nPassword has been copied to your clipboard!")
