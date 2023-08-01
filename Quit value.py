#read input from a user and store it in a list for later processing
values = []
print("Please enter values, Q to quit:")
userInput = input("")
while userInput.upper() != "Q" :
    values.append(float(userInput))
    userInput = input("")
