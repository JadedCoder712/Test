user = input("What is your name?")
user2 = input("What is five plus six, {0}?".format(user))
if user2 is 11:
    print("That's correct! Five plus six is {0}. And that minus two is {1}.".format(user2, int(user2)-2))
print("You're very smart, {0}!".format(user))