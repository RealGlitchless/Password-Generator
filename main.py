import random
import pyperclip

toggle = True
while toggle:
    
  lenght = input("How many characters shall the password have?\n")
  try:
    lenght = int (lenght)
    toggle = False
  
  except:
    print("Please enter a valid input")

password = []
def letters():
  letterList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z"]
  randLetter = letterList[random.randint(0, 24)]

  if random.randint(1, 2) == 1:
    randLetter = randLetter.upper()
    return randLetter
    
  else:
    return randLetter

def numbers():
  numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
  randNumber = numList[random.randint(0, 9)]
  return randNumber

def symbols():
  symList = ["!", "?", "@", "¤", "$", "€", "+", ".", "/", "*", "~", "½", "§"]
  randSymbol = symList[random.randint(0, 12)]
  return randSymbol

counter = 1
while counter <= lenght:
  randInt = random.randint(1, 3)
  if randInt == 1:
    password.append(letters())

  elif randInt == 2:
    password.append(str(numbers()))

  elif randInt == 3:
    password.append(symbols())
  
  counter += 1


finalPassword = ""
for character in password:
  finalPassword += character

pyperclip.copy(finalPassword)
print(f"Your password is: {finalPassword}\nPassword copied to your clipboard!")
