def count_10(number):
    if (number >= 10):
        coin_10 = number // 10
    if ((number % 10) >=5):
        remained = number % 10
        count_5(remained)
    else:
        remained = number % 10
        count_2(remained)
    print("Coin 10: " + str(coin_10))
    

def count_5(number):
    if (number >= 5):
        coin_5 = number // 5
    if ((number % 5) >=2):
        remained = number % 5
        count_2(remained)
    else:
        remained = number % 5
        count_1(remained)
    print("Coin 5: " + str(coin_5))

def count_2(number):
    if (number >= 2):
        coin_2 = number // 2
    if ((number % 2) >=1):
        remained = number % 2
        count_1(remained)
    print("Coin 2: " + str(coin_2))

def count_1(number):
    if (number >= 1):
        coin_1 = number // 1
    print("Coin 1: " + str(coin_1))

userInput = int(input("Please enter a number: "))
count_10(userInput)