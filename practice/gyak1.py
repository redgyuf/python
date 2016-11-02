number = int(input("Please enter a number: "))
fb = 0

if ((number % 3) == 0):
    print("Fizz", end="")
    fb = 1
if ((number % 5) == 0):
    print("Buzz")
    fb = 1

if (fb == 0):
    print(number)