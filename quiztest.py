user = input("Would 3 = val be considered valid in Python? 1 for yes, 0 for no.")
if int(user) is not 0:
    wrong1 = input("You are wrong.")
user2 = input("Suppose you type a = 5 then b = a. Is this valid in Python? 1=yes, 0=no")
if int(user2) is not 1:
    wrong2 = input("You are wrong!")
user3 = input("What is the final value of b if you type a = 5 then b = a? Type your response as a number.")
if int(user3) is not 5:
    wrong3 = input("Wrong!")
user4 = input ("What is the final value of b if you type a = 5 then b = a? Type your response as a number.")
if int(user4) is not 5:
    wrong4 = input("You are wrong!")
if int(user) is not 0:
    print("You got number one wrong.")
if int(user2) is not 1:
    print("You got number two wrong.")
if int(user3) is not 5:
    print("You got number three wrong.")
if int(user4) is not 5:
    print("You got number four wrong.")
