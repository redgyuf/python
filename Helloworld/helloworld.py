import sys    #Import sys, to be able to read arguments

#Converts all arguments into a single string.
def GetArgumentsToString():
    string = ""
    for x in range(1, len(sys.argv)):
        string += " " + sys.argv[x]
    return string

#Welcomes the given string, if empty string given, it welcomes the "World"
def WelcomeUser(UserName):
    if not UserName:   #Checks the given string for emptiness
        UserName = " World"
    print("Hello" + UserName + "!")

#This is where the program runs, "WelcomeUser" function called which gets the name from argument.
WelcomeUser(GetArgumentsToString())
