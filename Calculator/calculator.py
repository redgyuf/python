bold = '\033[1m'
unbold = '\033[0m'

while True:
    try:
        first_num = float(input("Enter a number " \
        "(or a letter to " + bold + "exit" + unbold +"): "))    #Asking the User for inputs.
        operation = input("Enter an operation: ")
        second_num = float(input("Enter another number: "))

        if (operation == "+"):
            result = (first_num + second_num)    #Doing the correct math based on what operation entered.
        elif (operation == "-"):
            result = (first_num - second_num)
        elif (operation == "/"):
            result = (first_num / second_num)
        elif (operation == "*"):
            result = (first_num * second_num)

        print("Result: ", result, end='\n\n')    #Writing the result back to the user
    except:
        quit()    #If the user enters a letter instead of a number, the app quits.