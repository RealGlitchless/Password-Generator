import random
import pyperclip

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
  symList = ["!", "?", "@", "¤", "$", "€", "+", ".", "/", "*", "~", "½", "§", ",", "#", "£", "<", ">", "|", "=", "-", ";", ":", "[", "]", "{", "}", "_", "*"]
  randSymbol = symList[random.randint(0, 12)]
  return randSymbol

def randomizer():
  password = []
  for num in range(lenght):
    if choices == 1:
      password.append(letters())

    elif choices == 2:
      randInt = random.randint(1, 2)
      if randInt == 1:
        password.append(letters())
      elif randInt == 2:
        password.append(str(numbers()))

    elif choices == 3:
      randInt = random.randint(1, 2)
      if randInt == 1:
        password.append(letters())
      elif randInt == 2:
        password.append(symbols())
      
    elif choices == 4:
      randInt = random.randint(1, 3)
      if randInt == 1:
        password.append(letters())
      elif randInt == 2:
        password.append(symbols())
      elif randInt == 3:
        password.append(str(numbers()))
        
  return password

if __name__ == "__main__":
  choices = 1
  while True:
      
    lenght = input("How many characters shall the password have?\n")
    try:
      lenght = int (lenght)
      toggle = False
    
    except:
      print("Please enter a valid input")

  while True:
    numChoice = input("Shall the password contain numbers? y/n\n")

    if numChoice == 'y':
      choices += 1
      break
    
    elif numChoice == 'n':
      break

    else:
      print("Please press a valid key")

  while True:
    symChoice = input("Shall the password contain symbols? y/n\n")
    if symChoice == 'y':
      choices += 2
      break

    elif symChoice == 'n':
      break

  finalPassword = ""
  for character in randomizer():
    finalPassword += character

  pyperclip.copy(finalPassword)
  print(f"Your password is: {finalPassword}\nPassword has been copied to your clipboard!")
