fib_numbers = [0, 1]

num_Needed = input("How many number You want? \n")
print("Fibonacci sequance:")

for x in range(0, num_Needed):
     if(x > 1):
         fib_numbers.insert(x, fib_numbers[x - 2] + fib_numbers[x - 1])
     
     text = str(x + 1) + ". " + str(fib_numbers[x])
     print(text)

     x = x + 1