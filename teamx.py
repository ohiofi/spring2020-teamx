#By: Sanjeev, Caleb, Jon, Isaac
from time import *
from random import *
from map import *

roomArray = []
itemArray = []
inventoryArray = []
correctAnswers = []
wrongAnswers = []
score = 0

for i in range(999):
  roomArray.append(False)
  itemArray.append(False)

roomArray[300] = "You are at the front entrance of the mental facility. The front door is locked, so the only way to move is South."
roomArray[201] = "You stand in the top left corner of the main lobby. It is very chilly in this corner."
roomArray[301] = "You look all around you. It is a cramped lobby: to the East and West is nothing special, but to the South you can see a hallway."
roomArray[401] = "You decide to sit in a chair for no good reason. There is a desk to the South."
roomArray[202] = "You walk into the lower left corner of the lobby. To the East, there is a hallway entrance."
roomArray[302] = "You stand right in the middle of the main lobby. To the South, there is a hallway. To the East, there is a desk."
roomArray[402] = "You stand in front of a desk. To the East, there is a short hallway. To the West, there is a longer one."
roomArray[502] = "You stand in the middle of the short hallway. To the West is a desk. To the East is a door."
roomArray[602] = "A huge iron door is directly to the West of you. Kinda eerie."
roomArray[303] = "You are at the beginning of the hallway. You look out of a window and see that it's probably after midnight."
roomArray[304] = "A door that leads to the janitor's closet is South of you."
roomArray[205] = "You are standing in a dark, smaller section of the closet.  You're surrounded by walls to the North, West, and South.  The closet opens back up to the East."
roomArray[305] = "Inside the janitor's closet, you see nothing really. It's pretty dark."
roomArray[405] ="You're now in the Northeast corner of the closet.  It smells strong of bleach.  There's a dark room to the West but you can't see that far."
roomArray[306] = "You've reached a wall to the South and West.  There's spilled cleaner on the floor."
roomArray[406] = "You are standing in the Southeast corner of the closet.  Theres a small single light bulb above your head and theres a cool breeze flowing from a vent near the floor on the wall."
itemArray[201] = "health pack"
itemArray[301] = "money"
itemArray[202] = "knife"
itemArray[402] = "clipboard"
itemArray[205] = "key"
itemArray[305] = "fire axe"
itemArray[306] = "broom"
itemArray[406] = "wrench"
 
def doesRoomExist(location):
  try:
    if roomArray[location] == False:
      print("You can’t go there.") 
      return False
    else:
      return True 
  except:
    print("You can't go there.")
    return False

def doesItemExist(location):
  try:
    if not itemArray[location] == False:
      print("Item: " + itemArray[location])  
  except:
    return

def pickUpItem(itemArray, location):
  inventoryArray.append(itemArray[location])
  print("You have picked up '" + itemArray[location] + "'")
  itemArray[location] = False

def move(userInput, location):
  if userInput == "n" and doesRoomExist(location - 1) == True:
    location -= 1
  else:
    if userInput == "s" and doesRoomExist(location + 1) == True:
      location += 1
    else:
      if userInput == "e" and doesRoomExist(location + 100) == True:
        location += 100
      else:
        if userInput == "w" and doesRoomExist(location - 100) == True:
          location -= 100
  return location

def main():
  boss = 0
  quiz = 0
  word = 0
  cipher = 0
  location = 300
  map = Map()
  printName()
  print("by: Isaac, Caleb, Sanjeev, and Jon")
  sleep(1)
  print("While out on a midnight stroll, you see a mental hospital. As if possessed by a ghost, you walk into the facility. The door locks behind you.")
  while True:
    map.draw(roomArray, itemArray, location)
    end = boss + quiz + word + cipher
    if location == 805 and word == 0:
       print("Guess the word game.")
       game = mainJon()
       word += 1
       roomArray[805] = "You have already beat this game."
    if location == 607 and boss == 0:
      print("BOSS BATTLE!!!!!")
      lose = mainIsaac()
      boss += 1
      roomArray[607] = "You already defeated the boss."
      if lose <= 0:
        break
    if location == 605 and quiz == 0:
      print("QUIZ!!!")
      mainSanjeev()
      quiz += 1
      roomArray[605] = "You already completed the quiz."
    if location == 807 and cipher == 0:
      mainCaleb()
      print("You decrypted the cipher.")
      cipher += 1
      roomArray[807] = "You've already decrypted the cipher."
    print("~ ~ ~")
    print(roomArray[location])
    if location == 708:
      break
    print("Inventory: " + str(inventoryArray))
    doesItemExist(location)
    print("Please type: n, s, e, w, pick up, or quit. Use an item by typing 'use' + name of item")
    userInput = input()
    if (location == 707 and "use key" in userInput) and end == 4:
      print("You unlocked the door.")
      roomArray[708] = "Congratulations! You escaped the mental facility."
    if ("use" in userInput and location == 602):
      if ("key" in inventoryArray and "key" in userInput):
        print("you unlocked the huge iron door.")
        roomArray[702] = "You've entered a hallway that leads South."
        roomArray[703] = "You are in the middle of the hallway and hear rumbling coming from the South end."
        roomArray[704] = "You are standing at the south end of the hallway and the rumbling has settled."
        roomArray[705] = "You've entered a new room and can move in any direction."
        roomArray[805] = "You are at the Northeast corner of the room and have stepped on a boss tile!"
        roomArray[605] = "You are at the Northwest corner of the room, and have to complete a quiz."
        roomArray[606] = "You are at the wall of the east side. You can only go north, south, or west."
        roomArray[607] = "You are at the southwest corner"
        roomArray[706] = "You are in the middle, you can go anywhere you want"
        roomArray[707] = "Ther is a door to the South with a sign that says, 'complete all 4 trials to leave.'"
        roomArray[806] = "You continue walking and suddenly hear noise to the west"
        roomArray[807] = "You are at the southeast corner."
      else:
        print("Can't do that right now.")
    if userInput == "quit":
      print("you trip, fall, and die immediately as your face hits the floor. unlucky")
      break
    if userInput == "pick up" and itemArray[location] == False:
      print("There are no items to pick up.")
    if userInput == "pick up" and not itemArray[location] == False:
      pickUpItem(itemArray, location)
    location = move(userInput, location)

def printName():
  print(" ███▄ ▄███▓▓█████  ███▄    █ ▄▄▄█████▓ ▄▄▄       ██▓    ")
  print("▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █ ▓  ██▒ ▓▒▒████▄    ▓██▒    ")
  print("▓██    ▓██░▒███   ▓██  ▀█ ██▒▒ ▓██░ ▒░▒██  ▀█▄  ▒██░    ")
  print("▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒░ ▓██▓ ░ ░██▄▄▄▄██ ▒██░    ")
  print("▒██▒   ░██▒░▒████▒▒██░   ▓██░  ▒██▒ ░  ▓█   ▓██▒░██████▒")
  sleep(.7)
  print("░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒   ▒ ░░    ▒▒   ▓▒█░░ ▒░▓  ░")
  sleep(.7)
  print("░  ░      ░ ░ ░  ░░ ░░   ░ ▒░    ░      ▒   ▒▒ ░░ ░ ▒  ░")
  print("░      ░      ░      ░   ░ ░   ░        ░   ▒     ░ ░   ")
  sleep(.7)
  print("       ░      ░  ░         ░                ░  ░    ░  ░")

#SECRET WORD START-------------------------------------------------------------------
def randomSecretWordJon():
    list1 = ["apple", "banana", "orange", "grape fruit", "cucumber", "carrot", "lettuce", "tomatoe", "onion", "kiwi"]
    list2 = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]
    list3 = ["wii", "ds", "xbox 360", "playstation 3", "switch", "xbox 1", "playstation 4", "wii u", "psp", "gamecube"]
    combinedList = list1 + list2 + list3
    rand = choice(combinedList)
    return rand

def mainJon():
    word = randomSecretWordJon()
    word = word.lower()
    print("I'm thinking of a secret word. Take a guess and I'll tell you if the secret word is before your word or after your word.")
    print("Guess a word.")
    while True:
        user = input()
        user = user.lower()
        if user < word:
            print("The secret word is after " + user + ".")
        if user > word:
            print("The secret word is before " + user + ".")
        if user == word:
            print("You got it!")
            break
    return 1
#SECRET WORD END-----------------------------------------------------------------------
#BOSS BATTLE START --------------------------------------------------------------------
def askPlayer():
  global x
  while True:
    sleep(.5)
    print("Type which weapon to use.")
    print("1. PUNCH")
    if "broom" in inventoryArray:
      print("2. Broom")
    else:
      print("2. ???")
    if "clipboard" in inventoryArray:
      print("3. Clipboard")
    else:
      print("3. ???")
    if "fire axe" in inventoryArray:
      print("4. Fire Axe")
    else:
      print("4. ???")
    if "wrench" in inventoryArray:
      print("5. Wrench")
    else:
      print("5. ???")
    if "knife" in inventoryArray:
      print("6. Knife")
    else:
      print("6. ???")
    if "health pack" in inventoryArray:
      print("7. Health Pack")
    else:
      print("7. ???")
    try:
      number = input()
      number = number.lower()
      if number in inventoryArray or number == "punch":
        break
      else:
        print("Not a valid weapon.")
    except:
      print("Not a valid weapon.")
  return number

def enemyLoseHealth(playerChoice, enemy):
  if playerChoice == "punch":
    damage = randint(5, 10)
  if playerChoice in inventoryArray:
    damage = randint(10, 15)
  if playerChoice == enemy["weakness"]:
    damage = randint(15, 30)
  if damage > 20:
    print("IT'S SUPER EFFECTIVE!!!!")
  sleep(.5)
  print("damage to " + enemy["name"] + ": " + str(damage))
  newEnemyHealth = enemy["health"] - damage
  print(enemy["name"] + " has " + str(newEnemyHealth) + " health remaining.")
  return newEnemyHealth

def playerLoseHealth(playerHealth, enemy):
  damage = randint(0, enemy["level"])
  randomAttack = choice(enemy["attacks"])
  sleep(.5)
  print(enemy["name"] + " used " + randomAttack + " and did " + str(damage) + " damage to you." )
  newPlayerHealth = playerHealth - damage
  sleep(.5)
  print("You have " + str(newPlayerHealth) + "HP.")
  return newPlayerHealth

def gameLevel(castleDescription, enemy, playerHealth):
  print("==========================================")
  sleep(.5)
  print(castleDescription)
  while playerHealth > 0:
    sleep(.5)
    print("~ ~ ~")
    playerChoice = askPlayer()
    if playerChoice == "punch":
      enemy["health"] = enemyLoseHealth(playerChoice, enemy)
    if playerChoice == "health pack" and "health pack" in inventoryArray:
      playerHealth = 100
      print("You use the health pack and heal back to 100 HP.")
      inventoryArray.remove("health pack")
    if playerChoice in inventoryArray:
      enemy["health"] = enemyLoseHealth(playerChoice, enemy)
    if enemy["health"] > 0:
      playerHealth = playerLoseHealth(playerHealth, enemy)
    if enemy["health"] <= 0:
      sleep(.5)
      print("You have defeated " + enemy["name"] + "!")
      break
    if playerHealth <= 0:
      sleep(.5)
      print("Oof.  You have DIED!  R.I.P.  Game Over.")
  return playerHealth

def mainIsaac():
  playerHealth = 100
  enemy = {}
  enemy["name"] = "Dhruvkrishna"
  enemy["level"] = 35
  enemy["health"] = 70
  enemy["attacks"] = ["Hemorrhage", "Decimate", "Crippling Strike", "Apprehend", 
  "Noxian Guillotine", "Noxian Diplomacy", "Shadow Assault"]
  if len(inventoryArray) == 0:
    if randint(1,6) == 1:
      enemy["weakness"] = "punch"
    else:
      enemy["weakness"] = "NONE"
  else:
    if len(inventoryArray) > 3:
      enemy["weakness"] = choice(inventoryArray)
    else:
      if randint(1,3) == 1:
        enemy["weakness"] = "punch"
      else:
        enemy["weakness"] = choice(inventoryArray)
  castleDescription = "defeat the boss."
  if playerHealth > 0:
    playerHealth = gameLevel(castleDescription,enemy,playerHealth)
  if playerHealth > 0:
    print("~ ~ ~")
    sleep(1)
    print("Good job taking care of Dhruvkrishna.")
  return playerHealth
#BOSS BATTLE END ---------------------------------------------------------
#FILL IN THE BLANK START---------------------------------------------------
def askQuestion(question, answer):
  while True:
    global score
    print(question)
    userInput = str(input())
    userInput = userInput.lower()
    if userInput == answer:
      score = score+5
      correctAnswers.append(userInput)
      print("correct, your score is " + str(score))
      break
    else:
      score = score-3
      wrongAnswers.append(userInput)
      print("incorrect, your score is " + str(score))

def mainSanjeev():
  askQuestion("9 * 15 = ?", "135")
  askQuestion("How many states are in the United States?", "50")
  askQuestion("3 x 4", "12")
  askQuestion("How many tires are in a car?", "4")
  print("Your wrong answers were: " + str(wrongAnswers))
  print("Your correct answers were: " + str(correctAnswers))
#FILL IN THE BLANK END-------------------------------------------------------------
#CIPHER START-------------------------------------------------------
def mainCaleb():
  print("You've stepped on a pressure plate and triggered a spike trap that surrounds you.  in the middle of the trap is a Caesar Cipher code.  You must decrypt the code to escape the trap.")
  mainCipher()
  
def caesarEncrypt(myString,myNumber):
  result = ""
  # loop thru the string saving each letter in the varable each
  for each in myString:
    # convert each letter to a number
    letterNumber = ord(each)
    # shift the letter number by adding mynumber
    shiftedNumber = letterNumber + myNumber
    # convert the number back to character and string
    result += str(chr(shiftedNumber))
  return result
  
def caesarDecrypt(myString,myNumber):
  result = ""
  # loop thru the string saving each letter in the varable each
  for each in myString:
    # convert each letter to a number
    letterNumber = ord(each)
    # shift the letter number by adding mynumber
    shiftedNumber = letterNumber - myNumber
    # convert the number back to character and string
    result += str(chr(shiftedNumber))
  return result

def randomSecretCodeWord():
    food = ["pizza", "beans", "cheese", "wings", "nachos", "lettuce", "beets", "strawberries", "burgers", "croutons"]
    sports = ["soccer", "football", "basketball", "tennis", "volleyball", "bowling", "badminton", "diving", "track", "lacrosse"]
    cities = ["Marion", "Cleveland", "Orlando", "Houston", "Huntsville", "Hilliard", "Selma", "Tuskegee", "Dallas", "London"]
    combinedList = food+sports+cities
    word1 = choice(combinedList)
    word2 = choice(combinedList)
    word3 = choice(combinedList)
    bigWord = word1 + word2 + word3
    return bigWord

def validInt(userInput):
    try:
        
        userInput = int(userInput)
        return True
    except:
        
        return False
def mainCipher():
    secretString = randomSecretCodeWord()
    secretNumber = randint(1,20)
    gibberish = caesarEncrypt(secretString, secretNumber)
    print("Gibberish message is "+gibberish)
    while True:
        print("Output shift by how much? Type 1-20")
        userInput = input()
        validity = validInt(userInput)
        if validity == True:
            userInput = int(userInput)
            newText  = caesarDecrypt(gibberish, userInput)
            print(newText)
            if userInput == secretNumber:
                break
        if validity == False:
            print("Not a number")
            
            validity = validInt(userInput)
#CIPHER END----------------------------------------------------------------------

main()
