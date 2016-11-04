import os
import random
import sys

#Checks is there any todo data file, if not it create a new one.
if(os.path.exists("highscore.txt")):
    print("",end="")
else:
    my_file = (open("highscore.txt", mode='w'))
    my_file.close()

def showHighscore():
    cache = list()
    my_file = (open("highscore.txt", mode='r'))
    for line in my_file:
        cache.append(line.strip())
    my_file.close()

    print("Highscores: ")
    for i in range(0, len(cache)):
        print(cache[i])

def saveHighscore(highscoreList, name, score):
    my_file = (open("highscore.txt", mode='r'))
   
    for line in my_file:
        highscoreList.append(line.strip().split(': '))
    my_file.close()

    highscoreList.append([name,str(score)])

    highscoreList.sort(key=lambda x: int(x[1]))

    my_file = (open("highscore.txt", mode='w'))
    for j in range(0, int(len(highscoreList))):
        my_file.write(": ".join(highscoreList[j]) + "\n")
    my_file.close()

def generateNewNumber():
    randnumber = random.randint(0,100)
    return randnumber

def checkGuess(random_num, input_num, numTries):
    if(int(random_num) == int(input_num)):
        print("You won!")
        print("Number of tries: " + str(numTries))
        print("""
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        ░░░░░░░▄▄▀▀▀▀▀▀▀▀▀▀▄▄█▄░░░░▄░░░░█░░░░░░░
        ░░░░░░█▀░░░░░░░░░░░░░▀▀█▄░░░▀░░░░░░░░░▄░
        ░░░░▄▀░░░░░░░░░░░░░░░░░▀██░░░▄▀▀▀▄▄░░▀░░
        ░░▄█▀▄█▀▀▀▀▄░░░░░░▄▀▀█▄░▀█▄░░█▄░░░▀█░░░░
        ░▄█░▄▀░░▄▄▄░█░░░▄▀▄█▄░▀█░░█▄░░▀█░░░░█░░░
        ▄█░░█░░░▀▀▀░█░░▄█░▀▀▀░░█░░░█▄░░█░░░░█░░░
        ██░░░▀▄░░░▄█▀░░░▀▄▄▄▄▄█▀░░░▀█░░█▄░░░█░░░
        ██░░░░░▀▀▀░░░░░░░░░░░░░░░░░░█░▄█░░░░█░░░
        ██░░░░░░░░░░░░░░░░░░░░░█░░░░██▀░░░░█▄░░░
        ██░░░░░░░░░░░░░░░░░░░░░█░░░░█░░░░░░░▀▀█▄
        ██░░░░░░░░░░░░░░░░░░░░█░░░░░█░░░░░░░▄▄██
        ░██░░░░░░░░░░░░░░░░░░▄▀░░░░░█░░░░░░░▀▀█▄
        ░▀█░░░░░░█░░░░░░░░░▄█▀░░░░░░█░░░░░░░▄▄██
        ░▄██▄░░░░░▀▀▀▄▄▄▄▀▀░░░░░░░░░█░░░░░░░▀▀█▄
        ░░▀▀▀▀░░░░░░░░░░░░░░░░░░░░░░█▄▄▄▄▄▄▄▄▄██
        ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
        """)
        return True     
    else:
        print("Sorry, this is not the number You are looking for.")
        print("┛◉Д◉)┛彡┻━┻")
        return False

def ask(question):
    #This is where the ask options are handled
    os.system('clear')
    if question ==  'bigger':
        while True:
            try:
                usrBigger = int(input("Is X bigger than?: "))
                if(checkBigger(usrBigger,randomNumber) == 1):
                    print("Yes, the number is bigger than this.")
                elif (checkBigger(usrBigger,randomNumber)) == 2:
                    print("\n¯\_(°‿°)_/¯")
                else:
                    print("No, the number is smaller than this.")
                break
            except ValueError:
                print("Please enter a number!")
        
        
    
    if question ==  'smaller':
        while True:
            try:
                usrSmaller = int(input("Is X smaller than?: "))
                if(checkSmaller(usrSmaller,randomNumber) == 1):
                    print("Yes, the number is smaller than this.")
                elif (checkSmaller(usrSmaller,randomNumber)) == 2:
                    print("\n¯\_(°‿°)_/¯")
                else:
                    print("No, the number is bigger than this.")
                break
            except ValueError:
                print("Please enter a number!")

    if question ==  'prime':
        if(checkPrime(randomNumber)):
            print("Yes, it is a prime.")
        else:
            print("No, it isn't a prime.")
    
    if question ==  'even':
        if(checkEven(randomNumber)):
            print("Yes, it is even.")
        else:
            print("No, it is odd")

    if question ==  'odd':
        if(checkOdd(randomNumber)):
            print("Yes, it is odd.")
        else:
            print("No, it is even.")

    if question ==  'divisible':
        while True:
            try:
                if(checkDivisible(int(input("Enter your number: ")),randomNumber)):
                    print("Yes, it is divisible, with your number")
                else:
                    print("No, it isn't divisible with your number")
                    break
            except ValueError:
                print("Please enter a number!")

def surrender(random_num, numTries):
    os.system('clear')
    print("The number was: " + str(random_num))
    print("The number of your tries: " + str(numTries))

    print("""
    ─▄▀▀▀▀▄─█──█────▄▀▀█─▄▀▀▀▀▄─█▀▀▄ 
    ─█────█─█──█────█────█────█─█──█ 
    ─█────█─█▀▀█────█─▄▄─█────█─█──█ 
    ─▀▄▄▄▄▀─█──█────▀▄▄█─▀▄▄▄▄▀─█▄▄▀ 

    ─────────▄██████▀▀▀▀▀▀▄
    ─────▄█████████▄───────▀▀▄▄
    ──▄█████████████───────────▀▀▄
    ▄██████████████─▄▀───▀▄─▀▄▄▄──▀▄
    ███████████████──▄▀─▀▄▄▄▄▄▄────█
    █████████████████▀█──▄█▄▄▄──────█
    ███████████──█▀█──▀▄─█─█─█───────█
    ████████████████───▀█─▀██▄▄──────█
    █████████████████──▄─▀█▄─────▄───█
    █████████████████▀███▀▀─▀▄────█──█
    ████████████████──────────█──▄▀──█
    ████████████████▄▀▀▀▀▀▀▄──█──────█
    ████████████████▀▀▀▀▀▀▀▄──█──────█
    ▀████████████████▀▀▀▀▀▀──────────█
    ──███████████████▀▀─────█──────▄▀
    ──▀█████████████────────█────▄▀
    ────▀████████████▄───▄▄█▀─▄█▀
    ──────▀████████████▀▀▀──▄███
    ──────████████████████████─█
    ─────████████████████████──█
    ────████████████████████───█
    ────██████████████████─────█
    ────██████████████████▄▄▄▄▄█

    ─────────────█─────█─█──█─█───█
    ─────────────█─────█─█──█─▀█─█▀
    ─────────────█─▄█▄─█─█▀▀█──▀█▀
    ─────────────██▀─▀██─█──█───█
    """)

    print('\nGenerating new number')
    os.system("eject cdrom") #easteregg

def checkEven(randomNumber):
    if((randomNumber % 2) == 0):
        return True
    else:
        return False

def checkOdd(randomNumber):
    if((randomNumber % 2) == 1):
        return True
    else:
        return False

def checkDivisible(input, randomNumber):
    if((randomNumber) % input == 0):
        return True
    else:
        return False

def checkBigger(usrInput, randomNumber):
    if usrInput < randomNumber:
        return 1
    elif usrInput == randomNumber:
        return 2
    else:
        return False        

def checkSmaller(usrInput, randomNumber):
    if usrInput > randomNumber:
        return 1
    elif usrInput == randomNumber:
        return 2
    else:
        return False

def checkPrime(randomNumber):
    primeList = [2,3,5,7,11,13,17,19,23,29 ,31,37,41,43,47,53,59,61,67,71 ,73,79,83,89,97,101]
    if randomNumber in primeList:
        return True
    else:
        return False

#Declaring variables
commandList = ["guess", "ask", "surrender", "highscore", "exit"]
questionList = ["bigger", "smaller", "prime", "even", "odd", "divisible"]
highscoreList = list()
randomNumber = generateNewNumber()
numTries = 0

#Initialising starting screen
os.system('clear')
print("Welcome in the GuessTheNumber game, where You have to guess the generated number (0 <= X < 100) to WIN")
print("\n      ¯\(°_o)/¯\n")
userName = input("Please enter your name: ") or "Unkown soldier"

#Main loop
while True:    
    print("\nAvailable commands: ", end=" ")
    for i in commandList:
        print(i,end=" ")
    print()

    userInput = (input("\nEnter a command: ")).lower()
    os.system('clear')
    
    #Guess
    if (userInput == commandList[0]):
        numTries += 1
        userGuess = input("Give your guessed number: ")
        if(checkGuess(randomNumber, userGuess, numTries)):
            print("New number (X) generated!")
            saveHighscore(highscoreList,userName,numTries)
            numTries = 0
            randomNumber = generateNewNumber()

    #Ask
    if (userInput == commandList[1]):
        numTries += 1
        print("Available questions: ")
        for i in questionList:
            print(i,end=" ")
        print()

        userQuestion = input("\nEnter a question: ").lower()
        ask(userQuestion) 

    #Surrender
    if (userInput == commandList[2]):
        surrender(randomNumber,numTries)
        randomNumber = generateNewNumber()

    #ShowHighscore
    if (userInput == commandList[3]):
        showHighscore()

    #Exit
    if (userInput == commandList[4]):
        print("Goodbye!")
        quit()