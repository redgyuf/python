def countCoins(number):
    coin_10 = int(number) // 10
    remain_10 = int(number) % 10
    coin_5 = remain_10 // 5
    remain_5 = remain_10 % 5
    coin_2 = remain_5 // 2
    coin_1 = remain_5 % 2

    print("Current number: " + str(number))
    print("Coin 10: " + str(coin_10) + " Coin 5: " + str(coin_5) + " Coin 2: " + str(coin_2) + " Coin 1: " + str(coin_1))

number_list = list()

file_list = (open("number_list.txt", mode='r'))
for number in file_list:
    number_list.append(number.strip())
file_list.close()

for j in range(0, len(number_list)):
    countCoins(number_list[j])