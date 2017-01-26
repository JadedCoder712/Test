user = input("What is your name?")
user2 = input("What is five plus six, {0}?".format(user))
if int(user2) is 11:
    print("That's correct! Five plus six is {0}. And that minus two is {1}.".format(user2, int(user2)-2))
    print("You're very smart, {0}!".format(user))
if int(user2) > 11:
    user3 = input("No, {0} is too high! Try again, {1}. What is five plus six?".format(user2, user))
    if int(user3) is not 11:
        print("You're hopeless!")
if int(user2) < 11:
    user4 = input("No, {0} is too low! Try again, {1}. What is five plus six?".format(user2, user))
    if int(user4) is not 11:
        print("You're hopeless!")
